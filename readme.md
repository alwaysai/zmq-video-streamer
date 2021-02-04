# ZMQ Video Streamer
This repo has two parts: an alwaysAI computer vision app which performs realtime object detection and streams video via (ZeroMQ)[https://zeromq.org/languages/python/] to a Flask server, and the server to display the video stream in a browser.

## Setup
This app requires an alwaysAI account. Head to the [Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account yet. Follow the instructions to install the alwaysAI toolchain on your development machine.

Next, create an empty project to be used with this app. When you clone this repo, you can run `aai app configure` within the repo directory and your new project will appear in the list.

## Usage
### Server
The server is a Flask server that hosts a webpage and an MJPG video stream.

First, create the Python virtual environment with the dependencies. For example, on Linux run these steps:

```
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Now, you should be able to run the app:

```
(venv) $ python app.py
[INFO] Starting server at http://localhost:5000
```

Open the link in a browser on your machine. Next, start the realtime object detection app.


### Realtime Object Detector
Once the alwaysAI toolset is installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & folder path

`$ aai app configure`

To install the app on the target device

`$ aai app install`

The app has the following options:

```
$ aai app start -- --help
usage: app.py [-h] [--camera CAMERA] [--use-streamer]
              [--server-addr SERVER_ADDR]

alwaysAI ZMQ Video Streamer Client

optional arguments:
  -h, --help            show this help message and exit
  --camera CAMERA       The camera index to stream from.
  --use-streamer        Use the embedded streamer instead of connecting to the
                        server.
  --server-addr SERVER_ADDR
                        The IP address or hostname of the server
                        (Default: localhost).
```

To start the app using the defaults:

`$ aai app start`

To capture video from camera index 1:

`$ aai app start -- --camera 1`

To connect to the server at 192.168.3.2:

`$ aai app start -- --server-addr 192.168.3.2`

> Note that tha extra `--` in the above commands is used to indicate that the parameters that follow are to be passed through to the python app, rather than used by the CLI.

#### Example

Run the realtime object detector connecting to `192.168.3.2`:

```
$ aai app start -- --server-addr 192.168.3.2
Loaded model:
alwaysai/mobilenet_ssd

Engine: Engine.DNN
Accelerator: Accelerator.GPU

Labels:
['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

[INFO] Connecting to server http://192.168.3.2:5000...
[INFO] Successfully connected to server.
```
