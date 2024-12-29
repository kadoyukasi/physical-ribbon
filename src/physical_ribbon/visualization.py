import matplotlib.pyplot as plt
from typing import List


def plot_motion(motion_starlit: List[float], motion_expo: List[float]) -> None:
    """
    plot the frame-to-frame motion changes.
    """
    plt.figure(figsize=(12, 8))
    plt.plot(motion_starlit, label="Starlit", marker="o", linestyle="-", color="b")
    plt.plot(motion_expo, label="Expo", marker="s", linestyle="--", color="r")
    plt.title("Frame-to-Frame Motion Changes: Starlit vs Expo")
    plt.xlabel("Frame Index")
    plt.ylabel("Motion Change (average displacement)")
    plt.legend()
    plt.grid(True)
    plt.show()
