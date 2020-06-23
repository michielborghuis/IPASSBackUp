import matplotlib.pyplot as plt


class Plot:
    pass


def plot(t, y):

    f, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(t, y, 'g', alpha=0.7, linewidth=2, label='iets')
    legend = ax.legend(borderpad=2.0)
    legend.get_frame().set_alpha(0.5)
    plt.show()
