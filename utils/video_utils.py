import cv2
import os

# Suppress OpenCV internal warnings
os.environ["OPENCV_LOG_LEVEL"] = "OFF"
try:
    cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_SILENT)
except AttributeError:
    pass

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_video_frames, output_video_path, fps=24):
    """Save a list of frames to a video file.

    Ensures the output directory exists and validates input before opening VideoWriter.
    Raises a clear error if frames list is empty or if VideoWriter fails to open.
    """
    if not output_video_frames:
        raise ValueError("No frames to save into video.")

    out_dir = os.path.dirname(output_video_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    height, width = output_video_frames[0].shape[:2]

    # Choose candidate fourcc codes based on file extension
    ext = os.path.splitext(output_video_path)[1].lower()
    if ext == '.mp4':
        candidates = ['mp4v', 'H264', 'X264']
    elif ext == '.avi':
        candidates = ['MJPG', 'XVID', 'DIVX']
    else:
        candidates = ['MJPG', 'XVID', 'mp4v']

    out = None
    tried = []
    for code in candidates:
        tried.append(code)
        fourcc = cv2.VideoWriter_fourcc(*code)
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
        if out.isOpened():
            break
        else:
            out.release()
            out = None

    if out is None or not out.isOpened():
        # Fallback: write frames as numbered PNGs if VideoWriter cannot open
        frames_dir = os.path.join(out_dir or '.', 'frames')
        os.makedirs(frames_dir, exist_ok=True)
        for i, frame in enumerate(output_video_frames):
            cv2.imwrite(os.path.join(frames_dir, f'frame_{i:06d}.png'), frame)
        print(f"Warning: VideoWriter failed; saved {len(output_video_frames)} frames to {frames_dir}")
        return

    for frame in output_video_frames:
        out.write(frame)
    out.release()