# Why

~~I hate myself~~ To win. So basically... the claw needs to be fast and auto-orienting.

## How

As the Silver Wolves put it...

- Camera with wide FOV
- Colour mask
- Contour
- Min Area Bounding Rectangle
- Angle
- Servo rotation

### Webcam Info

We need a webcam with a wide FOV (Silver Wolves use one with 120 degrees) mounted approximately 20cm above the ground. Ideally, it will parallel the ground and have a constant height (while taking images) to make location-based calculations easier.
<br>
<br>
[Choosing a webcam](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Webcams-for-FTC-VisionPortal)
<br>
<br>
In addition to this, we need to remove the fisheye distortion from the camera to allow for accurate position calculations relative to the camera position. This can be done with external calibration using a laptop and a checkerboard pattern. Ask ChatGPT for more info.

## Setting up the development environment

[Venv](https://docs.python.org/3/library/venv.html) usage. Please make a venv file within the python directory. There is a nested .gitignore file to prevent it being included in the git history. When cloning this repositiory it is recommended to not clone the history due to the large size of the repository. This can be done with:
```git
git clone <url> --depth=1
```
