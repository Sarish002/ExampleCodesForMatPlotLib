from matplotlib import pyplot as plot
from matplotlib import style, rc
from matplotlib.patches import Rectangle, Polygon, RegularPolygon, Circle, Ellipse
import numpy as npnum
fig, ax = plot.subplots(1, 1)
ax.axis([0, 200, 0, 200])
ax.axis('off')

Recta = Rectangle((50, 5),
                  width=100,
                  height=50,
                  linewidth=5,
                  fill = False,
                  color = 'k')

Circa = Circle((100, 80),
               radius = 25,
               color = 'k',
               fill=False,
               linewidth=5,
               angle=0.25)

RegPol = RegularPolygon((100, 120),
                        numVertices=3,
                        radius=20,
                        color='k',
                        fill=False,
                        linewidth=5)

nparray = npnum.array( ((150, 55), (150, 27.5), (199, 75), (199, 100)))
anarray = npnum.array( ((50, 55), (50, 27.5), (1, 75), (1, 100)) )
EmployerGon = Polygon(nparray,
                       fill = False,
                       color = 'k',
                      linewidth = 5)
EmployerCame = Polygon(anarray,
                       fill = False,
                       color = 'k',
                      linewidth = 5)
style.use('ggplot')

rc('font', **{'family': 'Comic Sans MS'})
plot.rcParams['axes.facecolor'] = '#FFFFFF'
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)
ax.add_patch(Recta)
ax.add_patch(Circa)
ax.add_patch(RegPol)
ax.add_patch(EmployerGon)
ax.add_patch(EmployerCame)
plot.show()