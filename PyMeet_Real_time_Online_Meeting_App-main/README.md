# 🧑🏻‍💻 PyMeet - Online Meeting Room Application

## 📌 Introduction
PyMeet is a simulated online meeting application that supports **real-time chat, voice chat, video call and multi-room features**.  
Built on a **Client-Server model with TCP & UDP**, the product aims to be **intuitive, understandable and extensible**.

---

## 👀 Goals
- Create a high-performance real-time communication platform.  
- Ensure basic security for login and data transmission.  
- Provide an intuitive, user-friendly interface using Tkinter.  

---

## 🔎 Features

### 💬 Text Chat (TCP)
- Reliable transmission with TCP (length-prefixed JSON).  
- Support for **group chat in rooms**.  
- Server routes messages to correct recipients.  

### 🎙️ Voice Chat (UDP)
- Audio transmission via **UDP** for low latency.  
- Uses **PyAudio** (16kHz, mono, PCM).  
- Support for microphone toggle.  

### 📹 Video Call (UDP)
- Webcam capture → JPEG compression → packet splitting (MTU 1200B) → UDP send.  
- Server relays frames by room.  
- Client assembles packets → decompresses → displays video.  
- Uses **sequence numbers** to skip corrupted frames.  
- Support for camera toggle.  

### 🏠 Multi-room
- Create/join/leave rooms.  
- Server maintains room list + members.  
- Lobby interface shows real-time user count.  

### 🔐 Security
- Login with **username + email**.  
- Session key **AES-256-GCM** for TCP messages.  
- Input validation (regex).  
- Rate limiting for UDP.  

### 🖥️ Interface
- **Tkinter GUI**: Login, Lobby, Room.  
- Mic/cam controls, chat, room participation.  
- WebSocket Gateway ⇄ UDP/TCP (extensible).  

---

## 🏗️ Architecture
- **Server**: manages users, rooms, data relay.  
- **Client**: sends/receives chat, audio, video.  
- **Multi-room**: supports parallel rooms.  

---

## 📋 Requirements
- Python 3.8+
- Libraries (see requirements.txt):
-	cryptography>=42.0
-	numpy>=1.24
-	pyaudio>=0.2.13
-	opencv-python>=4.9.0
-	(Optional): Pillow for smoother image processing in GUI.

---

## Installation

### 1. Install dependencies
```sh
pip install -r requirements.txt
```

### 2. (Optional) Install audio/video dependencies
#### For video processing:
```sh
pip install opencv-python
```

#### For audio processing (build tools required):
```sh
pip install pyaudio

```

---

## Quick Start

### 1. Start the server
```sh
python main.py
```

### 2. Start the GUI
```sh
python -m Client.meeting_gui_client
```


