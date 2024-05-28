from PIL import Image, ImageDraw, ImageFont
import os

#Исходные данные
        # 0   1 2 3   4   5  6  7   8   9  10  11 12 13  14 15
Place_1=[[1,  1,1,2,  3,  3,'x',1,  1,  1,  1,  1,1,  1,  1,1],
         [1,  1,1,2,'x',  3,'x',1,  1,  1,  1,  1,1,  1,  1,1],
         [1,  1,1,1,'x',  4,'x',1,  1,  1,  1,'x',1,  1,  1,1],
         [1,'a',1,1,'x',  5,'x',1,  1,  1,  1,'x',1,  1,  1,1],
         [1,  1,1,1,'x',  5,'x',1,  1,'x','x','x',1,  1,  1,1],
         [1,  1,1,1,'x',  4,'x',1,  1,'x','x','x',1,  1,  1,1],
         [1,  1,1,1,'x',  3,'x',1,'x','x','x','x',1,  1,  1,1],
         [1,  1,1,1,'x',  3,'x',1,'x','x','x','x',1,  1,'b',1],
         [1,  1,1,1,'x',  2,  2,1,  1,'x','x','x',1,  1,  1,1],
         [1,  1,1,1,'x',  1,  1,1,  1,  1,'x','x',1,  1,  1,1],
         [1,  1,1,1,'x',  1,  1,2,  2,  2,'x','x',2,  2,  2,1],
         [1,  1,1,1,'x','x',  1,2,  3,  3,'x','x',3,  3,  2,1],
         [1,  1,1,1,  1,'x',  1,2,  3,  4,'x','x',4,  3,  2,1],
         [1,  1,1,1,  1,'x',  1,2,  3,  4,  5,  5,4,  3,  2,1],
         [1,  1,1,1,  1,'x',  1,2,  3,  4,  5,  5,4,  3,  2,1],
         [1,  1,1,1,  1,  1,  1,2,  3,  4,  5,  5,4,  3,  2,1]]

A = [3,1]
B = [7,14]
#Заготовка фона
NameDirectori = os.path.basename(__file__)
NameDirectori = os.path.abspath(__file__).replace(NameDirectori, '')
PL = Image.new('RGB', (1600, 1600), (255,255,255)) # Базовое изображение
re_PL = ImageDraw.Draw(PL)
front=ImageFont.truetype(NameDirectori+"arial.ttf", 50)

#Функция разметки пространства
def ShowPlace(Place, Line):
    n=0
    for i in Place:
        n+=1
        m=0
        for j in i:
            m+=1
            if j=='x':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='black',outline=(255, 255, 255))
            elif j=='b':
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='yellow',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),j, fill='black', font=front)
            else:
                re_PL.rectangle((m*100-100, n*100-100, m*100, n*100), fill='white',outline=(0, 0, 0))
                re_PL.text((m*100-80, n*100-80),str(j), fill='black', font=front)

    for i in range(len(Line)):
        y = Line[i][0]
        x = Line[i][1]
        re_PL.rectangle((x*100, y*100, x*100+100, y*100+100), fill='red',outline=(255, 255, 255))
        if not ((Place[y][x] == 'b') or (Place[y][x] == 'a')):
            re_PL.text((x*100+20, y*100+20),str(round(int(Place[y][x]),0)), fill='black', font=front)
        else: 
            re_PL.text((x*100+20, y*100+20),str(Place[y][x]), fill='black', font=front)

def AStar(Array, Apos, Bpos):
    #                                От A до B
    CM = [[Apos[0],Apos[1],0,(Bpos[0]-Apos[0]+Bpos[1]-Apos[1])]] # Массив пути 
    ArrForFound = [[Apos[0],Apos[1]]]
    OM = [] # Массив потенциальных точек

    ArrObhoda = [[ 0, 1,1],
                 [-1, 1,(2)**0.5],
                 [-1, 0,1],
                 [-1,-1,(2)**0.5],
                 [ 0,-1,1],
                 [ 1,-1,(2)**0.5],
                 [ 1, 0,1],
                 [ 1, 1,(2)**0.5]]

    x0 = CM[-1][0]
    y0 = CM[-1][1]
    s0 = CM[-1][2]

    # Бесконечный цикл
    check = True
    time = 0
    while check:
        time = time + 1
        # Заполнение внешнего массива (OM)
        for i in range(8):
            # print("i = ",i,": ", x0+ArrObhoda[i][0],"|", y0+ArrObhoda[i][1])
            if (not(([x0+ArrObhoda[i][0], y0+ArrObhoda[i][1]]) in ArrForFound) and 
                    (x0+ArrObhoda[i][0] > -1) and (x0+ArrObhoda[i][0] < 15) and 
                    (y0+ArrObhoda[i][1] > -1) and (y0+ArrObhoda[i][1] < 15)): # Проверка границ

                OM.append([x0+ArrObhoda[i][0], y0+ArrObhoda[i][1], s0 + ArrObhoda[i][2]*Array[x0+ArrObhoda[i][0]][y0+ArrObhoda[i][1]], Bpos[0] - x0 + Bpos[1] - y0])
                # OM[str([x0+ArrObhoda[i][0], y0+ArrObhoda[i][1]]): [s0 + ArrObhoda[i][2]*Array[x0+ArrObhoda[i][0]][y0+ArrObhoda[i][1]], (Bpos[0] - x0 + Bpos[1] - y0)]]
                # Array[x0+ArrObhoda[i][0]][y0+ArrObhoda[i][1]] = OM[-1][2]
            # else: print("-")
        
        # Поиск элемента с минимальным значением
        min = [0,0,1000,1000]
        pos_min = None
        m = 0
        for i in OM:
            if (i[2]+i[3]) < (min[2]+min[3]):
                min = i
                pos_min = m
            m = m + 1
        
        # print("OM: ", OM)
        # print("min: ", min)

        OM.remove(min)
        CM.append(min)

        # x0 = CM[-1][0] # Current_X
        # y0 = CM[-1][1] # Current_Y
        # s0 = CM[-1][2] # Current_S

        if (x0==Bpos[0]) and (y0==Bpos[1]) or (time == 900): 
            print(time)
            check = False
    # Array[Bpos[0]][Bpos[1]] = 'b'
    return(CM)

def track(Array, Apose, Bpose):
    Line = [Bpose]
    ArrObhoda = [[ 0, 1],
                 [-1, 1],
                 [-1, 0],
                 [-1,-1],
                 [ 0,-1],
                 [ 1,-1],
                 [ 1, 0],
                 [ 1, 1]]
    checkend = True
    while checkend:
        min = Line[-1]
        for i in ArrObhoda:
            try: (Array[min[0]][min[1]])
            except: 
                print(Array[Line[-1][0]+i[0]][Line[-1][1]+i[1]])
                print(Array[min[0]][min[1]])
            
            if (Array[Line[-1][0]+i[0]][Line[-1][1]+i[1]] == 'a'):
                Line.append(Apose)
                checkend = False
                break
            elif (not (Array[Line[-1][0]+i[0]][Line[-1][1]+i[1]] == 'x') and
                (Line[-1][0]+i[0]<15)and(Line[-1][0]+i[0]>-1)and
                (Line[-1][1]+i[1]<15)and(Line[-1][1]+i[1]>-1)):    
                if (not (Array[Line[-1][0]+i[0]][Line[-1][1]+i[1]] == 0) and
                        (Array[Line[-1][0]+i[0]][Line[-1][1]+i[1]] < Array[min[0]][min[1]])):
                    min = ([Line[-1][0]+i[0], Line[-1][1]+i[1]])
        Line.append(min)
    Array[Bpose[0]][Bpose[1]] = 'b'
    Line.pop(-1)
    return(Line)

def main():
    result = AStar(Place_1, A, B)
    # print(result)

    ATreck = track(Place_1, A, B)
    ShowPlace(Place_1, ATreck)
    # ShowPlace(Place_1, result)
    PL.show()

if __name__ == "__main__":
    main()