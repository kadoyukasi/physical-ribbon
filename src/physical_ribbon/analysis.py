import os
import cv2
from typing import List
from physical_ribbon.features import detect_features, match_features
from physical_ribbon.motion import calculate_motion


def analyze_motion(image_dir: str) -> List[float]:
    """
    analyze motion between frames in the given directory of images.
    """
    image_files = sorted(
        [
            os.path.join(image_dir, f)
            for f in os.listdir(image_dir)
            if f.endswith((".png", ".jpg", ".jpeg"))
        ]
    )
    motion_changes = []
    prev_keypoints, prev_descriptors = None, None

    for image_file in image_files:
        image = cv2.imread(image_file)
        if image is None:
            print(f"Failed to load {image_file}")
            continue

        keypoints, descriptors = detect_features(image)
        if prev_keypoints is not None and prev_descriptors is not None:
            matches = match_features(prev_descriptors, descriptors)
            motion_change = calculate_motion(matches, prev_keypoints, keypoints)
            motion_changes.append(motion_change)
        else:
            motion_changes.append(0.0)

        prev_keypoints, prev_descriptors = keypoints, descriptors

    return motion_changes
