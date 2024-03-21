# PicPack: Bulk Image Zipper 📁

PicPack is a simple web application that allows users to download bulk images from the internet and zip them into a single file for easy download. It leverages Selenium for web scraping and Flask for the backend server.

## Features

- **Bulk Image Download**: Users can specify a celebrity name, the number of images they want to download, and the file type (PNG, JPG, or JPEG).
- **Zip Download**: The downloaded images are zipped into a single file for convenient download.
- **Simple UI**: The web interface is user-friendly and straightforward, making it easy for users to interact with the application.
- **Responsive Design**: The application is designed to work seamlessly.

## Technologies Used

- **Python**: Used for the backend server logic and web scraping with Selenium.
- **Flask**: A lightweight web framework used for handling HTTP requests and responses.
- **Selenium**: A powerful tool for automating web browsers, used here for web scraping to fetch images from the internet.
- **HTML/CSS**: Frontend markup and styling for the web interface.
- **JavaScript**: Used for client-side scripting to enhance user interaction.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask server:

    ```bash
    python app.py
    ```

4. Open a web browser and navigate to `http://localhost:5000` to access the PicPack application.

## Demo

https://github.com/JayeshJain246/PicPack/assets/77563599/1eed03b1-c866-4973-b5d6-0e928cea09d6

## Usage

1. Enter the celebrity name for which you want to download images.
2. Specify the number of images you want to download.
3. Choose the file type (PNG, JPG, or JPEG) from the dropdown menu.
4. Click on the "Download Images" button.
5. Wait for the images to be processed and zipped.
6. Once the download is ready, click on the download link provided to download the zip file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
