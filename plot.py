

import matplotlib.pyplot as plt 
from matplotlib import font_manager as fm

 # styling :]
background_color = 'black'
font_color = 'white'

figure = plt.figure(facecolor=background_color)
axes = plt.axes(facecolor=background_color)
for spine in axes.spines.keys(): 
    axes.spines[spine].set_color(font_color)
axes.tick_params(axis='x', colors=font_color)
axes.tick_params(axis='y', colors=font_color)

prop = fm.FontProperties(fname='RobotoMono-VariableFont_wght.ttf')
for label in (axes.get_xticklabels() + axes.get_yticklabels()): 
    label.set_fontproperties(prop)


# plot prices 
from datetime import datetime
from fetch import get_price
from matplotlib.animation import FuncAnimation

prices = []
times = []

def animate(arg):
    global times 
    global prices

    times.append(datetime.now())
    price = get_price('TSLA')
    prices.append(price)

    color = '#ff0000' if prices[-1] > price else '#00ff00'
    plt.cla()
    plt.plot(times[-20:], prices[-20:], color=color)

animation = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()