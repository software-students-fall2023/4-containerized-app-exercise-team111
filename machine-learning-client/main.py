from image_recognition import load_model, predict, prepare_image_from_array
from captureImage import capture_image_from_camera



def capture_and_recognize():
    model = load_model()

    # Capture an image from the camera
    captured_image = capture_image_from_camera()
    if captured_image is not None:
        # Prepare the image for the model
        processed_image = prepare_image_from_array(captured_image)

        # Predict and decode the result
        predictions = predict(model, processed_image)

        # Output the predictions
        for _, label, probability in predictions:
            print(f"{label}: {probability:.2f}")

if __name__ == '__main__':
    capture_and_recognize()