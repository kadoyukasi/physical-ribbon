import cv2
import numpy as np
from typing import Tuple, List


def detect_features(image: np.ndarray) -> Tuple[List[cv2.KeyPoint], np.ndarray]:
    """
    ORB feature detector and descriptor extractor.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(gray, None)
    return keypoints, descriptors


def match_features(desc1: np.ndarray, desc2: np.ndarray) -> List[cv2.DMatch]:
    """
    descriptor matcher to match two sets of descriptors.
    """
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desc1, desc2)
    return sorted(matches, key=lambda x: x.distance)
