from matplotlib import pyplot as plot
from matplotlib import style, rc

plot.figure(figsize = (5, 5))
style.use('ggplot')

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'

slices = [6.666, 0.8333, 4.16667, 1.66667, 2.5, 0.8333]
colorcols = ['#e8483c', '#e8813c', '#e5e83c', '#8ce83c', '#3ce8e5', '#3c4be8',]
labels = ['Sleep', 'Eat',
          'Code', 'Freshening up','TV',
          'Talk with Family']

plot.pie(slices, colors=colorcols, labels=labels, shadow=False, autopct='%1.1f%%')
plot.title('My Day!', loc='center')

plot.grid(True, color='k', linestyle = '-')
plot.show()