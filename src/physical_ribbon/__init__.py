from physical_ribbon.analysis import analyze_motion
from physical_ribbon.visualization import plot_motion


def main() -> int:
    starlit_dir = "resources/starlit"
    expo_dir = "resources/expo"

    motion_starlit = analyze_motion(starlit_dir)
    motion_expo = analyze_motion(expo_dir)

    plot_motion(motion_starlit, motion_expo)
    return 0
