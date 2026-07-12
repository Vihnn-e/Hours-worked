# ⏳ Work Hours Monitor

A lightweight, background Python script that tracks the exact amount of time you spend actively working in specified productivity and development applications. 

It works by checking your active desktop window title every 10 seconds and calculating the elapsed time dynamically.

---

## 🚀 Features
* **Automatic Detection:** Automatically tracks time when any of your specified work apps are in focus.
* **Smart Pausing:** Automatically pauses tracking when you switch away from work apps (e.g., to a browser tab or game not on your list) and resumes when you return.
* **Live Update:** Displays a real-time terminal counter of your total accumulated work time in minutes.
* **Multithreaded Execution:** Runs the monitoring logic in the background so you can safely stop the script at any time by typing a command.

---

## ⚙️ Monitored Applications
By default, the script tracks the following applications (case-insensitive):
* 💻 **PyCharm**
* 🌐 **Brave Browser**
* 📊 **Microsoft Excel**
* 📝 **Microsoft Word**
* 🛠️ **VS Code**

*(You can easily add more to the `Work_Apps` list inside the script!)*

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
Make sure you have Python 3.x installed on your machine.

### 2. Install Dependencies
This script relies on the `pygetwindow` library to monitor active window titles. Open your terminal or command prompt and run:

```bash
pip install pygetwindow
