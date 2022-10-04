import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure('Михеева Кристина. 9 Вариант. Лабораторная работа №1', figsize=(7, 6))
plt.subplot(111, polar=True)
plt.title('ρ = a*ф, 0 <= ф <= B, a >= 0')

B = int(input())
phi = np.arange(0, B, 0.05)
a = int(input())
rho = a*phi
plt.plot(phi, rho, lw=2)

plt.show()
