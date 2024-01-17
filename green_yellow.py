import matplotlib.pyplot as plt
import numpy as np

def interpolate_color(start_color, end_color, num_steps):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    r_step = (end_r - start_r) / num_steps
    g_step = (end_g - start_g) / num_steps
    b_step = (end_b - start_b) / num_steps

    colors = [
        (
            int(start_r + i * r_step),
            int(start_g + i * g_step),
            int(start_b + i * b_step)
        )
        for i in range(num_steps + 1)
    ]

    return colors

def plot_color_transition(colors):
    num_steps = len(colors)
    x = np.arange(0, num_steps)

    fig, ax = plt.subplots(figsize=(8, 1))
    ax.imshow([colors], aspect='auto', extent=(0, num_steps, 0, 1))

    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

if __name__ == "__main__":
    start_color = (136, 181, 3)
    end_color = (255, 212, 18)
    num_steps = 50

    colors = interpolate_color(start_color, end_color, num_steps)
    plot_color_transition(colors)
