import numpy as np
import cv2

def band_pass_filter(image_path, low_cutoff=10, high_cutoff=30):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Convert the image to grayscale if it's a color image
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform 2D Fourier Transform
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Get image shape
    rows, cols = image.shape

    # Create a mask for the bandpass filter
    mask = np.ones((rows, cols), np.uint8)
    center = (rows // 2, cols // 2)
    x, y = np.ogrid[:rows, :cols]
    mask[(x - center[0])**2 + (y - center[1])**2 < low_cutoff**2] = 0
    mask[(x - center[0])**2 + (y - center[1])**2 > high_cutoff**2] = 0

    # Apply the mask to the Fourier Transform
    f_transform_shifted_filtered = f_transform_shifted * mask

    # Inverse Fourier Transform
    img_filtered = np.fft.ifft2(np.fft.ifftshift(f_transform_shifted_filtered)).real

    return img_filtered
