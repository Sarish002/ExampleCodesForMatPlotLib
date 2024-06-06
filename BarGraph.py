from matplotlib import pyplot as plot, style, rc
import numpy as np

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'

plot.figure(figsize = (5, 5))
style.use('ggplot')

x = ['M', 'T', 'W', 'TH', 'F', 'SU',
     'ST']

x_eind = np.arange(len(x))

y = [1, 2.5, 3, 4.5, 5, 6.5, 7]
y2 = [1, 3, 2.5, 4.5, 4, 6, 5.5]

plot.bar(x_eind + 0.09, y, width = 0.2, color = '#BD6BFB', label = "Ben's reading hours")
plot.bar(x_eind - 0.09, y2, width = 0.2, color = '#6BC9FB', label = "Rachel's reading hours")

plot.title('Hours Spent Reading in a week', loc='center')
plot.xlabel("Days")
plot.ylabel("Hours")

plot.legend()
plot.grid(True, color='k', linestyle = '--')
plot.show()