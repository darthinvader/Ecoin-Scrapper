import matplotlib.pyplot as plt

# ScatterPlot
# Arguments:
# close1: the array of closing prices for the first coin
# close2: the array of closing price for the second coin
# xlabel: the label used in the x axis for the plot
# ylabel: the label used in the y axis for the plot
# title: the title of the plot
# color: the color of the dots on the plot
# marker:the marker used for the dots on the plot (e.g 'o' is for circle) same as matplotlib
# size: the size of the marker
# The function shows a scatter plot of the data given


def scatterPlot(close1, close2, xlabel="", ylabel="", title="Correlation Plot", color='k', marker='o', size=40):
    plt.scatter(close1, close2, label="CorrPlot", color=color, marker=marker, s=size)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
