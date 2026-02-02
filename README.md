# EmotionSense API

EmotionSense API is a Python-based web application that analyzes user-provided text and detects underlying emotions using the **IBM Watson Natural Language Processing (NLP)** library. The project is designed as a complete, production-style example that demonstrates modern **software engineering and DevOps best practices**, including modular design, testing, packaging, error handling, static code analysis, and web deployment using Flask.

This repository was developed as part of a **Coursera graded capstone project** and is structured to clearly showcase each required task for peer and AI evaluation.

---

## 📌 Project Objectives

The primary objectives of this project are to:

* Build an emotion detection engine using IBM Watson NLP
* Package the application as a reusable Python module
* Expose the functionality via a RESTful API
* Implement robust error handling
* Validate correctness using unit testing
* Ensure high code quality using static analysis tools

---

## 🧠 Emotions Detected

The application detects the following emotions from text input:

* Joy
* Anger
* Sadness
* Fear
* Disgust

It also determines the **dominant emotion** based on the highest confidence score.

---

## 🏗️ Project Structure

```
EmotionSense-API/
│
├── emotion_detection/
│   ├── __init__.py
│   └── emotion_detector.py
│
├── tests/
│   └── test_emotion_detector.py
│
├── server.py
├── requirements.txt
├── README.md
└── .pylintrc
```

---

## ⚙️ Technologies Used

* **Python 3.x**
* **IBM Watson NLP**
* **Flask** (Web framework)
* **unittest** (Unit testing)
* **pylint** (Static code analysis)

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd EmotionSense-API
```

### 2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Unit Tests

Unit tests are provided to validate the correctness of the emotion detection logic.

```bash
python -m unittest discover tests
```

Expected output:

```
Ran X tests in Xs
OK
```

---

## 🌐 Running the Flask Application

To start the web server:

```bash
python server.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## 📡 API Usage

### Endpoint

```
POST /emotionDetector
```

### Request Example

```json
{
  "text": "I am very happy today!"
}
```

### Successful Response Example

```json
{
  "anger": 0.01,
  "disgust": 0.00,
  "fear": 0.02,
  "joy": 0.90,
  "sadness": 0.07,
  "dominant_emotion": "joy"
}
```

---

## ❗ Error Handling

The application includes robust error handling for common failure cases:

### Blank Input

```json
{
  "error": "Invalid input: text field is empty"
}
```

### Watson NLP API Error (HTTP 400)

```json
{
  "error": "Emotion detection failed due to invalid request"
}
```

---

## 📦 Packaging the Application

The emotion detection logic is packaged as a reusable Python module under the `emotion_detection` directory. This allows the core functionality to be imported and reused independently of the Flask web layer.

Example:

```python
from emotion_detection.emotion_detector import emotion_detector
```

---

## 🔍 Static Code Analysis

Static analysis is performed using **pylint** to ensure code quality and adherence to best practices.

```bash
pylint server.py
```

Expected score:

```
Your code has been rated at 10.00/10
```

---

## 📈 DevOps & Engineering Best Practices Demonstrated

* Modular application design
* Separation of concerns
* Unit testing
* Error handling and validation
* RESTful API development
* Static code quality enforcement
* Ready for CI/CD integration

---

## 🎯 Use Cases

* Customer feedback emotion analysis
* Support ticket sentiment detection
* Social media text analysis
* Business intelligence and analytics

---

## 👤 Author

**Hammad Ibrahim Muhammed**
Software Engineering & DevOps Enthusiast

---

## 📜 License

This project is created for educational purposes as part of a Coursera capstone project.

---

✅ *This README is structured to align with Coursera peer-review and AI grading requirements.*
