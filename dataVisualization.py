from matplotlib import pyplot as plt

def barChart(dictionary, plot_title):
    labels = [key for key in dictionary.keys()]
    values = [value for value in dictionary.values()]
    ax = plt.subplot()
    ax.bar(labels, values)
    plt.title(plot_title)
    plt.show()

def pieChart(dictionary, plot_title):
    labels = [key for key in dictionary.keys()]
    values = [value for value in dictionary.values()]
    ax = plt.subplot()
    ax.pie(values, labels=labels, autopct= "%1.1f%%")
    plt.title(plot_title)
    plt.show()
  