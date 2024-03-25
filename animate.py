import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == "__main__":
    from sys import argv
    from .read_data import InputData

    inpd = InputData(argv[1:], False)
    print(len(inpd.filenames), len(argv))
    x, y = np.array(inpd.__next__()).transpose()
    fig, ax = plt.subplots()
    ax.scatter(x, y, color="red")
    (line,) = ax.plot(x, y)

    def update(num, inpd, line):
        print(f"num={num}")
        x, some, y = np.array(inpd.__next__()).transpose()
        line.set_data(x, y)
        return (line,)

    ani = animation.FuncAnimation(
        fig, update, len(argv) - 4, interval=40, fargs=[inpd, line], blit=True
    )
    ani.save("animation_drawing.mp4", writer="ffmpeg", fps=25)
