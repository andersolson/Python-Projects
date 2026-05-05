import numpy as np
import matplotlib.pyplot as plt

def add_bumps(points, radius=None, arc_points=25, side='left', eps=0.0):
    """
    Insert a half-circle 'bump' whenever consecutive duplicate points occur.

    Parameters
    ----------
    points : (N, 2) array-like
        Sequence of [x, y] points connected in order.
    radius : float or None
        Radius of the half-circle in data units. If None, a dynamic radius
        (2% of the data extent) is used.
    arc_points : int
        Number of points used to draw each semicircle (higher = smoother).
    side : {'left', 'right'}
        Which side of the line (relative to direction of travel) to draw the bump.
    eps : float
        Tolerance for treating points as duplicates (0 = exact match).
    """
    pts = np.asarray(points, dtype=float)
    new_pts = []
    i = 0

    # Choose a default radius if none was provided (scales with data extent)
    if radius is None:
        if len(pts) < 2:
            radius = 1.0
        else:
            min_xy = pts.min(axis=0)
            max_xy = pts.max(axis=0)
            radius = 0.02 * np.linalg.norm(max_xy - min_xy)  # 2% of diagonal

    while i < len(pts):
        new_pts.append(pts[i].copy())

        # Look ahead for a run of consecutive duplicates of pts[i]
        j = i + 1
        dup_count = 0
        while j < len(pts) and np.linalg.norm(pts[j] - pts[i]) <= eps:
            dup_count += 1
            j += 1

        if dup_count > 0:
            P = pts[i]

            # prev distinct point (if none, synthesize using the forward direction)
            prev_idx = i - 1
            next_idx = j
            if prev_idx < 0 and next_idx >= len(pts):
                # all points identical; nothing meaningful to draw
                i = j
                continue

            if prev_idx < 0:
                # start-of-path duplicate: use forward direction to synthesize prev
                t_forward = pts[next_idx] - P
                if np.linalg.norm(t_forward) == 0:
                    t_forward = np.array([1.0, 0.0])
                prev = P - t_forward
            else:
                prev = pts[prev_idx]

            if next_idx >= len(pts):
                # end-of-path duplicate: use backward direction to synthesize next
                t_backward = P - prev
                if np.linalg.norm(t_backward) == 0:
                    t_backward = np.array([1.0, 0.0])
                next_ = P + t_backward
            else:
                next_ = pts[next_idx]

            # Tangent (direction of travel) and a perpendicular normal
            t = next_ - prev
            norm_t = np.linalg.norm(t)
            if norm_t == 0:
                t = np.array([1.0, 0.0])
                norm_t = 1.0
            t = t / norm_t
            n = np.array([-t[1], t[0]])
            if side == 'right':
                n = -n

            # Start/end of the bump along the tangent around P
            s = P - radius * t
            e = P + radius * t

            # Replace the last appended P with s to avoid a zero-length P->P segment
            new_pts[-1] = s

            # Semicircle from s to e, centered at P, bulging along +n
            theta = np.linspace(0, np.pi, arc_points)
            # Vector on the circle: cos(theta)*(-t) + sin(theta)*n
            v = (-t[np.newaxis, :]) * np.cos(theta) + (n[np.newaxis, :]) * np.sin(theta)
            arc = P + radius * v
            new_pts.extend(arc.tolist())

            # Skip the entire duplicate run and continue
            i = j
            continue

        i += 1

    return np.asarray(new_pts)


# --- Demo using your example ---
points = np.array([[-1, 1], [2, 1], [3, 1], [3, 1], [5, 1]], dtype=float)
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