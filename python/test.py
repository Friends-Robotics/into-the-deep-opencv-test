import cv2 as cv
import numpy as np

def main():
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # lower_blue = np.array([100, 100, 80])
    # upper_blue = np.array([140, 255, 255])

    while True:
        success, img = cam.read()

        gray_frame = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        mask1 = cv.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv.inRange(hsv, lower_red2, upper_red2)
        final = mask1 + mask2

        # mask1 = cv.inRange(hsv, lower_blue, upper_blue)
        # final = mask1
        
        contours, hierarchy = cv.findContours(final.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        output = img.copy()
        cv.drawContours(output, contours, -1, (0, 255, 0), 2)

        cv.imshow("Test1", img)
        cv.imshow("Test2", gray_frame)
        cv.imshow("Test3", final)
        cv.imshow("Test4", output)

        key = cv.waitKey(10)

        if key == ord('q'):
            break


if __name__ == "__main__":
    main()
