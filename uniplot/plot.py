import matplotlib.pyplot as plt

def plot_bar_show(d):
    r = range(0, len(d))
    plt.figure()
    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.tight_layout()
    plt.title('Average Protein Length of Organisms')
    plt.show()

def plot_pie_show(d):
    plt.figure()
    sizes=d.values()

    def real_value(val):
        x = int(val/100*sum(sizes))
        return x

    plt.pie(sizes, labels = d.keys(), startangle = 110, autopct = real_value)
    plt.axis('equal')
    plt.title('Average Protein Length of Organisms')
    plt.show()
