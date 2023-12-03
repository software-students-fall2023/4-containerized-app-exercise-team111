import numpy as np
import cv2
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from database_manager import DatabaseManager
model = MobileNetV2(weights='imagenet')


def preprocess_image(image_path_):
    img = cv2.imread(image_path_)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    return np.expand_dims(img, axis=0)


def recognize_objects(image_path_1):
    img = preprocess_image(image_path_1)
    preds = model.predict(img)
    return decode_predictions(preds, top=3)[0]


if __name__ == "__main__":
    image_path = '1.png'
    predictions = recognize_objects(image_path)
    for _, label, probability in predictions:
        print(f"{label}: {probability:.2f}")
    inserted_id = DatabaseManager.save_prediction(image_path, predictions)
    print(f"Saved predictions with ID: {inserted_id}")
