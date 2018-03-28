import matplotlib.pyplot as plt
from filterSmoothing import Mid

pullData = open("walking.txt", "r").read()  # Открытие файла на чтение
dataArray = pullData.split('\n')
x_label = []
x = []
y = []

for s in dataArray:  # Парсинг данных из файла
    spl = s.split(',')
    x_label.append(spl[0][-5:])
    x.append(len(y))
    y.append(int(spl[1]))

opt = Mid(10)  # Определение размера усредняющего окна в 10 значений
sh = opt.smoothOut(y)  # Применение скользящей средней на спарсиных данных

plt.xticks(x, x_label)

plt.plot(x, sh)  # Отрисовка полученных значений
plt.show()

