from PIL import Image, ImageDraw, ImageFont
from math import sqrt
#Исходные данные
Place_1=[[0,  0,0,0,  0,  0,'x',0,  0,  0,  0,  0,0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,  0,  0,  0,  0,0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,  0,  0,  0,'x',0,  0,  0,0],
         [0,'a',0,0,'x',  0,'x',0,  0,  0,  0,'x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,  0,'x','x','x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,  0,'x','x','x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,'x','x','x','x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,'x',0,'x','x','x','x',0,  0,'b',0],
         [0,  0,0,0,'x',  0,  0,0,  0,'x','x','x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,  0,0,  0,  0,'x','x',0,  0,  0,0],
         [0,  0,0,0,'x',  0,  0,0,  0,  0,'x','x',0,  0,  0,0],
         [0,  0,0,0,'x','x',  0,0,  0,  0,'x','x',0,  0,  0,0],
         [0,  0,0,0,  0,'x',  0,0,  0,  0,'x','x',0,  0,  0,0],
         [0,  0,0,0,  0,'x',  0,0,  0,  0,  0,  0,0,  0,  0,0],
         [0,  0,0,0,  0,'x',  0,0,  0,  0,  0,  0,0,  0,  0,0],
         [0,  0,0,0,  0,  0,  0,0,  0,  0,  0,  0,0,  0,  0,0]]

#Заготовка фона
PL = Image.new('RGB', (1600, 1600), (255,255,255))
re_PL = ImageDraw.Draw(PL)
front=ImageFont.truetype("arial.ttf", 20)

#Функция разметки пространства
def ShowPlace(Place):
    n=0
    for i in Place:
        n+=1
        m=0
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

def placement(Place):

    """ Функция собственно расставляет маршрут без учёта """

    flag1 = 0
    Max = 0
    Place_2 = Place
    flag2 = 0
    for _ in range (30):
        Max += 1 
        n=0
        for i in Place_2:
            m = 0
            for j in i:
                if j == Max:
                    if n >= 1 and (Place_2[n - 1][m] == 0 or Place_2[n - 1][m] == 'x'):
                        Place_2[n - 1][m] = Max + 1
                    if n <= 14 and (Place_2[n + 1][m] == 0 or Place_2[n + 1][m] == 'x'):
                        Place_2[n + 1][m] = Max + 1
                    if m >= 1 and (Place_2[n][m - 1] == 0 or Place_2[n][m - 1] == 'x'):
                        Place_2[n][m - 1] = Max + 1
                    if m <= 14 and (Place_2[n][m + 1] == 0 or Place_2[n][m + 1] == 'x'):
                        Place_2[n][m + 1] = Max + 1 
                if j == 'a':
                    if n >= 1 and Place_2[n - 1][m] == Max:
                        flag1 = 1
                    elif n <= 14 and Place_2[n + 1][m] == Max:
                        flag1 = 1
                    elif m >= 1 and Place_2[n][m - 1] == Max:
                        flag1 = 1
                    elif m <= 14 and  Place_2[n][m + 1] == Max:
                        flag1 = 1
                if flag2 == 0 and j == 'b':
                    Place_2[n - 1][m] = 1
                    Place_2[n + 1][m] = 1
                    Place_2[n][m - 1] = 1
                    Place_2[n][m + 1] = 1
                    flag2 = 1
                    Max = 0
                    break
                m+=1 
            n+=1
            if flag2 == 1:
                flag2 = 3
                break 
    allocation(Place, Place_2)

def allocation(Place, Place_2):
    Place_3 = Place
    Max = 0
    for _ in range (30):
        Max += 1 
        n=0
        for i in Place_3:
            m = 0
            for j in i:
                if j == Max:
                    if n >= 1 and Place_2[n - 1][m] == 0:
                        Place_2[n - 1][m] = Max + 1
                    if n <= 14 and Place_2[n + 1][m] == 0:
                        Place_2[n + 1][m] = Max + 1
                    if m >= 1 and Place_2[n][m - 1] == 0:
                        Place_2[n][m - 1] = Max + 1
                    if m <= 14 and Place_2[n][m + 1] == 0:
                        Place_2[n][m + 1] = Max + 1
                    if n >= 1 and n <= 14 and 
                         


placement(Place_1)

contin=0
PL.show()





