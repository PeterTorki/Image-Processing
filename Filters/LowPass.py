import cv2
import numpy as np
from matplotlib import pyplot as plt

def low_pass_filter(image_path, radius=30):

	f = cv2.imread(image_path, 0)
	F = np.fft.fft2(f)
	Fshift = np.fft.fftshift(F)

	M,N = f.shape
	H = np.zeros((M,N) , dtype = np.float32)

	for u in range(M):
		for v in range(N):
			D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
			H[u,v] = np.exp(-D ** 2 / (2 * radius * radius))

	### make Low Pass on Image
	Gshift = Fshift * H
	## make inverse to return spatial domain
	G = np.fft.ifftshift(Gshift)
	g = np.abs(np.fft.ifft2(G))

	return g



