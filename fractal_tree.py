import numpy as np
import matplotlib.pyplot as plt

def draw_tree(ax, x, y, angle, depth):

    if depth > 0:
        dx = np.cos(np.radians(angle))
        dy = np.sin(np.radians(angle))
        ax.plot([x, x + dx], [y, y + dy], color="k", linewidth=depth, zorder=1)
        draw_tree(ax, x + dx, y + dy, angle + 30, depth - 1)
        draw_tree(ax, x + dx, y + dy, angle - 30, depth - 1)
        draw_tree(ax, x + dx, y + dy, angle, depth - 1)


fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
draw_tree(ax, 0.5, 0, 90, 6)
plt.axis('off')

# Uncomment the next line to save the image
plt.savefig('fractal_tree30.png', dpi=300)

plt.show()
