import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def add_bezier_bumps(points, radius=None, bezier_points=30,
                     side='left', eps=0.0, bump_scale=1.0):
    """
    Insert medium Bezier bumps at duplicate points.

    bump_scale = 1.0 gives a medium bump.
    Reduce for smaller bumps, increase for taller bumps.
    """
    pts = np.asarray(points, dtype=float)
    new_pts = []
    i = 0

    # Auto radius if not provided
    if radius is None:
        span = np.linalg.norm(pts.max(axis=0) - pts.min(axis=0))
        radius = 0.02 * span

    while i < len(pts):
        new_pts.append(pts[i].copy())

        # detect consecutive duplicates
        j = i + 1
        while j < len(pts) and np.linalg.norm(pts[j] - pts[i]) <= eps:
            j += 1

        if j > i + 1:
            P = pts[i]

            # compute tangent
            if i == 0:
                d = pts[j] - P
                if np.allclose(d, 0): d = np.array([1.0, 0.0])
                prev = P - d
            else:
                prev = pts[i - 1]

            if j >= len(pts):
                d = P - prev
                if np.allclose(d, 0): d = np.array([1.0, 0.0])
                nxt = P + d
            else:
                nxt = pts[j]

            # tangent and normal
            t = nxt - prev
            if np.linalg.norm(t) == 0:
                t = np.array([1.0, 0.0])
            t = t / np.linalg.norm(t)

            n = np.array([-t[1], t[0]])
            if side == 'right':
                n = -n

            # Define start, control, end
            S = P - radius * t
            E = P + radius * t
            C = P + (radius * bump_scale) * n   # bump height

            # replace last point with S
            new_pts[-1] = S

            # quadratic Bezier parameterization
            t_vals = np.linspace(0, 1, bezier_points)
            for tt in t_vals:
                B = (1-tt)**2 * S + 2*(1-tt)*tt * C + tt**2 * E
                new_pts.append(B.tolist())

            i = j
            continue

        i += 1

    return np.asarray(new_pts)

# --- Demo using your example ---
points = np.array([
    [1,1], [2,3], [3,1], [3,1], [1,1]
])

pts_bezier = add_bezier_bumps(
    points,
    radius=0.2,
    bezier_points=40,
    side='left',
    bump_scale=1.0   # medium bump
)

plt.plot(pts_bezier[:,0], pts_bezier[:,1], linewidth=3)
plt.gca().set_aspect('equal')
plt.grid(True, alpha=0.3)
plt.show()

plt.savefig('line_with_bumps.jpg', dpi=300)
plt.show()

