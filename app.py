import os
import cv2
import yaml
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from ultralytics import YOLO

# Flask app configuration
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

# Load YOLO model
model = YOLO('carrotsAi.pt')  # Replace with your trained model's path

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Read class names from your data.yaml
with open('data.yaml', 'r') as file:  # Replace with the correct path to your data.yaml
    data = yaml.safe_load(file)
names = data['names']

# Define vehicle-related classes
vehicle_classes = [
    'bus', 'cargo_van', 'coach_bus', 'delivery_van', 'double_deck', 'fuel_truck', 
    'microbus', 'minibus', 'motorcycle', 'pickup', 'private_car', 'rickshaw', 
    'truck', 'van'
]
vehicle_ids = [idx for idx, name in enumerate(names) if name in vehicle_classes]

# Main Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('videos')
        filenames = {}
        directions = ['top-left', 'top-right', 'bottom-left', 'bottom-right']

        for file, direction in zip(files, directions):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames[direction] = filename

        if filenames:
            results = analyze_videos(filenames.values())
            return render_template('results.html', results=results, videos=filenames)

    return render_template('index.html', videos={})

# Analyze videos and count vehicles
def analyze_videos(filenames):
    directions = ["North", "South", "East", "West"]
    vehicle_counts = [0, 0, 0, 0]
    max_frames = 100  # Limit the number of frames to process per video

    for idx, filename in enumerate(filenames):
        cap = cv2.VideoCapture(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        frame_count = 0

        while frame_count < max_frames:
            ret, frame = cap.read()
            if not ret:
                break

            # Run YOLO detection
            results = model.predict(frame, imgsz=640)

            # Count vehicles using class IDs
            vehicle_count = sum(1 for obj in results[0].boxes.cls if int(obj) in vehicle_ids)
            vehicle_counts[idx] += vehicle_count
            frame_count += 1

        cap.release()

    # Compute green light timings
    total_vehicles = sum(vehicle_counts)
    if total_vehicles > 0:
        timings = [max(10, int((count / total_vehicles) * 60)) for count in vehicle_counts]
        return dict(zip(directions, timings))
    return {}

# Serve uploaded video files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
