import numpy as np
from typing import List
import cv2


def calculate_motion(
    matches: List[cv2.DMatch], kp1: List[cv2.KeyPoint], kp2: List[cv2.KeyPoint]
) -> float:
    """
    calculate motion from feature matching results.
    """
    motion = []
    for match in matches:
        pt1 = np.array(kp1[match.queryIdx].pt)
        pt2 = np.array(kp2[match.trainIdx].pt)
        motion.append(np.linalg.norm(pt1 - pt2))
    return np.mean(motion) if motion else 0.0
