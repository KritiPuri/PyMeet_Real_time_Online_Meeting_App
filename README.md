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
  - `cryptography>=42.0`
  - `numpy>=1.24`
  - `pyaudio>=0.2.13`
  - `opencv-python>=4.9.0`
  - (Optional): `Pillow` for smoother image processing in GUI.

---

## 📦 Installation

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

## 🚀 Quick Start

### 1. Start the server
```sh
python main.py
```

### 2. Start the GUI
```sh
python -m Client.meeting_gui_client
```

---

## 📸 Screenshots & Outputs

The application interface and features are demonstrated in the following screenshots located in the `outputs/` folder:

### 1. Login Screen
![Login Screen](outputs/1.png)
- User authentication interface
- Username and email input fields
- Secure login with validation

### 2. Lobby Interface
![Lobby Interface](outputs/2.png)
- Real-time room listing
- Active user count display
- Create/Join room functionality
- User-friendly navigation

### 3. Meeting Room - Text Chat
![Meeting Room](outputs/3.png)
- Real-time text chat interface
- Room member list
- Message history
- Audio/Video controls

### 4. Video Call Features
![Video Call](outputs/4.png)
- Multi-user video conferencing
- Real-time video streaming
- Audio communication
- Interactive control panel (Mic/Camera toggle)

---

## 🔧 Technical Details

### Network Protocol
- **TCP**: Reliable message transmission for text chat and control messages
- **UDP**: Low-latency streaming for audio and video data
- **WebSocket Gateway**: Optional extensibility for web clients

### Data Flow
1. **Client Authentication** → Server validates credentials
2. **Room Management** → Create/Join/Leave operations via TCP
3. **Text Messages** → JSON-encoded, AES-256-GCM encrypted
4. **Audio Packets** → 16kHz PCM, transmitted via UDP
5. **Video Frames** → JPEG-compressed, split into MTU-sized packets (1200B)

### Security Features
- AES-256-GCM encryption for TCP messages
- Session-based authentication
- Input validation and sanitization
- Rate limiting on UDP streams

---

## 📁 Project Structure

```
PyMeet_Real_time_Online_Meeting_App-main/
├── main.py                      # Server entry point
├── Client/                      # Client-side code
│   ├── meeting_gui_client.py    # Main GUI application
│   ├── gui_login.py             # Login interface
│   ├── gui_lobby.py             # Lobby interface
│   ├── gui_room.py              # Meeting room interface
│   ├── gateway.py               # Client gateway
│   └── requirements.txt         # Client dependencies
├── server/                      # Server-side code
│   ├── tcp_server.py            # TCP server implementation
│   ├── udp_server.py            # UDP server implementation
│   ├── auth.py                  # Authentication logic
│   ├── rooms.py                 # Room management
│   ├── routing.py               # Message routing
│   └── users_db.json            # User database
├── advanced_feature/            # Advanced features
│   ├── video_call.py            # Video call implementation
│   ├── voice_chat.py            # Voice chat implementation
│   ├── config_server.py         # Server configuration
│   └── config_client.py         # Client configuration
├── gateway/                     # WebSocket gateway
│   └── gateway_ws.py            # WebSocket implementation
└── outputs/                     # Application screenshots
    ├── 1.png                    # Login screen
    ├── 2.png                    # Lobby interface
    ├── 3.png                    # Meeting room
    └── 4.png                    # Video call features
```

---

## 🛠️ Usage Guide

### For Users
1. **Login**: Enter username and email to authenticate
2. **Lobby**: View available rooms or create a new one
3. **Join Room**: Click on a room to enter the meeting
4. **Chat**: Send text messages to all participants
5. **Voice**: Toggle microphone to enable/disable audio
6. **Video**: Toggle camera to enable/disable video stream
7. **Leave**: Exit room to return to lobby

### For Developers
- Extend features in `advanced_feature/` directory
- Modify GUI in `Client/` directory
- Customize server logic in `server/` directory
- Add protocols in `server/protocol.py`

---

## 🐛 Troubleshooting

### Common Issues

**Audio not working:**
- Ensure PyAudio is properly installed
- Check microphone permissions
- Verify audio device availability

**Video not displaying:**
- Verify OpenCV installation
- Check camera permissions
- Ensure webcam is connected

**Connection failed:**
- Verify server is running on correct port
- Check firewall settings
- Ensure network connectivity

**Installation errors:**
- Use Python 3.8 or higher
- Install build tools for PyAudio (Windows: Visual C++, Linux: portaudio-dev)

---

## 📝 License
This project is open-source and available for educational purposes.

---

## 👥 Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

---

## 📧 Contact
For questions or support, please open an issue in the repository.

---

## 🙏 Acknowledgments
- Built with Python, Tkinter, PyAudio, and OpenCV
- Inspired by modern video conferencing platforms
- Designed for educational purposes in computer networking

---

**⭐ Star this repository if you find it helpful!**
