import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_filter(file_path):
	img = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
	

	equImg = cv2.equalizeHist(img)

	return equImg

if __name__ == '__main__':
    histogram_filter()