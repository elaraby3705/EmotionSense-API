# EmotionSense API 🧠📊

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![AI Service](https://img.shields.io/badge/AI-IBM%20Watson%20NLP-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**EmotionSense API** is a modular, production-ready Python web application that analyzes text to detect underlying emotions using the **IBM Watson Natural Language Processing (NLP)** library.

Built with a **DevOps-first mindset**, this project demonstrates modern software engineering practices including modular architecture, test-driven development (TDD), static code analysis, and secure configuration management.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture & Design](#-architecture--design)
- [Technology Stack](#-technology-stack)
- [Installation & Setup](#-installation--setup)
- [Configuration (Security)](#-configuration-security)
- [Usage Guide](#-usage-guide)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Project Roadmap (Milestones)](#-project-roadmap-milestones)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 📖 Project Overview

The primary goal of EmotionSense is to expose a robust AI engine via a RESTful API. It takes raw user text, processes it through IBM's Watson NLP service, and returns a structured JSON response indicating the dominance of specific emotions.

This repository was developed as a **Coursera Capstone Project** but has been elevated to meet professional backend standards.

---

## 🚀 Key Features

* **Real-time Emotion Analysis:** Detects Joy, Anger, Sadness, Fear, and Disgust.
* **Dominant Emotion Logic:** Automatically calculates and returns the strongest emotion.
* **Modular Design:** The core logic (`emotion_detection`) is decoupled from the web server (`server.py`), allowing for easy reuse.
* **Robust Error Handling:** Manages API failures, network issues, and invalid inputs gracefully (400/500 errors).
* **Security Best Practices:** Uses Environment Variables (`.env`) to protect sensitive API keys.

---

## 🏗 Architecture & Design

The system follows a strict **Separation of Concerns**:

1.  **Core Logic (Engine):** Handles the communication with IBM Watson and data formatting.
2.  **Web Layer (Interface):** A Flask server that routes HTTP requests to the engine.
3.  **Client:** Any frontend or tool (like Postman/cURL) that consumes the JSON API.

### Logic Flow
`User Input` -> `Input Validation` -> `IBM Watson API` -> `Data Parsing` -> `Dominant Emotion Calculation` -> `JSON Response`

---

## ⚙️ Technology Stack

* **Language:** Python 3.x
* **Web Framework:** Flask
* **AI Engine:** IBM Watson NLP
* **HTTP Client:** Requests
* **Testing:** Unittest
* **Linting:** Pylint
* **Configuration:** Python-Dotenv

---

## 🛠 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/EmotionSense-API.git](https://github.com/your-username/EmotionSense-API.git)
cd EmotionSense-API