from flask import Flask, render_template, Response
import cv2
import imagezmq

app = Flask(__name__)


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


def gen_video_feed():
    while True:
        img_hub = app.config['IMAGE_HUB']
        text, image = img_hub.recv_image()

        # Encode image as jpeg
        image = cv2.imencode(
                '.jpg', image,
                [int(cv2.IMWRITE_JPEG_QUALITY), 75])[1].tobytes()
        yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')


@app.route('/video')
def video():
    return Response(
            gen_video_feed(),
            mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    print('[INFO] Starting server at http://localhost:5000')
    app.config['IMAGE_HUB'] = imagezmq.ImageHub(
            open_port='tcp://127.0.0.1:5001', REQ_REP=False)
    app.run(host='0.0.0.0', port=5000)
