from image_recognition import load_model, prepare_image, predict
def test_simple_image_recognition():
    model = load_model()
    processed_image = prepare_image('/Users/liukaihsin/dockerProj/4-containerized-app-exercise-team111/machine-learning-client/tests/test1.jpg')
    predictions = predict(model, processed_image)
    recognized_labels = [label for _, label, _ in predictions]
    
    assert any('cat' in label for label in recognized_labels), f"None of the labels contain 'cat': {recognized_labels}"

