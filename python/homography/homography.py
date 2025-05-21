import numpy as np
import cv2 as cv


# Internal camera matrix
K =  np.array([[435.13547291,   0.          , 323.25520758],
               [0.          ,   436.57859545, 162.07589769],
               [0.          ,  0.           , 1.          ]])

# Distortion coefficients
D =  [[-0.37214566, 0.15730994, -0.00202448, -0.00163149, -.04350173]]


