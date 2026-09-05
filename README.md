# OpenCV Learning Journey

This repository documents my first journey into **Computer Vision with Python**, mainly using **OpenCV** and **MediaPipe**.

I created this repository to keep track of what I learned, the experiments I made, and the projects I built while studying Computer Vision.

Rather than focusing only on the final project, I wanted to keep the learning process itself documented.

---

https://github.com/user-attachments/assets/e9182641-d870-4972-b596-627b83296dee

## 🎯 Goal

The goal of this repository was to understand the fundamentals of computer vision by building small experiments and gradually combining them into a real-time application.

During this journey, I worked with:

* Python
* OpenCV
* NumPy
* MediaPipe
* Image processing
* Video processing
* Face detection
* Hand landmark detection

---

# 📂 Project Structure

```text
OpenCV(Git)/
│
├── Face&HandDetection/
│   ├── haar_face.xml
│   ├── hand_landmarker.task
│   └── main.py
│
└── Tests/
    │
    ├── les1/
    ├── les2/
    ├── Ressources/
    │
    ├── 2d convultion.py
    ├── AVGFiltering.py
    ├── HSVColor
    ├── ImageHistogram
    ├── MedianFiltering
    ├── ReadandWritePixels
    └── ReadandWriteVideos
```

---

# 🧪 Tests

The `Tests` directory contains the experiments and exercises I made while learning the fundamentals of OpenCV.

## Image & Pixel Manipulation

### `ReadandWritePixels`

Experiments with accessing and modifying individual image pixels.

Concepts explored:

* Image arrays
* Pixel coordinates
* Reading pixel values
* Modifying pixels

### `ReadandWriteVideos`

Experiments with reading and processing video using OpenCV.

Concepts explored:

* `VideoCapture`
* Video frames
* Reading frames continuously
* Displaying video
* Working with webcams

---

## 🎨 Color Processing

### `HSVColor`

Experiments with the HSV color space.

Topics explored:

* BGR vs RGB
* HSV
* `cv.cvtColor()`
* Color ranges
* Color masking with `cv.inRange()`

This helped me understand how computers represent and process colors.

---

## 📊 Image Analysis

### `ImageHistogram`

Experiments with image histograms.

Topics explored:

* Pixel intensity distribution
* Histograms
* `cv.calcHist()`
* Understanding image brightness and color distribution

---

## 🌀 Image Filtering

### `2d convultion.py`

Experiments with 2D convolution and kernels.

Topics explored:

* Kernels
* Convolution
* `cv.filter2D()`
* How neighboring pixels can be used to transform an image

### `AVGFiltering.py`

Experiments with average filtering and blurring.

Topics explored:

* Average filters
* Kernels
* Blurring
* Noise reduction

### `MedianFiltering`

Experiments with median filtering.

Topics explored:

* Median filters
* Noise reduction
* Differences between average and median filtering

---

# 👤 Face Detection

## `Face&HandDetection`

This is the main project I built during this learning journey.

It combines **OpenCV Haar Cascade face detection** with **MediaPipe hand tracking** in a real-time webcam application.

### Technologies

* Python
* OpenCV
* MediaPipe

### Face Detection

The face detector uses a Haar Cascade classifier.

The general pipeline is:

```text
Camera
   ↓
Video Frame
   ↓
Grayscale
   ↓
Haar Cascade
   ↓
Face Detection
   ↓
Bounding Boxes
```

The project uses:

```text
haar_face.xml
```

as the trained Haar Cascade model.

---

# ✋ Hand Tracking

The project also uses MediaPipe to detect hands and their landmarks.

The pipeline is approximately:

```text
Camera
   ↓
Video Frame
   ↓
BGR → RGB
   ↓
MediaPipe Hands
   ↓
Hand Landmarks
   ↓
Draw Connections
```

The project uses:

```text
hand_landmarker.task
```

for hand landmark detection.

---

# 🔗 Combining Both

The final experiment combines the two computer vision pipelines:

```text
                  Camera
                    ↓
                  Frame
               ┌────┴────┐
               ↓         ↓
          Grayscale      RGB
               ↓         ↓
        Haar Cascade   MediaPipe
               ↓         ↓
          Face(s)      Hand(s)
               └────┬────┘
                    ↓
               Final Frame
```

This was my first attempt at combining multiple computer vision systems into one real-time application.

---

# 📚 What I Learned

Throughout this project, I learned and practiced:

* How images are represented as arrays
* Reading and writing images
* Reading webcam/video frames
* BGR and RGB
* HSV color space
* Color masking
* Image histograms
* 2D convolution
* Kernels
* Image filtering
* Average filtering
* Median filtering
* Grayscale images
* Haar Cascade face detection
* Real-time face detection
* MediaPipe hand tracking
* Hand landmarks
* Combining multiple computer vision pipelines
* Working with external model files
* Structuring a Python project

---

# 🚀 Final Result

The final project, `Face&HandDetection`, represents the transition from small OpenCV experiments to a real-time computer vision application.

The purpose of this repository is not to present myself as an expert in Computer Vision, but to document the process of learning, experimenting, debugging, and building.

---

# 🧠 Learning Philosophy

I believe that understanding the fundamentals is more important than simply copying a finished project.

For that reason, this repository contains both:

**small experiments → larger project**

The `Tests` folder represents the learning process, while `Face&HandDetection` represents the application of what I learned.

---

# 🗺️ My Long-Term Learning Journey

Computer Vision is one part of a much broader technical journey I am building.

My long-term goal is to develop a deep understanding of computers and technology from the fundamentals upward, rather than limiting myself to a single specialization.

The areas I want to explore include:

```text
Programming
    ↓
Python → C → Software Development
    ↓
Computer Science & Algorithms
    ↓
Operating Systems & Linux
    ↓
Computer Systems
    ↓
Networking & CCNA
    ↓
Network Programming
    ↓
Cybersecurity & Security Research
    ↓
Artificial Intelligence & Machine Learning
    ↓
Computer Vision
```

These areas are interconnected rather than isolated.

I want to understand how software interacts with operating systems, how computers communicate through networks, how systems can be secured and tested, and eventually how AI and machine learning can be used to build intelligent systems.

My interests therefore span several overlapping fields, including:

* Computer Science
* Software Engineering
* Systems Engineering
* Linux and Operating Systems
* Networking
* Cybersecurity
* Security Research
* Artificial Intelligence
* Machine Learning
* Computer Vision

The long-term direction I am working toward is becoming a **strong systems-oriented programmer and engineer with expertise across networking, security, and AI/ML**.

---

# 📈 What's Next?

Computer Vision is currently a **side project** in my overall learning journey.

After exploring the fundamentals of OpenCV and building this project, my next major focus is **Networking and CCNA**.

I want to use networking as a bridge between programming and systems, while continuing to develop my Python skills and gradually moving toward:

```text
Networking
    ↓
CCNA
    ↓
Linux & Operating Systems
    ↓
Python for Networking
    ↓
Systems & Software
    ↓
Cybersecurity & Security Research
    ↓
AI / ML
    ↓
Advanced Computer Vision
```

This repository represents one stage of that larger journey.

---

## 👨‍💻 Author

**Raisky**

Learning Python, Computer Science, Systems, Linux, Networking, Cybersecurity, AI/ML and Computer Vision.

> This repository represents one step in my programming journey.
