# Driver Drowsiness Alert System

A real-time computer vision system that detects driver fatigue using a Convolutional Neural Network (CNN) and facial landmark detection. The system monitors the driver's eye state through a webcam and triggers an alarm if drowsiness is detected.

---

## Project Overview

Driver fatigue is one of the leading causes of road accidents. This project aims to reduce such incidents by detecting early signs of drowsiness in drivers.

The system continuously monitors the driver's eyes using a webcam and uses a trained CNN model to classify whether the eyes are open or closed. If the eyes remain closed for a prolonged period, an alarm is triggered to alert the driver.

---

## Features

* Real-time driver monitoring using webcam
* Face detection using facial landmarks
* Eye state classification using a CNN model
* Alarm alert system when drowsiness is detected
* Continuous tracking of driver attention

---

## Technologies Used

* Python
* OpenCV
* TensorFlow / Keras
* NumPy
* dlib
* pygame
* imutils

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/amanjsg02/Drowsiness-Alert-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Drowsiness-Alert-System
```

### 3. Install Dependencies

Install the required libraries using:

```bash
pip install -r requirements.txt
```

If you do not have a requirements file, install manually:

```bash
pip install opencv-python numpy dlib tensorflow pygame imutils
```

---

## Running the Project

Run the main Python script:

```bash
python drowziness.py
```

### Steps

1. The webcam will start automatically.
2. The system detects the driver's face.
3. The eye region is extracted and analyzed.
4. The CNN model predicts whether the eyes are open or closed.
5. If the eyes remain closed for multiple frames, an alarm is triggered.

Press **q** to exit the program.

---

## Project Structure

```
Drowsiness-Alert-System
│
├── drowziness.py
├── drowziness_model2.h5
├── CnnEyeDetector.ipynb
├── shape_predictor_68_face_landmarks.dat
├── AlarmTone.mp3
├── requirements.txt
└── README.md
```

## Future Improvements

* Improve model accuracy with larger datasets
* Deploy the system on embedded devices such as Raspberry Pi
* Integrate mobile notifications
* Improve face tracking and eye detection algorithms
---

## Run the Executable Version

You can download the ready-to-run application from the release page:

🔗 https://github.com/amanjsg02/Drowsiness-Alert-System/releases/tag/v1.0

### Note

* The provided **drowziness.exe** file is built for **Windows operating systems only**.
* Users on **macOS or Linux** should run the project using the Python source code provided in this repository.
* When running the executable for the first time, Windows Defender may show a warning because the file is not digitally signed. Click **"More info → Run anyway"** to proceed.

### Instructions to Run

1. Download **drowziness.exe** from the release page.
2. Double-click the file to start the application.
3. Allow webcam access if prompted.
4. Maintain a proper sitting distance from the webcam for accurate detection.
5. Select the **ROI (Region of Interest)** around the face and press **Enter**.
6. Press **Q** to close the application.


https://github.com/amanjsg02

