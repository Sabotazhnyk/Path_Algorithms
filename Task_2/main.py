from PIL import Image, ImageDraw, ImageFont
from scipy.spatial import distance
from math import sqrt

# Исходные данные - Список вложенных списков
# Place_1 =   [[0,  0,0,0,  0,  0,'x',0,  0,  0,  0,  0,0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,  0,  0,  0,  0,0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,  0,  0,  0,'x',0,  0,  0,0],
#             [0,'a',0,0,'x',  0,'x',0,  0,  0,  0,'x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,  0,'x','x','x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,  0,'x','x','x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,'x','x','x','x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,'x',0,'x','x','x','x',0,  0,'b',0],
#             [0,  0,0,0,'x',  0,  0,0,  0,'x','x','x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,  0,0,  0,  0,'x','x',0,  0,  0,0],
#             [0,  0,0,0,'x',  0,  0,0,  0,  0,'x','x',0,  0,  0,0],
#             [0,  0,0,0,'x','x',  0,0,  0,  0,'x','x',0,  0,  0,0],
#             [0,  0,0,0,  0,'x',  0,0,  0,  0,'x','x',0,  0,  0,0],
#             [0,  0,0,0,  0,'x',  0,0,  0,  0,  0,  0,0,  0,  0,0],
#             [0,  0,0,0,  0,'x',  0,0,  0,  0,  0,  0,0,  0,  0,0],
#             [0,  0,0,0,  0,  0,  0,0,  0,  0,  0,  0,0,  0,  0,0]]

Place_1 = [[0, 0, 0, 0, 0, 0, 0],       # строка 1
           [0, 0, 0,'x',0, 0, 0],       # строка 2
           [0,'a',0,'x',0,'b',0],       # строка 3
           [0, 0, 0,'x',0, 0, 0],       # строка 4
           [0, 0, 0, 0, 0, 0, 0]]       # строка 5


# ====================================================================================================

# Поиск координат Начальной точки(a[x, y]) и Финальной точки (b[x, y)]
'''
Таблица с исходными данными предстваляет из себя список со вложенными списками.
Place = [j_1[i_1, i_2, ..., i_n],
         j_2[i_1, i_2, ..., i_n],
         .......................,
         j_n[i_1, i_2, ..., i_n]]
Вложенные списки - это значения всех столбцов одной строки (i). А глобальный список - это вложенные строки (j).
Счётчик сначала прогоняет построчно каждую строку и каждый элемент её списка, сравнивая с условием.
Если условие выполнено, подсчитанные значения i и j являются координатами искомой точки [j, i] = [x, y].
На выходе, возвращаются значения координат Начальной точки(a[x, y]) и Финальной точки (b[x, y).
'''
def start_finish_for_manh(Place):
    n = 0
    for i in Place:
        m = 0
        for j in i:
            if j == 'a':
                point_start = [i.index(j), Place.index(i)]      # Координата a[x,y]
            if j == 'b':
                point_finish = [i.index(j), Place.index(i)]     # Координата b[x,y)
            m += 1
        n += 1
    return point_start, point_finish


# ====================================================================================================

# Получение координат Начальной точки(a[x, y]) и Финальной точки (b[x, y)
'''
На вход функции start_finish_for_manh подаётся Список вложенных списков Place_1.
На выходе, переменные point_start и point_finish получают значения Начальной точки(a[x, y]) и Финальной точки (b[x, y) соответственно.
'''
point_start, point_finish = start_finish_for_manh(Place_1)

# Наделение начальной и финальной точки для метода Манхэттена
point_start_m, point_finish_m = start_finish_for_manh(Place_1)
point_start_m.append(0)
point_finish_m.append(0)


class Cage:
    def __init__(self, x, y, contain):
        self.cord_x = x
        self.cord_y = y
        self.contain = contain  # can  be  0|x|b|a
        self.F = 0  # F = G + H
        self.G = 0  # energy from start to current cage
        self.H = 0  # energy from current cage to final (Алгоритм манхэттона)

    def calculate_H(self, point_start, point_finish):
        self.H = distance.cityblock(point_start, point_finish)

    def calculate_F(self):
        self.F = self.G + self.H

    def set_G(self, new_G):
        self.G = new_G
        Cage.calculate_F(self)

# ====================================================================================================

# Размер списка
def size_of_place(Place):
    n = 0
    for i in Place:
        n += 1
        m = 0
        for j in i:
            m += 1
    return m, n


# Заготовка фона
size_of_place_x, size_of_place_y = size_of_place(Place_1)                           # Получение размера списка
PL = Image.new('RGB', (size_of_place_x*100, size_of_place_y*100), (255,255,255))    # Создание фона, опираясь на размер списка
re_PL = ImageDraw.Draw(PL)
front=ImageFont.truetype("arial.ttf", 20)


# Функция разметки пространства
def ShowPlace(Place):
    n = 0
    for i in Place:
        n += 1    # y
        m=0     # x
        for j in i:
            m+=1
            if j=='x':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='black',outline=(255, 255, 255))
            elif j=='a' or j=='b':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='yellow',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),j, fill='black', font=front)
            else:
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='white',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),str(j), fill='black', font=front)

contin = 0
ShowPlace(Place_1)
PL.show()

# ====================================================================================================

list_of_instances = []


def create_list_of_instances(Place):
    n = 0
    for i in Place:
        m = 0
        for j in i:
            #print(m,n,j)
            list_of_instances.append(Cage(m, n, j))
            m += 1
        n += 1


create_list_of_instances(Place_1)
lenght_of_maze_row = len(Place_1[0])
open_list = []
close_list = []


def check_around(point_start):
    # finding home point in class instances list
    elements_for_best_search = []
    for elem in list_of_instances:
        if elem.cord_x == point_start[0] and elem.cord_y == point_start[1]:
            home_point = elem
            pass

    # check start point coordinates equal to form (x, y, z)
    if len(point_start) < 3:
        point_start_for_h = point_start + [0]
    else:
        point_start_for_h = point_start
    G_p = home_point.G

    home_point.calculate_H(point_start_for_h, point_finish_m)

    if home_point in open_list:
        #print("Deliting:", home_point.cord_x, home_point.cord_y)
        open_list.pop(open_list.index(home_point))

    check_list = [[point_start[0] - 1, point_start[1] - 1],     # G = G_p + 14
                  [point_start[0] - 1, point_start[1]],         # G = G_p + 10
                  [point_start[0] - 1, point_start[1] + 1],     # G = G_p + 14
                  [point_start[0],     point_start[1] - 1],     # G = G_p + 10
                  [point_start[0],     point_start[1] + 1],     # G = G_p + 10
                  [point_start[0] + 1, point_start[1] - 1],     # G = G_p + 14
                  [point_start[0] + 1, point_start[1]],         # G = G_p + 10
                  [point_start[0] + 1, point_start[1] + 1]]     # G = G_p + 14

    list_of_G = [14, 10, 14, 10, 10, 14, 10, 14]
    close_list.append(home_point)
    # looking up to collect information about cages around
    for point in check_list:
        for element in list_of_instances:
            if element.cord_x == point[0] and element.cord_y == point[1]:
                if element.contain != 'x' and element not in close_list:
                    element.calculate_H([element.cord_x, element.cord_y, 0], point_finish_m)
                    element.set_G(G_p + list_of_G[check_list.index(point)])
                    elements_for_best_search.append(element)
                    open_list.append(element)
                elif element.contain == 'x' and element not in close_list:
                    close_list.append(element)

    # searching best next step position
    best_F = elements_for_best_search[-0]
    for element in elements_for_best_search:
        print(element.cord_x, element.cord_y, element.F, element.H, element.G)
        if element.F <= best_F.F:
            best_F = element
    return best_F

#check_around(point_start)


best_next_step = check_around(point_start)
print("Point_start", point_start)
print("Point_finish", point_finish)
for i in range(15):
    print(best_next_step.cord_x,best_next_step.cord_y)
    best_next_step = check_around([best_next_step.cord_x, best_next_step.cord_y])
    if [best_next_step.cord_x, best_next_step.cord_y] == point_finish:
        print("Ура победа ")
        break

