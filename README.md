# AI-Powered Football Analysis System ⚽📊

## 🌟 Overview
This project is an advanced Computer Vision system designed to analyze football matches. Using **YOLOv8** and sophisticated tracking algorithms, the system can track players, referees, and the ball, identify teams based on jersey colors, calculate player speed, and estimate ball possession.

It's a comprehensive tool for coaches and analysts to gain deeper insights into game dynamics.

---

## 🔥 Key Features
- **Object Tracking:** Real-time tracking of players, referees, and the ball using YOLOv8.
- **Team Assignment:** Automatic team classification using K-Means clustering on player jersey colors.
- **Ball Possession:** Intelligent logic to detect which player/team has the ball at any given time.
- **Camera Movement Estimation:** Adjusts object positions by accounting for camera pans and tilts.
- **Perspective Transformation:** Transforms pixels into real-world meters for accurate measurements.
- **Performance Metrics:** Calculates and displays individual player speed and total distance covered.

---

## 🛠️ Tech Stack
- **Languages:** Python
- **Computer Vision:** OpenCV, Ultralytics (YOLOv8)
- **Data Handling:** NumPy, Pandas
- **Visualization:** Supervision (by Roboflow)
- **ML Algorithms:** K-Means Clustering (for color segmentation)

---

## 🚀 Why This Tech Stack?
- **YOLOv8:** Chosen for its state-of-the-art speed and accuracy in object detection.
- **K-Means:** Provides a robust, unsupervised way to group players into teams without pre-labeling.
- **OpenCV:** The backbone for all video processing and annotation tasks.

---

## 📁 Directory Structure
- `trackers/`: Core logic for object tracking and interpolation.
- `team_assigner/`: K-Means based team identification.
- `player_ball_assigner/`: Proximity-based ball possession detection.
- `camera_movement_estimator/`: Optical flow logic for camera adjustment.
- `view_transformer/`: Perspective mapping.
- `speed_and_distance_estimator/`: Calculating physical metrics.
- `utils/`: Video I/O and helper functions.

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Football_Analysis_Project.git
   cd Football_Analysis_Project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the analysis:**
   ```bash
   python main.py
   ```
   *Note: Ensure you have a video file in `input_videos/` and a YOLOv8 model in `models/`.*

---

## 📈 Future Improvements
- [ ] **Player Identification:** Integrating Re-ID to maintain player IDs even after occlusions.
- [ ] **Event Detection:** Automatic detection of goals, fouls, and corners.
- [ ] **Heatmaps:** Generating tactical heatmaps for player movements.
- [ ] **Real-time Web Dashboard:** A Streamlit or Flask interface for interactive analysis.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📝 License
This project is licensed under the MIT License.
