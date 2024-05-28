from PIL import Image, ImageDraw, ImageFont
from math import sqrt
# Исходные данные
Place_1 = [[0, 0, 0, 0, 0, 0, 0],       # строка 1
           [0, 0, 0,'x',0, 0, 0],       # строка 2
           [0,'a',0,'x',0,'b',0],       # строка 3
           [0, 0, 0,'x',0, 0, 0],       # строка 4
           [0, 0, 0, 0, 0, 0, 0]]       # строка 5

# Заготовка фона
PL = Image.new('RGB', (700, 500), (255,255,255))
re_PL = ImageDraw.Draw(PL)
front=ImageFont.truetype("arial.ttf", 20)

# Открытый список
open_list = []

# Закрытый список
closed_list = []


# Функция индексации всех точек
def Create_Template_List(Place):
    # point_of_Place_1 = [i, j, state, G(none), H(none), F(none)]
    default_list = []
    n = -1
    for i in Place:
        n += 1
        m = -1
        for j in i:
            m += 1
            if Place[n][m] == 'x' or Place[n][m] == 'a':
                default_list.append([n, m, 0, None, None, None])
            else:
                default_list.append([n, m, 1, None, None, None])
    return default_list
default_list = Create_Template_List(Place_1)
print(default_list)

# Функция разметки пространства
def Show_Place(Place):
    n=0
    for i in Place:
        n += 1
        m = 0
        for j in i:
            m+=1
            if j == 'x':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='black',outline=(255, 255, 255))
            elif j == 'a' or j == 'b':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='yellow',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),j, fill='black', font=front)
            else:
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='white',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),str(j), fill='black', font=front)

# Функция поиска точки A и B
def Find_Start_Finish(Place):
    n = 0
    for i in Place:
        n += 1
        m = 0
        for j in i:
            m += 1
            if j == 'a':
                point_start = (Place.index(i), i.index(j))
            if j == 'b':
                point_finish = (Place.index(i), i.index(j))
    return point_start, point_finish

# Функция поиска координат точек x
def Find_Coord_x(Place):
    list_x = []
    n = -1
    for i in Place:
        n += 1
        m = -1
        for j in i:
            m += 1
            if j == 'x':
                point_x = (n,m)
                list_x.append(point_x)
    return list_x       # возвращает список координат всех точек x

# F = G + H
# spisok = [i, j, state, G, H, F]   # кроме A и x
# state - какие точки? не x, не в закрытом списке
# но, если x - то, добавляем его координаты в особый список
# поиск пути
def Inspection_ASS(Place, default_list):
    point_start = Find_Start_Finish(Place)[0]
    open_list.append(point_start)
    # A = [i, j]   =>   A = [i, j, state, G, H, F]
    a_i, a_j = point_start[0](point_start[1])
    print(a_i, a_j)
    # default_list.append([i, j, 1, None, None, None])
    # [[0, 0, 1, None...],
    #  [0, 1, 1, None...]]
    for element in default_list:
        123
    cord_dict = [default_list[a_i[0],a_i[1]]]
    print(cord_dict)

Inspection_ASS(Place_1, default_list)



# Функция нахождения точки с минимальным значением вокруг искомой
# def point_min(s_i, s_j):
#     cord_dict = {Place_1[s_i-1][s_j]:[s_i-1,s_j],
#                  Place_1[s_i-1][s_j+1]:[s_i-1,s_j],
#                  Place_1[s_i][s_j+1]:[s_i,s_j+1],
#                  Place_1[s_i]:[s_i],
#                  Place_1[s_i+1][s_j]:[s_i+1,s_j],
#                  Place_1[s_i]:[s_i],
#                  Place_1[s_i][s_j-1]:[s_i,s_j-1],
#                  }
#     if 'x' in cord_dict.keys():
#         del cord_dict['x']
#     if 'b' in cord_dict.keys():
#         del cord_dict['b']
#     m = min(cord_dict.keys())
#     for k in cord_dict.keys():
#         if k == m:
#             start_cords = cord_dict[k]
#             start_point_i = start_cords[0]
#             start_point_j = start_cords[1]
#             return ([start_point_i, start_point_j, m])

# Функция добавления путевой точки в открытый список
def Add_Open_List(path_point):
    open_list.append(path_point)

# Функция добавления путевой точки в закрытый список
def Add_Closed_List(path_point):
    closed_list.append(path_point)

# def placement(Place):

# placement(Place_1)

contin=0
Show_Place(Place_1)
PL.show()
