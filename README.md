# Real-Time Video Streaming

A Python-based application for secure, real-time video streaming between a server and client using sockets and SSL encryption.

## Features

- **Secure SSL/TLS transmission** for all video data
- **Real-time webcam streaming** using OpenCV
- **Frame serialization and custom protocol** for efficient transmission
- **Low latency** video display on client side

## Technologies

- Python 3.x
- OpenCV (`cv2`)
- Socket
- SSL
- Pickle
- Struct

## Setup Instructions

### Prerequisites

- Python 3.x installed
- OpenCV (`cv2`), install with `pip install opencv-python`
- SSL certificates: `server_cert.pem` and `server_key.pem` (self-signed or CA issued)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/suree20/real-time-video-streaming.git
    cd real-time-video-streaming
    ```

2. **Install dependencies:**
    ```bash
    pip install opencv-python imutils
    ```

3. **Generate or provide SSL certificates:**
    - Place `server_cert.pem` and `server_key.pem` in the project directory.

### Running the Server

1. **Start the server:**
    ```bash
    python server.py
    ```
    - By default, the server uses `host_ip = '192.168.1.9'` and `port = 5005`. Change as needed.

### Running the Client

1. **Start the client:**
    ```bash
    python client.py
    ```
    - Make sure `host_ip` and `port` match the server settings.

## How It Works

- The server captures video frames using OpenCV.
- Each frame is serialized and sent over a secure socket.
- The client receives the frames, deserializes them, and displays the video in real-time.

## File Structure

- `server.py` : Main server script for capturing and sending video frames securely.
- `client.py` : Main client script for receiving and displaying video frames.

## Troubleshooting

- If you experience connection issues, ensure both server and client are on the same network and the IP/port are correctly set.
- SSL certificate errors can be resolved by regenerating certificates or setting `CERT_NONE` (not recommended for production).
