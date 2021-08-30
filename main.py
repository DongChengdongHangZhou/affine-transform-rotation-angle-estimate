import cv2
import numpy as np 


src = np.array( [[164, 215], [128, 8], [480, 72]] )
dst = np.array( [(175, 237), (146, 44), (486, 99)] ).reshape(-1,2)


m = cv2.estimateAffine2D(dst,src)
print(m)
# m = cv2.estimateRigidTransform(_prev_pts, _curr_pts, fullAffine=False)


tr = np.array([[ 1.03016009,  3.17376025e-02, -2.37998282e+01],
       [ 1.51034752e-02,  1.07026943e+00, -4.12969621e+01]])
dst2 = np.matmul(src,tr)
print(dst2)