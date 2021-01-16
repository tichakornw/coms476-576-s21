from matplotlib import colors
from matplotlib.ticker import AutoMinorLocator
import numpy as np


def draw(ax, grid, path, visited):
    """Plot the grid, path and visited cells on axis ax

    @type ax: axes.Axes, created, e.g., fig, ax = plt.subplots()
    @type grid: 2-dimensional list such that grid[j][i] indicates whether cell (i,j) is occupied
    @type path: a list of tuples specifying the sequence of cells visited along the path
    @type visited: a list of a tuple specifying the cells that have been visited
    """
    draw_grid(ax, grid)
    draw_path(ax, path)
    mark_cell(ax, visited)


def draw_grid(ax, grid, grid_on=True, tick_step=[1, 1]):
    """Draw the grid on the axis ax"""
    data = np.asarray(grid)
    N = np.shape(data)[0] - 1
    M = np.shape(data)[1] - 1

    # Define grid colors
    cmap = colors.ListedColormap(["white", "slategrey"])
    bounds = [-0.5, 0.5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Draw grid
    ax.imshow(data, cmap=cmap, norm=norm, origin="lower")

    # Draw grid lines and labels
    if grid_on:
        ax.grid(which="minor", axis="both", linestyle="-", color="k", linewidth=2)

    ax.set_xticks(np.arange(0, M + 1, tick_step[0]))
    ax.set_yticks(np.arange(0, N + 1, tick_step[1]))

    minor_locator = AutoMinorLocator(2)
    ax.tick_params(which="minor", width=0)
    ax.tick_params(which="minor", length=0)
    ax.xaxis.set_minor_locator(minor_locator)
    ax.yaxis.set_minor_locator(minor_locator)

    ax.set_xlim(-0.5, M + 0.5)
    ax.set_ylim(-0.5, N + 0.5)


def draw_path(ax, path):
    """Draw the path on the axis ax"""
    if not path:
        return

    data = np.asarray(path)
    ax.plot(data[:, 0], data[:, 1], "r-", linewidth=5)


def mark_cell(ax, cells):
    """Mark cells on the axis ax"""
    if not cells:
        return

    data = np.asarray(cells)
    ax.plot(data[:, 0], data[:, 1], "bx", markersize=5)
