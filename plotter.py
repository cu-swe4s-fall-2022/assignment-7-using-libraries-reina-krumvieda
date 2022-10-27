# Description: code to create majestic plots!
#     script that produces 3 figures: iris_boxplot.png,
#     petal_length_v_width_scatter.png and multi_panel_figure.png
# Usage: python plotter.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_boxplot():
    #read in data
    iris = pd.read_csv('iris.data')
    iris.columns = ['sepal_width','sepal_length','petal_width',
                    'petal_length','species']

    #plot data
    f = plt.figure()
    iris_plt = iris[['sepal_width','sepal_length','petal_width',
                     'petal_length','species']].plot(kind='box')
    plt.ylabel('cm')
    plt.savefig('iris_boxplot')
    f.clear()  
    plt.close(f)

def plot_scatter():
    #read in data
    iris = pd.read_csv('iris.data')
    iris.columns = ['sepal_width','sepal_length','petal_width',
                    'petal_length','species']
    #for loop plpotting
    f = plt.figure()
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        plt.scatter(iris_subset['petal_length'],
                    iris_subset['petal_width'],label=species_name)
    plt.xlabel('petal_length (cm)')
    plt.ylabel('petal_width (cm)')
    plt.legend(loc='upper right')
    plt.savefig('petal_width_v_length_scatter')
    f.clear()  
    plt.close(f)

    
def plot_multi_panel():
    iris = pd.read_csv('iris.data')
    measurement_names = ['sepal_width','sepal_length','petal_width',
                         'petal_length','species']
    iris.columns = measurement_names

    fig = plt.figure()
    fig, axes = plt.subplots(2)
    #left boxplot
    #axes[0,0].plot_boxplot()
    #axes[0,1].plot_scatter()

    plt.savefig('multi_panel_figure')
    fig.clear()  
    plt.close(fig)
    return None

def main():
    plot_boxplot()
    plot_scatter()
    plot_multi_panel()
    
if __name__ == '__main__':
    main()