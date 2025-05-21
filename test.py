import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
#import cv2 as cv


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("test")
        self.setGeometry(100, 100, 400, 400)
        self.show()


def main():
    print("Starting test")

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
