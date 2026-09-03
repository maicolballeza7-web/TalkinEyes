# TalkinEyes 👁️

> **Give a voice to those who can only blink.**

TalkinEyes is an accessibility-focused communication prototype that uses **eye blinks as an input method**.

The idea is simple: a camera tracks the user's eyes, intentional blinks are detected, and the system uses them to navigate a visual menu and select phrases that can be spoken aloud using text-to-speech.

The project started with one question:

**What if blinking could become a way to communicate?**

---

## 💡 The Problem

For people with severe motor or speech limitations, communicating basic needs can be difficult when using a keyboard, mouse, or touchscreen is not possible or practical.

TalkinEyes explores whether **computer vision and intentional eye blinks** can provide another way to interact with a communication interface.

It is not intended to replace professional assistive communication devices. It is a prototype exploring what could be possible.

---

## 🔎 How It Works

```text
Camera
  ↓
MediaPipe Face Landmarks
  ↓
Eye landmarks
  ↓
EAR calculation
  ↓
Blink detection
  ↓
Menu navigation
  ↓
Phrase selection
  ↓
Text-to-Speech
```

TalkinEyes uses the **Eye Aspect Ratio (EAR)** to estimate whether the eyes are open or closed.

To avoid treating every natural blink as a selection, the system also considers the **duration of the eye closure**.

This allows the user to:

**Look → Wait → Blink → Communicate**

---

## ✨ Features

* 👁️ Real-time eye tracking
* 📐 Eye Aspect Ratio (EAR) calculation
* 🧠 Intentional blink detection
* 🔄 Automatic menu scanning
* 🖱️ Interaction without a mouse
* 🗣️ Text-to-speech
* 📋 Categories and submenus
* 🎨 Simple, high-contrast interface
* 📷 Real-time camera processing

Current categories include:

* 🍽️ Food
* 🚿 Bathroom
* 🩹 Pain
* 😴 Sleep
* 🆘 Help

---

## 🛠️ Built With

* **Python**
* **OpenCV** — camera and computer vision
* **MediaPipe** — facial landmarks
* **NumPy** — numerical calculations
* **Tkinter** — graphical interface
* **pyttsx3** — text-to-speech
* **Git & GitHub** — version control

---

## 🚀 Getting Started

### Requirements

* Windows
* Python 3
* Webcam

Clone the repository:

```bash
git clone https://github.com/maicolballeza7-web/TalkinEyes.git
cd TalkinEyes
```

Install the dependencies:

```bash
pip install opencv-python mediapipe numpy pyttsx3 pywin32
```

Run the project:

```bash
python TalkinEyes.py
```

> The current prototype is primarily designed for Windows because of its speech implementation.

---

## ♿ Accessibility

TalkinEyes was designed around a simple interaction model:

> **Look → Wait → Blink → Communicate**

The interface uses large options and automatic highlighting so that the user does not need to physically reach a keyboard or mouse during normal interaction.

The goal is to make the interaction as simple as possible while keeping the system understandable.

---

## 🔐 Privacy & Safety

TalkinEyes is currently a **local prototype**.

The camera is used for real-time facial landmark detection, and the current implementation does not intentionally upload or store camera frames.

This project is **not a medical device** and has not been clinically validated.

Before being considered for real-world assistive use, it would require much more testing, reliability validation, accessibility testing, and feedback from potential users and professionals.

---

## ⚠️ Limitations

This is still an experimental project.

Detection can be affected by:

* Lighting conditions
* Camera position
* Individual blinking patterns
* Facial landmark accuracy
* Different eye shapes and movements

The current system also has a limited vocabulary and may require individual calibration to work reliably for different users.

---

## 🌱 What's Next?

Some improvements I would like to explore:

* Individual eye calibration
* More communication categories and phrases
* Better false-positive prevention
* More robust detection in different environments
* Customizable phrases
* Improved text-to-speech support
* Testing with real users and accessibility experts

---

## 🧑‍💻 Why I Built This

I started learning programming relatively recently, and TalkinEyes grew out of my curiosity about **Python and computer vision**.

While learning how facial landmarks and eye detection worked, I started wondering if something as simple as a blink could be used for something more meaningful.

So I decided to build it.

I learned many of the technologies used here while developing the project — from calculating EAR and working with MediaPipe to building the interface, handling real-time camera input, and connecting everything with text-to-speech.

It is not a perfect system, and I still have a lot to learn.

But I wanted to use what I was learning to build something that could potentially **help someone communicate**.

---

## 📖 Development

TalkinEyes went through several stages:

```text
Camera experiment
       ↓
Face & eye detection
       ↓
EAR calculation
       ↓
Blink detection
       ↓
Intentional blink detection
       ↓
Interactive menu
       ↓
Submenus
       ↓
Text-to-Speech
       ↓
TalkinEyes
```

The development process, experiments, and progress are documented in the project devlog.

---

## 📌 Project Status

**Functional prototype — still under development.**

TalkinEyes can currently detect eye movements, identify intentional closures, navigate menus, select phrases, and convert those selections into speech.

The project is being developed as a learning experience as well as an exploration of accessible human-computer interaction.

---

## ❤️ Final Note

TalkinEyes started as a programming experiment.

It became something more when I realized that the things I was learning could be used to explore a real human problem.

**Built with Python, computer vision, curiosity, and a lot of learning. 👁️**
