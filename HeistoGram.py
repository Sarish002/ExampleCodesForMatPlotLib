from matplotlib import pyplot as plot
from matplotlib import style, rc

plot.figure(figsize = (5, 5))
style.use('ggplot')

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'

GA = [7, 9, 13, 8, 24, 23, 18, 19, 14, 6, 57, 34, 53, 29, 37,
      83, 71, 56, 33, 11, 22, 44, 55, 66, 77, 88, 99, 91,82, 73,
      64, 55, 12, 23, 34, 45, 56, 67, 78, 89, 90, 9, 98, 87, 76,
      65, 54, 43, 32, 21]

Bins_Qual = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plot.hist(GA, Bins_Qual, edgecolor = 'k', histtype="bar", rwidth=0.5, color='#c76ded', label='People No.')
plot.title('Group Ages!', loc='center')
plot.xlabel("No. of people with Age in given range")
plot.ylabel("Ranges of Age")

plot.legend()
plot.grid(True, color='k', linestyle = '-')
plot.show()