from PIL import Image, ImageDraw, ImageFont

# Исходные данные
Place_1=[[0,  0,0,0,'x',  0,0,0,  0,  0,  0,  0,0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,  0,  0,  0,  0,0,'b',0,0],
         [0,  0,0,0,'x',  0,0,0,  0,  0,  0,  0,0,  0,0,0],
         [0,  1,0,0,'x',  0,0,0,  0,  0,  0,'x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,  0,'x','x','x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,  0,'x','x','x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,'x','x','x','x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,'x','x','x','x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,  0,'x','x','x',0,  0,0,0],
         [0,  0,0,0,'x',  0,0,0,  0,  0,'x','x',0,  0,0,0],
         [0,  0,0,0,  0,'x',0,0,  0,  0,'x','x',0,  0,0,0], 
         [0,  0,0,0,  0,'x',0,0,  0,  0,'x','x',0,  0,0,0],
         [0,  0,0,0,  0,  0,0,0,  0,  0,'x','x',0,  0,0,0],
         [0,  0,0,0,  0,  0,0,0,  0,  0,  0,'x',0,  0,0,0],
         [0,  0,0,0,  0,  0,0,0,  0,  0,  0,'x',0,  0,0,0],
         [0,  0,0,0,  0,  0,0,0,  0,  0,  0,  0,0,  0,0,0]]

# Заготовка фона
PL = Image.new('RGB', (1600, 1600), (255,255,255))
re_PL = ImageDraw.Draw(PL)
front = ImageFont.truetype("arial.ttf", 50)


# Функция разметки пространства
def ShowPlace(Place):
    n = 0
    for i in Place:
        n += 1
        m = 0
        for j in i:
            m += 1
            if j == 'x':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='black', outline=(255, 255, 255))
            elif j == 1 or j == 'b':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='yellow', outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80), str(j), fill='black', font=front)
            else:
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='white',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80), str(j), fill='black', font=front)

# Функция нахождения координат начальной точки
def start_point(Place):
    n = 0
    for i in Place:
        n += 1
        m = 0
        for j in i:
            m += 1
            if j == 1:
                point_s = (Place.index(i),i.index(j))
    return point_s
 
# Функция нахождения точки с минимальным значением вокруг искомой
def point_min(s_i, s_j):
    cord_dict = {Place_1[s_i-1][s_j]:[s_i-1,s_j],    
                 Place_1[s_i][s_j+1]:[s_i,s_j+1],
                 Place_1[s_i+1][s_j]:[s_i+1,s_j],
                 Place_1[s_i][s_j-1]:[s_i,s_j-1]}
    if 'x' in cord_dict.keys():
        del cord_dict['x']
    if 'b' in cord_dict.keys():
        del cord_dict['b']
    m = min(cord_dict.keys())
    for k in cord_dict.keys():
        if k == m:
            start_cords = cord_dict[k]
            start_point_i = start_cords[0]
            start_point_j = start_cords[1]
            return ([start_point_i, start_point_j, m])

# Функция окрашивания пути
def trail_painting(way):        # way = [(first_way_i_cord, first_way_j_cord, value_at_cords), .... ,(last_way_i_cord, last_way_j_cord, value_at_cords)]
    for cords in way:           # cords = (way_i_cord, way_j_cord, value_at_cords)
        x = cords[1] + 1
        y = cords[0] + 1
        re_PL.rectangle((x*100-100, y*100-100, x*100, y*100), fill='red', outline=(0, 0, 0))
        re_PL.text((x*100-80, y*100-80), str(cords[2]), fill='black', font=front)


# Построение маршрута

# нумерация ячеек
max_way_lenght = 50             # задаётся длина волны
point_s = start_point(Place_1)  # задаётся стартовая точка пути (b)
width = len(Place_1[0])         # ширина матрицы Place_1
height = len(Place_1)           # высота матрицы Place_1

p_s = 1                         # начальное минимальное значение стартовой точки (1)
for k in range(max_way_lenght):
    for i in range(height):     # высота
        for j in range(width):  # ширина
            if Place_1[i][j] == p_s:
                if j < 15 and Place_1[i][j+1] == 0:
                    Place_1[i][j+1] = p_s + 1
                if j > 0 and Place_1[i][j-1] == 0:
                    Place_1[i][j-1] = p_s + 1 
                if i < 15 and Place_1[i+1][j] == 0:
                    Place_1[i+1][j] = p_s + 1
                if i > 0 and Place_1[i-1][j] == 0:
                    Place_1[i-1][j] = p_s + 1
    p_s = p_s + 1

# Нахождение координаты конечной точки
p_e = 'b'                       # значение конечной точки (b)
for i in range(height):
    for j in range(width):
        if Place_1[i][j] == p_e:
            s_i = i
            s_j = j

# Трассировка пути
# берутся координаты и числовое значение точки для первого шага
start_point_i, start_point_j, step_value = point_min(s_i, s_j)
way = []                        # список координат, находящихся на кратчайшем пути (координата x, координата y, числовое значение координаты)
way.append((start_point_i, start_point_j, step_value))  # добавление первого шага в список
for k in range(max_way_lenght):
    # поиск минимального значения ближайшей ячейки из прилижащих
    start_point_i, start_point_j, step_value = point_min(start_point_i, start_point_j)
    way.append((start_point_i, start_point_j, step_value))
    if (start_point_i, start_point_j) == point_s:   # при нахождении начальной точки - завершение цикла
        break
way.pop()                       # удаление поседнего элемента списка (начальную точку (1))

ShowPlace(Place_1)              # разметка 
trail_painting(way)             # окраска пути
PL.show()                       # вывод на экран
