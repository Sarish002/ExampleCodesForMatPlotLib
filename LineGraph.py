from matplotlib import pyplot as plot, style, rc

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'
x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
y = [1, 2.5, 3, 4.5, 5, 6.5, 7]

x2 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
y2 = [1, 3, 3, 5, 5, 7, 7]

plot.plot(x, y, '#9F35FC', label = "Ben's Reading (Hours) / Day", linewidth = 2)
plot.plot(x2, y2, '#28D6FC', label = "Rachel's Reading (Hours) / Day", linewidth = 2)

plot.title('Hours Spent Reading in a week')
plot.xlabel("Days")
plot.ylabel("Hours")

plot.legend()
plot.grid(True, color='k', linestyle = '--')
plot.show()