# Traffic Management with AI

## Overview
This project aims to optimize traffic flow and reduce congestion using AI to analyze real-time traffic videos. The system dynamically adjusts traffic signal timings based on the detected number of vehicles in each direction.

## Features
- Upload traffic videos for different directions (North, South, East, West)
- Real-time vehicle detection using YOLO
- Dynamic calculation of green light duration for each direction
- Display of results with processed videos

![image](https://github.com/user-attachments/assets/55748ac5-c729-4304-8a65-62080a293b1a)
![image](https://github.com/user-attachments/assets/aba164b9-756b-4d3e-9e98-37d12cc82c59)

## Technology Stack
- Flask
- YOLO (You Only Look Once)
- OpenCV
- Python 3.11

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Dev-A-17/Traffic_Management_with_AI.git
    cd Traffic_Management_with_AI
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the YOLO model files**:   
   Place `carrotsAi.pt` and `yolov8s.pt` in the root directory of the project. 

## Special Note
This project requires **Python 3.11** because YOLO is part of Ultralytics, which uses PyTorch. PyTorch has optimal support and compatibility with Python 3.11, ensuring that all functionalities of the model are fully utilized.

## Usage
1. **Run the Flask application**:
    ```bash
    py -3.11 app.py
    ```

2. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:5000/`.

3. **Upload Traffic Videos**:
    - Upload videos for each direction (North, South, East, West).
    - The system will process the videos, detect vehicles, and calculate optimized green light durations.

4. **View Results**:
    - The results page will display the green light durations and the processed videos.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or inquiries, please contact **_Dev Akshat_** at devakshatsrivastava@gmail.com or dm687@snu.edu.in.
