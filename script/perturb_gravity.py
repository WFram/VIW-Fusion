import numpy as np
from scipy.spatial.transform import Rotation as R


r_x = R.from_euler('x', 2, degrees=True)
print(r_x.as_matrix())
# r_z = R.from_euler('z', 1, degrees=True)
# r = r_x * r_z
r = r_x
# R = np.array([[0.03758758, 0.0190846, 0.99911108],
#               [-0.99906439, -0.02068303, 0.0379809],
#               [0.02138949, -0.99960392, 0.01828932]])
g = np.array([[0.0],
              [-9.805],
              [0.0]])
print(np.dot(R, g))
