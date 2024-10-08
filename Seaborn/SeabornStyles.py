import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
    sns.despine(left=True)

    plt.show()

with sns.axes_style('ticks'):
    plt.subplot(211)
    plot()

plt.subplot(212)
plot()

# darkgrid
# whitegrid
# dark
# white
# ticks