from matplotlib import pyplot as plt
import numpy as np

from . import get_all_readings


def generate_chart(j, p):
    
    # Numbers of pairs of bars you want
    N = 3

    # Data on X-axis

    # Specify the values of blue bars (height)
    blue_bar = (j[0], j[1], j[2])
    # Specify the values of orange bars (height)
    orange_bar = (p[0], p[1], p[2])

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(5,5), dpi=100)

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar , width, label='Senzor posude')
    plt.bar(ind + width, orange_bar, width, label='Karakteristika biljke')

    plt.xlabel('OČITANJA : SENZOR POSUDE <--> KARAKTERISTIKA BILJKE', 
                fontdict={
                'fontname' : 'Comic Sans MS', 
                'fontsize' : 12})
    plt.ylabel('VRIJEDNOSTI', 
            fontdict={
                'fontname' : 'Comic Sans MS', 
                'fontsize' : 12})
    plt.title('Usporedba očitanja senzora i karakteristika biljke',
            fontdict={
                'fontname' : 'Comic Sans MS', 
                'fontsize' : 14})

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Temperatura', 'pH FAKTOR', 'Vlažnost'), 
                fontdict={
                'fontname' : 'Comic Sans MS', 
                'fontsize' : 10})

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    return plt.savefig('app/static/pics/chart.png')


