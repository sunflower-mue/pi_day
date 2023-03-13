from colorama.ansi import Style
from visual import pi_digits
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import unicodedata
import colorama
from colorama import Fore
from visual import pi_digits

'''
Return a spiral color dot representation of the pi_digits
'''

def pi_picture():
    '''
        Return a pi symbol at center of a canvas and pi digits color encoded with cmap
        in spiral shape
    '''
    return unicodedata.lookup("GREEK SMALL LETTER PI")

def spiral():

    digits = np.arange(10)
    cmap_list = cm.get_cmap('Blues',10) #10 discrete colors


    #/////////////////////////
    r = np.linspace(0,20,999)

    t = np.linspace(0,2000,999)
    t = np.radians(t)

    x = r*np.cos(t)
    y = r*np.sin(t)


    fig, ax = plt.subplots()
    

    im = ax.scatter(x, y, c = pi_digits(),s=0.5, cmap=cmap_list)
    fig.colorbar(im,ax=ax)
    im.set_clim(0,9)

    plt.axis('equal')
    ax.axis('off')

    font ={'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': '16',
            }

    plt.title(label="INFINITY", fontdict= font, loc = 'center') # last digit on spiral must be an infinity symbol
    plt.show()

if __name__ == "__main__":
    print(Fore.YELLOW + pi_picture()) # Print at center of the spiral
    spiral()
