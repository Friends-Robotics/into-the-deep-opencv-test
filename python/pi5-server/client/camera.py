import cv2
import numpy as np
import requests


pi_ip = "192.168.1.60"
url = f"http://{pi_ip}:5000")


def get_remote_image(url=f"{url}/image"):
    response = requests.get(url)
    if response.status_code == 200:
        img_array = np.frombuffer(response.content, dtype=np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return image
    else:
        return None


def set_servo_position():
    curl -X POST http://<PI_IP>:5000/servo -H "Content-Type: application/json" \
    -d '{"channel": 0, "angle": 90}'

