document.addEventListener('DOMContentLoaded', function () {
    const webcamElement = document.getElementById('webcam');
    const captureButton = document.getElementById('capture');
    const resultsElement = document.getElementById('results');

    // Initialize the webcam
    navigator.mediaDevices.getUserMedia({video: true})
        .then(stream => webcamElement.srcObject = stream)
        .catch(err => console.error("error accessing webcam", err));

    captureButton.addEventListener('click', function () {
        captureImage(webcamElement)
            .then(blob => sendImageToServer(blob))
            .then(displayResults)
            .catch(err => console.error("error processing image", err));
    });

    function captureImage(videoElement) {
        return new Promise((resolve, reject) => {
            const canvas = document.createElement('canvas');
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
            canvas.toBlob(blob => resolve(blob), 'image/png');
        });
    }

    function sendImageToServer(blob) {
        const formData = new FormData();
        formData.append('image', blob, 'capture.png');

        return fetch('/upload', {
            method: 'POST',
            body: formData
        }).then(response => response.json());
    }

function displayResults(data) {
    const resultsElement = document.getElementById("results");

    if (data.error) {
        resultsElement.innerText = data.error;
    } else {
        let resultText = '';

        if (data.all_predictions && data.all_predictions.length > 0) {
            data.all_predictions.reverse().forEach(predictionGroup => {
                predictionGroup.forEach(prediction => {
                    resultText += `Label: ${prediction.label}<br>`;
                    resultText += `Probability: ${(prediction.probability * 100).toFixed(2)}%<br><br>`;
                });
            });
        } else {
            resultText += 'No prediction data available.<br>';
        }

        resultsElement.innerHTML = resultText;
    }
}




});
