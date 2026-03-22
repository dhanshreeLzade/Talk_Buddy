# Talk_Buddy

## Project Overview

Talk Buddy is a Python-based application that converts text into clear, natural-sounding audio. It is built using Streamlit for the user interface and pyttsx3 for text-to-speech functionality.

The application allows users to input raw text, automatically clean and format it, and listen to the processed content as spoken audio. It is designed to support learning, storytelling, and accessibility through audio.

---

## Features

* Text-to-Speech Conversion
* Automatic Text Cleaning (removal of extra spaces and formatting issues)
* Simple and Interactive UI using Streamlit
* Offline Audio Generation using pyttsx3
* Real-time Text Processing and Playback

---

## Technologies Used

* Python
* Streamlit
* pyttsx3 (Text-to-Speech Engine)

---

## Project Structure

```
Talk_Buddy/
│
├── app.py              # Main Streamlit application
├── utils.py            # Text cleaning and helper functions
├── requirements.txt    # Project dependencies
└── README.md
```

---

## Setup Instructions

1. Clone the repository
   git clone <your-repo-link>

2. Install dependencies
   pip install -r requirements.txt

3. Run the application
   streamlit run app.py

4. Open in browser

   * The app will run on http://localhost:8501

---

## How It Works

The user inputs raw text into the application interface. The system processes the text by removing unnecessary spaces and formatting inconsistencies. The cleaned text is then converted into audio using the pyttsx3 engine, allowing users to listen to the content.

---

## Use Cases

* Listening to study material
* Story narration
* Accessibility support for reading
* Quick audio conversion of written content

---

## Author

Dhanashree Zade
Developed the application using Python, focusing on text processing and audio generation.

---

## Future Enhancements

* Add voice customization options
* Support for multiple languages
* Downloadable audio files
* Improved UI/UX design

---

## License

This project is open-source and available for learning and development purposes.

