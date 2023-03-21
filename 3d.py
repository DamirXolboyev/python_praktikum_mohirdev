import numpy as np
from scipy import spatial
from stl import mesh
from myplot import plot_mesh
vertices = np.array(
[
[-3, -3, 0],
[+3, -3, 0],
[+3, +3, 0],
[-3, +3, 0],
[+0, +0, +3]
]
)
hull = spatial.ConvexHull(vertices)
faces = hull.simplices
