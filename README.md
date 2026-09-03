# TalkinEyes 👁️

> **Give a voice to those who can only blink.**

TalkinEyes is an accessibility-focused communication prototype that uses **intentional eye blinks as an input method**.

A camera tracks the user's eyes, detects intentional closures, and uses them to navigate a visual menu. When an option is selected, the corresponding phrase can be spoken aloud using text-to-speech.

The project started with one question:

**What if blinking could become a way to communicate?**

---

## 💡 The Problem

For people with severe motor or speech limitations, communicating basic needs can become difficult when using a keyboard, mouse, or touchscreen is not practical.

TalkinEyes explores whether **computer vision and intentional eye blinks** can provide another way to interact with a communication interface.

It is not intended to replace professional assistive communication devices. It is an experimental prototype exploring what could be possible.

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
Menu scanning
   ↓
Phrase selection
   ↓
Text-to-Speech
```

TalkinEyes uses the **Eye Aspect Ratio (EAR)** to estimate whether the eyes are open or closed.

Because a normal blink should not automatically select an option, the system also considers the **duration of the eye closure**.

The interaction is designed around a simple flow:

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

Current communication categories include:

* 🍽️ Food
* 🚿 Bathroom
* 🩹 Pain
* 😴 Sleep
* 🆘 Help

---

## 🛠️ Built With

* **Python**
* **OpenCV** — camera and computer vision
* **MediaPipe** — facial landmark detection
* **NumPy** — numerical calculations
* **Tkinter** — graphical interface
* **pyttsx3** — text-to-speech
* **Git & GitHub** — version control

---

## 📂 Project Structure

```text
TalkinEyes/
│
├── TalkinEyes.py
│   └── Main application
│
├── TalkinEyesV0.py
│   └── Earlier prototype
│
├── camra.py
│   └── Camera and computer vision experiments
│
├── formulas.md
│   └── EAR calculations and eye landmarks
│
└── TalkinEyes Dvlog.md
    └── Development journey and experiments
```

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

The interface uses large options and automatic highlighting so the user can make selections without physically reaching a keyboard or mouse during normal interaction.

The goal is to keep the interaction simple, predictable, and easy to understand.

---

## 🔐 Privacy & Safety

TalkinEyes is currently a **local prototype**.

The camera is used for real-time facial landmark detection, and the current implementation does not intentionally upload or store camera frames.

This project is **not a medical device** and has not been clinically validated.

Real-world assistive use would require significantly more testing, reliability validation, accessibility testing, and feedback from potential users and professionals.

---

## ⚠️ Limitations

TalkinEyes is still an experimental prototype.

Detection can be affected by:

* Lighting conditions
* Camera position
* Individual blinking patterns
* Facial landmark accuracy
* Different eye movements

The current system also has a limited vocabulary and may require individual calibration for different users.

---

## 🌱 What's Next?

Future improvements could include:

* Individual eye calibration
* More communication categories and phrases
* Better false-positive prevention
* More robust detection in different environments
* Customizable phrases
* Improved text-to-speech support
* Testing with real users and accessibility experts

---

## 📌 Project Status

**Functional prototype — still under development.**

The current prototype can:

* Detect facial and eye landmarks
* Calculate EAR
* Detect intentional eye closures
* Automatically navigate communication menus
* Select phrases using eye blinks
* Navigate submenus
* Convert selected phrases into speech

The project is currently focused on proving the interaction concept and improving reliability before considering more advanced features.

---

## 👋 About the Project

I’m a **17-year-old student from Mexico studying at BUAP**, and I started learning programming about three months ago.

TalkinEyes began as a way to learn Python and computer vision. While experimenting with facial landmarks and eye detection, I started wondering if something as simple as a blink could be used for something more meaningful.

I developed the project independently and learned many of the technologies while building it. I also used **AI as a learning and development tool** to understand concepts, debug problems, explore ideas, and move faster.

AI was part of the process, but I still had to understand the code, test the system, make decisions, and connect the different pieces into a working prototype.

For me, TalkinEyes represents more than what I have learned about programming. It is an attempt to use those new skills to explore a real human problem:

**How could technology help someone communicate?**

---

## 📖 Development Journey

TalkinEyes evolved through several stages:

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

## ❤️ Final Note

TalkinEyes started as a programming experiment.

It became something more when I realized that the things I was learning could be used to explore a real human problem.

**Built with Python, computer vision, curiosity, and a lot of learning. 👁️**
