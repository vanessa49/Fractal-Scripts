import numpy as np
import matplotlib.pyplot as plt

# Define the properties of the image
width, height = 3000, 3000  # Adjust these values for a higher or lower resolution image
max_iter = 1000  # Increase this for more detail, decrease for faster computation

# Define the properties of the Julia set
c = -0.8 + 0.156j  # Adjust this value to generate different Julia sets
xmin, xmax, ymin, ymax = -0.1, 0, -0.5, 0.5  # Adjust these values to zoom in or out x和y轴与直角坐标系相反

# Create an empty image
image = np.zeros((width, height))

# Calculate the Julia set
for i, real in enumerate(np.linspace(xmin, xmax, width)):
    for j, imag in enumerate(np.linspace(ymin, ymax, height)):
        z = complex(real, imag)
        iteration = 0
        while abs(z) < 1000 and iteration < max_iter:
            z = z*z + c
            iteration += 1
        image[i, j] = iteration

# Display the image
plt.imshow(image, cmap='twilight_shifted', origin='lower', extent=(xmin, xmax, ymin, ymax))
plt.title('Julia Set')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
# Save the image to disk before displaying it
plt.savefig('julia.png', dpi=5000)

# Then display the image
plt.show()
