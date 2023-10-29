from matplotlib import pyplot as plt

def barChart(dictionary):
    labels = [key for key in dictionary.keys()]
    values = [value for value in dictionary.values()]
    ax = plt.subplot()
    ax.bar(labels, values)
    plt.show()

def pieChart(dictionary):
    labels = [key for key in dictionary.keys()]
    values = [value for value in dictionary.values()]
    ax = plt.subplot()
    ax.pie(values, labels=labels)
    plt.show()

    
    print(labels)


