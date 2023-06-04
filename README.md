# Video Streaming from Raspberry Pi to Ubuntu PC using Python

This repository provides a simple Python-based solution for streaming video from a Raspberry Pi to an Ubuntu PC. The video is captured using the Raspberry Pi camera, encoded with H.264, and sent to the Ubuntu PC over a UDP connection. The Ubuntu PC then receives the UDP stream and displays it using OpenCV.

## Requirements

### Hardware

- Raspberry Pi with a camera module
- Ubuntu PC

### Software

- Python 3.6 or later
- [OpenCV](https://opencv.org/) on the Ubuntu PC
- [picamera2](https://pypi.org/project/picamera2/) on the Raspberry Pi
- Network connectivity between Raspberry Pi and Ubuntu PC

## Installation

### On Raspberry Pi

1. Clone the repository

```bash
git clone https://github.com/abcamiletto/raspberry-camera-remote.git
```

2. Navigate to the directory

```bash
cd raspberry-camera-remote
```

3. Install the required Python packages

```bash
pip3 install picamera2
```

### On Ubuntu PC

1. Clone the repository

```bash
git clone git clone https://github.com/abcamiletto/raspberry-camera-remote.git
```

2. Navigate to the directory

```bash
cd raspberry-camera-remote
```

3. Install the required Python packages

```bash
pip3 install opencv-python
```

## Usage

### On Raspberry Pi

Run the script to start streaming video from the Raspberry Pi camera. Replace `<Remote IP>` and `<Port>` with the IP address and port number of your Ubuntu PC:

```bash
python3 send.py --ip <Remote IP> --port <Port> --size 1280x720
```

This will start recording video from the Raspberry Pi's camera and send it as a UDP stream to the specified IP address and port. The video size is set to 1280x720 by default but can be adjusted using the `--size` flag.

Press any key to stop the recording.

### On Ubuntu PC

Run the script to start receiving the video stream. Replace `<Your IP>` and `<Port>` with the IP address and port number that you've previously specified:

```bash
python3 read.py --ip <Your IP> --port <Port>
```

This will start displaying the video stream received from the Raspberry Pi. If the connection is interrupted or no frames are received, the program will retry every second.

Press 'q' on your keyboard to stop the video stream.
