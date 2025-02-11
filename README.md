# ESP-Voice Assistant

![ESP-Voice Assistant](https://img.shields.io/badge/ESP32-Voice%20Assistant-blue.svg)

## 📌 Overview
ESP-Voice Assistant is a lightweight voice-controlled assistant built using an ESP32 microcontroller. It enables voice command execution for IoT devices, smart home automation, and other interactive applications. This project leverages speech recognition, MQTT communication, and AI-based processing for an enhanced user experience.

## 🚀 Features
- **Speech Recognition**: Processes voice commands efficiently.
- **ESP32-Based**: Runs on a low-cost, energy-efficient ESP32.
- **IoT Integration**: Supports MQTT and HTTP communication.
- **Custom Wake Word**: Allows personalized activation phrases.
- **Multi-Device Control**: Connects and controls various IoT devices.
- **Open-Source & Extensible**: Modify and extend functionalities as needed.

## 🏗️ Project Structure
```
ESP-voice-assistant/
│── firmware/               # ESP32 Firmware Code
│── hardware/               # Circuit diagrams & schematics
│── models/                 # Speech recognition models
│── docs/                   # Documentation and guides
│── scripts/                # Python utilities for testing
│── LICENSE                 # License information
│── README.md               # Project documentation
```

## 🔧 Hardware Requirements
- **ESP32 Development Board**
- **Microphone Module  INMP441
- **Speaker Module** (for audio feedback)
- **Power Supply (5V, 2A)**
- **IoT Devices (Optional for automation setup)**

## 📜 Software Requirements
- **Arduino IDE / ESP-IDF** (for flashing firmware)
- **Python 3.x** (for testing and utilities)
- **MQTT Broker** (Mosquitto, HiveMQ, etc.)
- **Wi-Fi Connectivity** (for cloud interactions)

## 📖 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/adityagirishh/ESP-voice-assistant.git
   cd ESP-voice-assistant
   ```
2. **Install Dependencies**
   - **For Arduino IDE**:
     - Install ESP32 Board Support Package.
     - Install required libraries: `PubSubClient`, `WiFi`, `ArduinoJson`.
   - **For ESP-IDF**:
     - Set up ESP-IDF environment.
     - Compile and flash firmware using `idf.py`.
3. **Connect to Wi-Fi & MQTT Broker**
   - Update `config.h` with Wi-Fi credentials.
   - Set up MQTT broker details.
4. **Flash the Firmware**
   ```bash
   idf.py build flash monitor
   ```
5. **Test the Setup**
   - Use an MQTT client to send/receive messages.
   - Use voice commands to control connected devices.

## 🔌 Usage
- Say the wake word to activate.
- Speak commands like:
  - *"Turn on the lights"*
  - *"Increase the fan speed"*
  - *"Play music"*
- The ESP32 processes the command and executes the required action.

## 📊 Architecture Diagram
```text
[Microphone] --> [ESP32 (Speech Processing)] --> [Wi-Fi/MQTT] --> [IoT Devices]
```

## 🚀 Future Improvements
- Implement offline voice recognition
- Add AI-based natural language processing
- Support additional IoT communication protocols (Zigbee, Bluetooth)
- Enable cloud-based voice command execution

## 📝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments
- Open-source contributors
- ESP-IDF and Arduino communities
- Speech recognition libraries & tools

---
📧 For queries, contact: aditya.girish17@gmail.com


