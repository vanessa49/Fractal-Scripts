import numpy as np
import matplotlib.pyplot as plt

def sierpinski(order, scale=10):
    def _sierpinski_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            p1 = _sierpinski_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 3, dtype=np.complex128)
            new_points[::3] = p1
            new_points[1::3] = p1 + dp / 2
            new_points[2::3] = p1 + dp / 2 * np.exp(np.deg2rad(60) * 1j)
            return new_points

    points = _sierpinski_complex(order)
    x, y = points.real, points.imag
    return x, y

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
x, y = sierpinski(order=5)
ax.fill(x, y, fill=False, edgecolor='blue')  # Only display the edge in blue
ax.axis('equal')

# Uncomment the next line to save the image
plt.savefig('sierpinski.png', dpi=300)

plt.show()
