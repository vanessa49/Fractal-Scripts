import numpy as np
import matplotlib.pyplot as plt

def koch_snowflake(order, scale=10):
    def _koch_snowflake_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
x, y = koch_snowflake(order=6)

ax.fill(x, y, fill=False, edgecolor='blue')  # Only display the edge in blue
ax.axis('equal')

# Uncomment the next line to save the image
plt.savefig('koch_snowflake.png', dpi=300)

plt.show()


