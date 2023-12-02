import cv2

def capture_image_from_camera():
    # Open the first camera connected to the device(you phone probabally )
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return None

    # Capture a single frame
    ret, frame = cap.read()
    cap.release()  # release the camera

    if ret:
        return frame
    else:
        print("Error: Could not capture an image")
        return None
