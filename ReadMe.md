# Image Captioning and Text-to-Speech App

This is a Streamlit application that allows users to upload an image, generate a descriptive caption for the image using a pre-trained VisionEncoderDecoderModel, and convert the caption to speech using Google Text-to-Speech (gTTS).

## Features

- **Image Upload:** Users can upload an image in JPG, JPEG, or PNG format.
- **Image Captioning:** The app generates a descriptive caption for the uploaded image using a pre-trained VisionEncoderDecoderModel.
- **Text-to-Speech:** The app converts the generated caption to speech using gTTS.

## Usage

- Open the Streamlit app in your web browser.
- Upload an image by clicking on the "Choose an image..." button.
- The app will display the uploaded image and generate a descriptive caption for it.
- The generated caption will be displayed below the immage

## License

- This project is licensed under the MIT License.
- See the LICENSE file for details.


## Acknowledgements
- Streamlit
- Hugging Face Transformers
- Google Text-to-Speech (gTTS)

Make sure to replace `<repository-url>` and `<repository-name>` with the actual URL and name of your repository. This `README.md` file provides a comprehensive overview of your project, including installation instructions, usage, and a brief code overview.


## Installation

To run this application, you need to have Python installed on your system. Follow the steps below to set up the environment and run the app:

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-name>

2. **Setting up the environment** 
 ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   streamlit run app.py
   





