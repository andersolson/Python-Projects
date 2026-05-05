import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

import numpy as np

def add_bumps(points, radius=None, arc_points=25, side='left', eps=0.0):
    pts = np.asarray(points, dtype=float)
    new_pts = []
    i = 0

    # Compute default radius from data extent
    if radius is None:
        if len(pts) < 2:
            radius = 1.0
        else:
            span = np.linalg.norm(pts.max(axis=0) - pts.min(axis=0))
            radius = 0.02 * span  # 2% of data diagonal

    while i < len(pts):
        new_pts.append(pts[i].copy())

        # detect consecutive duplicates
        j = i + 1
        while j < len(pts) and np.linalg.norm(pts[j] - pts[i]) <= eps:
            j += 1

        if j > i + 1:
            P = pts[i]

            # previous distinct
            if i == 0:
                # synthesize previous using forward direction
                d = pts[j] - P
                if np.allclose(d, 0):
                    d = np.array([1.0, 0.0])
                prev = P - d
            else:
                prev = pts[i-1]

            # next distinct
            if j >= len(pts):
                d = P - prev
                if np.allclose(d, 0):
                    d = np.array([1.0, 0.0])
                nextp = P + d
            else:
                nextp = pts[j]

            # tangent and normal
            t = nextp - prev
            if np.linalg.norm(t) == 0:
                t = np.array([1.0, 0.0])
            t = t / np.linalg.norm(t)
            n = np.array([-t[1], t[0]])
            if side == 'right':
                n = -n

            # start and end of bump
            s = P - radius * t
            e = P + radius * t

            # replace previous appended P with s
            new_pts[-1] = s

            # arc: ensure column vectors for broadcasting
            theta = np.linspace(0, np.pi, arc_points)
            cos_t = np.cos(theta).reshape(-1, 1)
            sin_t = np.sin(theta).reshape(-1, 1)

            v = cos_t * (-t) + sin_t * n
            arc = P + radius * v

            new_pts.extend(arc.tolist())

            i = j
            continue

        i += 1

    return np.asarray(new_pts)

# --- Demo using your example ---
points = np.array([[-1, 1], [2, 5],[2,5], [3, 1], [3, 1], [-2, -3]], dtype=float)
pts_with_bumps = add_bumps(points, radius=0.2, arc_points=30, side='left')

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(points[:, 0], points[:, 1], color='lightgray', linewidth=2, label='original')
ax.plot(pts_with_bumps[:, 0], pts_with_bumps[:, 1], color='steelblue', linewidth=3, label='with bump')

# Keep circles circular in the rendered image
ax.set_aspect('equal', adjustable='datalim')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.25)

plt.savefig('line_with_bumps.jpg', dpi=300)
plt.show()

