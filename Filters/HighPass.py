import cv2
import numpy as np
import matplotlib.pyplot as plt
def high_pass_filter(image_path, radius=20):
	f = cv2.imread(image_path, 0)
	#plt.imshow(f)
	# convert from spatial domain to frequency domain using fft
	F = np.fft.fft2(f)

	plt.figure(figsize=(10,10))
	plt.subplot(1, 2, 1)
	plt.imshow(np.log(np.abs(F)))
	
	#  Shift frequencies to center
	Fshift = np.fft.fftshift(F)
	plt.subplot(1, 2, 2)
	plt.imshow(np.log(np.abs(Fshift)))
	plt.show()

	print(Fshift)
	M,N = f.shape
	H = np.zeros((M,N) , dtype = np.float32)

	# Gaussian filter modify at the mask (H)
	for u in range(M):
		for v in range(N):
			D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
			H[u,v] = 1 - np.exp(-D ** 2 / (2 * radius * radius))

	Gshift = Fshift * H
	## make inverse to return spatial domain
	G = np.fft.ifftshift(Gshift)
	g = np.abs(np.fft.ifft2(G))
	

	return g
