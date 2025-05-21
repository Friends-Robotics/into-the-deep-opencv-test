import cv2

def get_frame():
    cap = cv2.VideoCapture(0)  # You can change device index if needed
    if not cap.isOpened():
        return None
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return None
    _, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes()

