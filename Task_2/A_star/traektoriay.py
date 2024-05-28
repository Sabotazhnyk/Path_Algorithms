from PIL import Image, ImageDraw, ImageFont
import os

#Исходные данные
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
    print(Line)
    for i in range(Line[1][0]):
        y = Line[i+1][1][0]
        x = Line[i+1][1][1]
        re_PL.rectangle((x*100, y*100, x*100+100, y*100+100), fill='red',outline=(255, 255, 255))
        re_PL.text((x*100+20, y*100+20),str(Place[y][x]), fill='black', font=front)

def SettingTheScales(Array):
    # print(len(Array),"x",len(Array[0]))
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            if (Array[i][j] != 0) and (type(Array[i][j]) == int):
                if (i+1 < len(Array)) and not(Array[i+1][j]): Array[i+1][j] = Array[i][j] + 1
                if (i-1 > -1) and not(Array[i-1][j]): Array[i-1][j] = Array[i][j] + 1
                if (j+1 < len(Array[0])) and not(Array[i][j+1]): Array[i][j+1] = Array[i][j] + 1
                if (j-1 > -1) and not(Array[i][j-1]): Array[i][j-1] = Array[i][j] + 1

def MakeTreep(Array):
    ListTreep = list()
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            if Array[i][j] == 'b':
                # ListTreep.append() = list(list([i])+list([j]))
                pop = list(['b',[i,j]])
                ListTreep.append(pop)
    Marker = True
    m = 0
    while Marker:
        min = [100, [0,0]]
        fix_i = ListTreep[-1][-1][0]
        # print(fix_i)
        fix_j = ListTreep[-1][-1][1]
        # print(fix_j)
        if (type(Array[fix_i+1][fix_j]) == int) and (Array[fix_i+1][fix_j] < min[0]): 
            min[0] = Array[fix_i+1][fix_j]
            min[1] = [fix_i+1,fix_j]
        if (type(Array[fix_i-1][fix_j]) == int) and (Array[fix_i-1][fix_j] < min[0]): 
            min[0] = Array[fix_i-1][fix_j]
            min[1] = [fix_i-1,fix_j]
        if (type(Array[fix_i][fix_j+1]) == int) and (Array[fix_i][fix_j+1] < min[0]): 
            min[0] = Array[fix_i][fix_j+1]
            min[1] = [fix_i,fix_j+1]
        if (type(Array[fix_i][fix_j-1]) == int) and (Array[fix_i][fix_j-1] < min[0]): 
            min[0] = Array[fix_i][fix_j-1]
            min[1] = [fix_i,fix_j-1]
        # print(min)
        ListTreep.append(min)
        # print(ListTreep)
        if ListTreep[-1][0] == 1: Marker = False
        m = m + 1
    # print(m)
    # print(ListTreep)
    return(ListTreep)
    
contin=0
for i in range(13): SettingTheScales(Place_1)
Treep = MakeTreep(Place_1)
ShowPlace(Place_1, Treep)
PL.show()