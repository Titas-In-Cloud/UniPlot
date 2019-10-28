import matplotlib.pyplot as plt

def plot_bar_show(d):
    """Configures and gives average length bar chart of proteins"""
    r = range(0, len(d))
    plt.figure()
    plt.bar(r, d.values())
    plt.xticks(r, d.keys(), rotation = 45, ha = "right", fontsize = 8)
    plt.title('Average Protein Length of Organisms', fontsize = 14)
    plt.tight_layout()
    plt.show()

def plot_pie_show(d):
    """Configures and gives average length pie chart of proteins"""
    plt.figure()
    sizes = d.values()

    def real_value(val):
        x = int(val/100*sum(sizes))
        return x

    plt.pie(sizes, labels = d.keys(), startangle = 110, autopct = real_value, pctdistance = 0.85, labeldistance = 1.05, textprops = {'fontsize': 8})
    plt.axis('equal')
    plt.title('Average Protein Length of Organisms', fontsize = 14)
    plt.tight_layout()
    plt.show()
