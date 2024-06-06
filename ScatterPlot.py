from matplotlib import pyplot as plot
from matplotlib import style, rc

plot.figure(figsize = (7, 5))
style.use('ggplot')

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'

x = [12, 23, 34, 45, 56, 67, 78, 89]
x2 = [9, 20, 31, 42, 53, 64, 75, 86]

y = ['Rachel', 'Abhinav', 'Fred', 'Kiran', 'Navin', 'David', 'Ashwin', 'Zoe']

plot.scatter(y, x, label = 'Marks in English', color='#9a07f5')
plot.scatter(y, x2, label = 'Marks in Math', color='#e83cc9')
plot.title('English or Math?', loc='center')
plot.xlabel("Student")
plot.ylabel("Marks")

plot.legend()
plot.grid(True, color='k', linestyle = '-')
plot.show()