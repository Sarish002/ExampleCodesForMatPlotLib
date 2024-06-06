from matplotlib import pyplot as plot
from matplotlib import style, rc
import numpy

plot.figure(figsize = (28, 21))
style.use('ggplot')

style.use('ggplot')
rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'

np = numpy.arange(0, 40 * numpy.pi, 0.1)
x = numpy.sin(np)
y = numpy.cos(np)

ax2 = plot.subplot(211)
plot.plot(x)
plot.grid(True, linestyle = '--')

ax1 = plot.subplot(212)
plot.plot(y)
plot.title('Sin and Cos')

ax2.set_title('Sine Graph')
ax1.set_title('Cosine Graph')
plot.show()
