import matplotlib.pyplot as plt


class Plot:
    pass


def plot(t, S, I, R):
    f, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
    ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
    ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
    ax.set_xlabel('Time (days)')
    plt.show()
