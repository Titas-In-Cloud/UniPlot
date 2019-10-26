import matplotlib.pyplot as plt

def plot_bar_show(d, fontsize = 14):
    r = range(0, len(d))
    plt.figure()
    plt.bar(r, d.values())
    plt.xticks(r, d.keys())
    plt.title('Average Protein Length of Organisms', fontsize = fontsize)
    plt.tight_layout()
    plt.show()

def plot_pie_show(d, fontsize = 14):
    plt.figure()
    sizes = d.values()

    def real_value(val):
        x = int(val/100*sum(sizes))
        return x

    plt.pie(sizes, labels = d.keys(), startangle = 110, autopct = real_value)
    plt.axis('equal')
    plt.title('Average Protein Length of Organisms', fontsize = fontsize)
    plt.tight_layout()
    plt.show()
