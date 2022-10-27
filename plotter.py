# Description: code to create majestic plots!
#     script that produces 3 figures: iris_boxplot.png,
#     petal_length_v_width_scatter.png and multi_panel_figure.png
# Usage: python plotter.py

import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    # read in data
    iris = pd.read_csv('iris.data', header=None)
    iris.columns = ['sepal_width', 'sepal_length', 'petal_width',
                    'petal_length', 'species']
    return iris


def plot_boxplot():
    iris = read_data()

    # plot data
    f = plt.figure()
    iris_plt = iris[['sepal_width', 'sepal_length', 'petal_width',
                     'petal_length', 'species']].plot(kind='box')
    plt.ylabel('cm')
    plt.savefig('iris_boxplot')
    f.clear()
    plt.close(f)
    return None


def plot_scatter():
    iris = read_data()

    # for loop plpotting
    f = plt.figure()
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        plt.scatter(iris_subset['petal_length'],
                    iris_subset['petal_width'], label=species_name)
    plt.xlabel('petal_length (cm)')
    plt.ylabel('petal_width (cm)')
    plt.legend(loc='upper right')
    plt.savefig('petal_width_v_length_scatter')
    f.clear()
    plt.close(f)
    return None


def plot_multi_panel():
    iris = read_data()

    f = plt.figure()
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(10, 5)

    # right scatterplot
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        axes[1].scatter(iris_subset['petal_length'],
                        iris_subset['petal_width'], label=species_name)
    axes[1].set_xlabel('petal_length (cm)')
    axes[1].set_ylabel('petal_width (cm)')
    axes[1].legend(loc='lower right')

    # left boxplot
    measurement_names = ['sepal_width', 'sepal_length', 'petal_width',
                         'petal_length']
    axes[0].boxplot(iris[measurement_names], labels=measurement_names)
    axes[0].set_ylabel('cm')

    for i in range(2):
        # choose to hide of show certain borders or "spines"
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)
        axes[i].spines['bottom'].set_visible(True)
        axes[i].spines['left'].set_visible(True)

    plt.savefig('multi_panel_figure')
    f.clear()
    plt.close(f)

    return None


def main():
    plot_boxplot()
    plot_scatter()
    plot_multi_panel()


if __name__ == '__main__':
    main()
