import numpy as np
import matplotlib.pyplot as plt

# Define the properties of the image
width, height = 4000, 4000  # Adjust these values for a higher or lower resolution image
max_iter = 300  # Increase this for more detail, decrease for faster computation

# Define the properties of the Mandelbrot set
xmin, xmax, ymin, ymax = -0.2196, -0.2186, -0.70, -0.699  # Adjust these values to zoom in or out

# Create an empty image
image = np.zeros((width, height))

# Calculate the Mandelbrot set
for i, real in enumerate(np.linspace(xmin, xmax, width)):
    for j, imag in enumerate(np.linspace(ymin, ymax, height)):
        c = complex(real, imag)
        z = 0
        iteration = 0
        while abs(z) < 1000 and iteration < max_iter:
            z = z*z + c
            iteration += 1
        image[i, j] = iteration

# Display the image
plt.imshow(image, cmap='twilight_shifted', origin='lower', extent=(xmin, xmax, ymin, ymax))
plt.title('Mandelbrot Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
# Uncomment the next line to save the image
plt.savefig('mandelbrot3.png', dpi=5000)
plt.show()


