# from flask import Flask, render_template, request, send_file
# import os
# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import shutil
# import zipfile

# app = Flask(__name__)
# def remove_previous_zips():
#     folder_path = "static/celeb_photos"
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".zip"):
#             os.remove(os.path.join(folder_path, filename))  

# def image_scrapper(query, no_of_photos=50,file_type='png'):
#     # Set Chrome options and service
#     options = Options()
#     options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

#     driver_version = "123.0.0.0"
#     manager = ChromeDriverManager(version=driver_version)
#     driver_path = manager.install()
#     service = Service(driver_path)

#     # service = Service(ChromeDriverManager().install())

#     # Initialize the Chrome driver
#     driver = webdriver.Chrome(service=service, options=options)

#     # Construct the Google Images URL with the search query
#     url = f'https://www.google.com/search?tbm=isch&q={query}'

#     # Open the Google Images page
#     driver.get(url)

#     # Scroll down to load more images
#     scroll_pause_time = 2
#     scroll_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(scroll_pause_time)
#         new_scroll_height = driver.execute_script("return document.body.scrollHeight")
#         if new_scroll_height == scroll_height:
#             break
#         scroll_height = new_scroll_height

#     # Find all image elements using XPath
#     images_tags = driver.find_elements(By.XPATH, "//img[@class='rg_i Q4LuWd']")

#     # Extract image URLs from the image elements
#     images_urls = [img.get_attribute('src') for img in images_tags if img.get_attribute('src')]

#     folder_path = f"static/celeb_photos/{query}"  # Change this to your desired folder path

#     # Check if the folder exists, if not, create it
#     # remove_previous_zips()
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     for i, url in enumerate(images_urls[:no_of_photos+20]):
#         try:
#             # Download the image
#             image_response = requests.get(url)
#             image_response.raise_for_status()
    
            
#             # Save the image to a file
#             with open(os.path.join(folder_path, f"image_{i}.{file_type}"), "wb") as file:
#                 file.write(image_response.content)

#         except Exception as e:
#             print(f"Error downloading image {i}: {e}")

#     driver.quit()

#     # Zip the downloaded images
#     remove_previous_zips()
#     zip_filename = f"static/celeb_photos/{query}.zip"
#     shutil.make_archive(os.path.join("static/celeb_photos", query), 'zip', folder_path)

#     # Remove the image folder after zipping
    
#     shutil.rmtree(folder_path)
    

#     return zip_filename

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/download', methods=['POST'])
# def download():
#     if request.method == 'POST':
#         celeb_name = request.form['celeb_name']
#         celeb_name  = celeb_name.replace(" ", "+")
#         no_of_photos = int(request.form['no_of_photos'])
#         file_type = request.form['file_type']
#         zip_filename = image_scrapper(celeb_name,no_of_photos,file_type)
#         return send_file(zip_filename, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)

# # if __name__ == '__main__':
# # #     # app.run(debug=False, host='0.0.0.0')
# #     app.run(debug=True)


from flask import Flask, render_template, request, send_file
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import shutil
import zipfile
import platform

app = Flask(__name__)

def get_chrome_driver_path():
    # Determine the platform and architecture of the remote server
    platform_name = platform.system().lower()
    architecture = platform.architecture()[0]

    # Choose the appropriate version of the Chrome driver based on the platform and architecture
    if platform_name == "linux":
        if architecture == "64bit":
            driver_version = "latest"
        else:
            raise ValueError("Chrome driver not available for 32-bit Linux")
    elif platform_name == "windows":
        if architecture == "64bit":
            driver_version = "latest"
        else:
            raise ValueError("Chrome driver not available for 32-bit Windows")
    elif platform_name == "darwin":
        driver_version = "latest"

    # Install the Chrome driver using the selected version
    return ChromeDriverManager().install()

def image_scrapper(query, no_of_photos=50, file_type="png"):
    # Set Chrome options and service
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    # Initialize the Chrome driver
    service = Service(get_chrome_driver_path())

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=options)

    # Construct the Google Images URL with the search query
    url = f'https://www.google.com/search?tbm=isch&q={query}'

    # Open the Google Images page
    driver.get(url)

    # Scroll down to load more images
    scroll_pause_time = 2
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        if new_scroll_height == scroll_height:
            break
        scroll_height = new_scroll_height

    # Find all image elements using XPath
    images_tags = driver.find_elements(By.XPATH, "//img[@class='rg_i Q4LuWd']")

    # Extract image URLs from the image elements
    images_urls = [img.get_attribute('src') for img in images_tags[:no_of_photos+20] if img.get_attribute('src')]

    folder_path = f"static/celeb_photos/{query}"  # Change this to your desired folder path

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for i, url in enumerate(images_urls[:no_of_photos+20]):
        try:
            # Download the image
            image_response = requests.get(url)
            image_response.raise_for_status()

            # Save the image to a file
            with open(os.path.join(folder_path, f"image_{i}.{file_type}"), "wb") as file:
                file.write(image_response.content)

        except Exception as e:
            print(f"Error downloading image {i}: {e}")

    driver.quit()

    # Zip the downloaded images
    zip_filename = f"static/celeb_photos/{query}.zip"
    shutil.make_archive(os.path.join("static/celeb_photos", query), 'zip', folder_path)

    # Remove the image folder after zipping
    shutil.rmtree(folder_path)

    return zip_filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        celeb_name = request.form['celeb_name']
        no_of_photos = int(request.form['no_of_photos'])
        file_type = request.form['file_type']
        zip_filename = image_scrapper(celeb_name, no_of_photos, file_type)
        return send_file(zip_filename, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
