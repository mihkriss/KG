import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button


def TransparentON(event):
    axis.add_collection3d(Poly3DCollection(
        frame, facecolors=[1, 0.4, 0.3], alpha=0.7, linewidths=1, edgecolors='black'))


def TransparentOFF(event):
    axis.add_collection3d(Poly3DCollection(
        frame, facecolors=[1, 0.4, 0.3], alpha=1, linewidths=1, edgecolors='black'))


fig = plt.figure('Михеева Кристина. Вариант №4. Лабораторная работа №2', figsize=(7, 6))
axis = fig.add_subplot(111, projection='3d')

buttonON = fig.add_subplot(863)
btnON = Button(buttonON, 'ON')
btnON.on_clicked(TransparentON)
btnON.color = '#778899'

buttonOFF = fig.add_subplot(864)
btnOFF = Button(buttonOFF, 'OFF')
btnOFF.on_clicked(TransparentOFF)
btnOFF.color = '#778899'

x = 15
y = 10
z = 20

p = np.array([
    [x / 2, -y / 2, -z / 2],
    [-x / 2, -y / 2, -z / 2],
    [-x / 2, y / 2, -z / 2],
    [x / 2, y / 2, -z / 2],
    [0, -y / 2, z / 2],
    [0, y / 2, z / 2]
])
frame = [
    [p[0], p[4], p[1]],
    [p[3], p[5], p[2]],
    [p[0], p[1], p[2], p[3]],
    [p[1], p[4], p[5], p[2]],
    [p[0], p[4], p[5], p[3]]
]

axis.scatter3D(p[:, 0], p[:, 1], p[:, 2], color='black')

axis.add_collection3d(Poly3DCollection(
    frame, facecolors=[1, 0.4, 0.3], alpha=0.7, linewidths=1, edgecolors='black'))

axis.set_xlabel('X', fontsize=20, color='black')
axis.set_ylabel('Y', fontsize=20, color='black')
axis.set_zlabel('Z', fontsize=20, color='black')
axis.set_title('\"Клин\"\nПрозрачность')

plt.show()