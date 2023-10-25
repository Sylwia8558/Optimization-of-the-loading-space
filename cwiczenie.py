import pandas as pd
import random
import obraz
import matplotlib.pyplot as plt
def ukladanie_dlugosc():

    start_length = 0
    start_width = 0
    start_height = 0
    list_random = package.copy()

    while len(list_random) != 0:

        # losowanie paczki do ustawienia
        random_package = losowanie_paczki(list_random)

        end_length = start_length + random_package[0]['length']
        end_width = start_width + random_package[0]['width']
        end_height = start_height + random_package[0]['height']

        # sprawdzenie czy zmiesci sie paczka
        if int(area[0]) - end_length >= 0 and int(area[1]) - end_width >= 0 and int(area[2]) - end_height >= 0:
            #zapisuje punkty zajete przez paczke
            for h in range(start_height, end_height + 1):
                for i in range(start_length, end_length + 1):
                    start_width = 0
                    for j in range(start_width, end_width + 1):
                        occupied.append([i, j, h])

            v[0] = v[0] + random_package[0]['length'] * random_package[0]['width'] * random_package[0]['height']
            edge(start_length, start_width, start_height, end_height, end_length, end_width)
            draw_point.append([start_length, start_width, start_height])
            length_width_number.append([random_package[0]['length'], random_package[0]['width'],
                                        random_package[0]['height'], random_package[0]['package number']])
            start_point.append([start_length, end_width, start_height])

            # dodaje paczke do listy sprawdzajacej
            for k in occupied:
                check_package.append(k)
            occupied.clear()
            arranged.append(random_package[0])
            first_point.append([start_length, start_width, start_height])
            first_point_floor.append([start_length, start_width, end_height])
            start_length = end_length
            i = len(arranged) - 1
            obraz.plot_cuboid(
                [first_point[i][0] + arranged[i]['length'] / 2,
                 first_point[i][1] + arranged[i]['width'] / 2,
                 first_point[i][2] + arranged[i]['height'] / 2], (arranged[i]['length'], arranged[i]['width'],
                                                                    arranged[i]['height']), random_package[0]['package number'])
            list_random.remove(random_package[0])
            package.remove(random_package[0])
            for i in range(2):
                for t in package:
                    if t['package number'] == random_package[0]['package number'] and t['choice'] != \
                            random_package[0]['choice']:
                        package.remove(t)
                        for l in list_random:
                            if l['package number'] == random_package[0]['package number'] and l['choice'] != \
                                    random_package[0]['choice']:
                                list_random.remove(t)

        else:
            list_random.remove(random_package[0])

def ukladanie_szerokosc():
    start_length = 0
    start_width = arranged[0]['width']
    start_height = 0
    list_random = package.copy()
    while len(list_random) != 0:

        # losowanie paczki do ustawienia
        random_package = losowanie_paczki(list_random)

        end_length = start_length + random_package[0]['length']
        end_width = start_width + random_package[0]['width']
        end_height = start_height + random_package[0]['height']

        if int(area[0]) - end_length >= 0 and int(area[1]) - end_width >= 0 and int(area[2]) - end_height >= 0:
            # zapisuje punkty zajete przez paczke
            for h in range(start_height, end_height + 1):
                for i in range(start_width, end_width + 1):
                    start_length = 0
                    for j in range(start_length, end_length + 1):
                        occupied.append([j, i, h])

            sprawdzenie(occupied)

            if len(occupied) != 0:
                edge(start_length, start_width, start_height, end_height, end_length, end_width)
                v[0] = v[0] + random_package[0]['length'] * random_package[0]['width'] * random_package[0]['height']
                draw_point.append([start_length, start_width, start_height])
                length_width_number.append(
                    [random_package[0]['length'], random_package[0]['width'], random_package[0]['package number']])
                start_point_w.append([end_length, start_width, start_height])
                for k in occupied:
                    check_package.append(k)
                occupied.clear()
                arranged.append(random_package[0])
                first_point.append([start_length, start_width, start_height])
                first_point_floor.append([start_length, start_width, end_height])
                i = len(arranged) - 1
                obraz.plot_cuboid(
                    [first_point[i][0] + arranged[i]['length'] / 2,
                     first_point[i][1] + arranged[i]['width'] / 2,
                     first_point[i][2] + arranged[i]['height'] / 2], (arranged[i]['length'], arranged[i]['width'],
                                                                      arranged[i]['height']), random_package[0]['package number'])
                start_width = end_width
                list_random.remove(random_package[0])
                package.remove(random_package[0])
                for i in range(2):
                    for t in package:
                        if t['package number'] == random_package[0]['package number']:
                            package.remove(t)
                            for l in list_random:
                                if l['package number'] == random_package[0]['package number']:
                                    list_random.remove(t)
        else:
            list_random.remove(random_package[0])
            continue


def ukladanie_dlugosc_kolejne():
    len_point = len(start_point)
    while len_point != 0:
        start_length = start_point[0][0]
        start_width = start_point[0][1]
        start_height = start_point[0][2]
        list_random = package.copy()

        while len(list_random) != 0:

            random_package = losowanie_paczki(list_random)

            end_length = start_length + random_package[0]['length']
            end_width = start_width + random_package[0]['width']
            end_height = start_height + random_package[0]['height']

            if int(area[0]) - end_length >= 0 and int(area[1]) - end_width >= 0 and int(area[2] - end_height >= 0):

                for h in range(start_height, end_height + 1):
                    for i in range(start_length, end_length + 1):
                        for j in range(start_width, end_width + 1):
                            occupied.append([i, j, h])
                sprawdzenie(occupied)

                if len(occupied) != 0:
                    edge(start_length, start_width, start_height, end_height, end_length, end_width)
                    v[0] = v[0] + random_package[0]['length'] * random_package[0]['width'] * random_package[0]['height']
                    draw_point.append([start_length, start_width])
                    length_width_number.append([random_package[0]['length'], random_package[0]['width'], random_package[0]['package number']])
                    for k in occupied:
                        check_package.append(k)
                    occupied.clear()
                    start_point.append([start_length, end_width, start_height])
                    arranged.append(random_package[0])
                    first_point.append([start_length, start_width, start_height])
                    first_point_floor.append([start_length, start_width, end_height])
                    start_length = end_length
                    i = len(arranged) - 1
                    obraz.plot_cuboid(
                        [first_point[i][0] + arranged[i]['length'] / 2,
                         first_point[i][1] + arranged[i]['width'] / 2,
                         first_point[i][2] + arranged[i]['height'] / 2], (arranged[i]['length'], arranged[i]['width'],
                                                                          arranged[i]['height']), random_package[0]['package number'])
                    package.remove(random_package[0])
                    list_random.remove(random_package[0])

                    for i in range(2):
                        for t in package:
                            if t['package number'] == random_package[0]['package number'] and t['choice'] != \
                                    random_package[0]['choice']:
                                package.remove(t)
                                for l in list_random:
                                    if l['package number'] == random_package[0]['package number'] and l['choice'] != \
                                            random_package[0]['choice']:
                                        list_random.remove(t)
                else:
                    list_random.remove(random_package[0])
                    continue
            else:
                 list_random.remove(random_package[0])
                 continue

        if len(list_random) == 0:
            del start_point[0]
            len_point = len_point - 1

def ukladanie_szerokosc_kolejne():
    len_point_w = len(start_point_w)

    while len_point_w != 0:
        start_length = start_point_w[0][0]
        start_width = start_point_w[0][1]
        start_height = start_point_w[0][2]
        list_random = package.copy()

        while len(list_random) != 0:

            random_package = losowanie_paczki(list_random)

            end_length = start_length + random_package[0]['length']
            end_width = start_width + random_package[0]['width']
            end_height = start_height + random_package[0]['height']

            if int(area[0]) - end_length >= 0 and int(area[1]) - end_width >= 0 and int(area[2]) - end_height >= 0:

                for h in range(start_height, end_height + 1):
                    for i in range(start_length, end_length + 1):
                        for j in range(start_width, end_width + 1):
                            occupied.append([i, j, h])
                sprawdzenie(occupied)

                if len(occupied) != 0:
                    e = edge(start_length, start_width, start_height, end_height, end_length, end_width)
                    v[0] = v[0] + random_package[0]['length'] * random_package[0]['width'] * random_package[0]['height']
                    draw_point.append([start_length, start_width])
                    length_width_number.append(
                        [random_package[0]['length'], random_package[0]['width'], random_package[0]['package number']])
                    for k in occupied:
                        check_package.append(k)
                    occupied.clear()
                    start_point_w.append([end_length, start_width, start_height])
                    arranged.append(random_package[0])
                    first_point.append([start_length, start_width, start_height])
                    first_point_floor.append([start_length, start_width, end_height])
                    i = len(arranged) - 1

                    obraz.plot_cuboid(
                        [first_point[i][0] + arranged[i]['length'] / 2,
                         first_point[i][1] + arranged[i]['width'] / 2,
                         first_point[i][2] + arranged[i]['height'] / 2], (arranged[i]['length'], arranged[i]['width'],
                                                                          arranged[i]['height']), random_package[0]['package number'])
                    start_width = end_width
                    package.remove(random_package[0])
                    list_random.remove(random_package[0])

                    for i in range(2):
                        for t in package:
                            if t['package number'] == random_package[0]['package number'] and t['choice'] != \
                                    random_package[0]['choice']:

                                package.remove(t)
                                for l in list_random:
                                    if l['package number'] == random_package[0]['package number'] and l['choice'] != \
                                            random_package[0]['choice']:
                                        list_random.remove(t)
                else:
                    list_random.remove(random_package[0])
                    continue

            else:
                 list_random.remove(random_package[0])
                 continue

        if len(list_random) == 0:
            del start_point_w[0]
            len_point_w = len_point_w - 1

def ukladanie_pietro():
    len_first_point = len(first_point_floor)

    while len(first_point_floor) != 0:

        start_length = first_point_floor[0][0]
        start_width = first_point_floor[0][1]
        start_height = first_point_floor[0][2]
        list_random = package.copy()
        while len(list_random) != 0:

            random_package = losowanie_paczki(list_random)

            end_length = start_length + random_package[0]['length']
            end_width = start_width + random_package[0]['width']
            end_height = start_height + random_package[0]['height']

            if int(area[0]) - end_length >= 0 and int(area[1]) - end_width >= 0 and int(area[2]) - end_height >= 0:

                for h in range(start_height, end_height + 1):
                    for i in range(start_length, end_length + 1):
                        for j in range(start_width, end_width + 1):
                            occupied.append([i, j, h])

                sprawdzenie(occupied)
                c = czy_nie_w_powietrzu(start_length, start_width, start_height, end_length, end_width)

                if len(occupied) != 0 and c == 1:
                    e = edge(start_length, start_width, start_height, end_height, end_length, end_width)
                    v[0] = v[0] + random_package[0]['length'] * random_package[0]['width'] * random_package[0]['height']
                    draw_point.append([start_length, start_width])
                    length_width_number.append([random_package[0]['length'], random_package[0]['width'], random_package[0]['package number']])
                    for k in occupied:
                        check_package.append(k)
                    occupied.clear()
                    start_point.append([start_length, end_width, start_height])
                    arranged.append(random_package[0])

                    first_point.append([start_length, start_width, start_height])

                    i = len(arranged) - 1

                    obraz.plot_cuboid_floor(
                        [first_point[i][0] + arranged[i]['length'] / 2,
                         first_point[i][1] + arranged[i]['width'] / 2,
                         first_point[i][2] + arranged[i]['height'] / 2], (arranged[i]['length'], arranged[i]['width'],
                                                                          arranged[i]['height']), random_package[0]['package number'])

                    first_point_floor.append([end_length, start_width, start_height])
                    first_point_floor.append([start_length, end_width, start_height])
                    first_point_floor.append([start_length, start_width, end_height])

                    package.remove(random_package[0])
                    del first_point_floor[0]
                    list_random.remove(random_package[0])

                    for i in range(2):
                        for t in package:
                            if t['package number'] == random_package[0]['package number'] and t['choice'] != \
                                    random_package[0]['choice']:
                                package.remove(t)
                                for l in list_random:
                                    if l['package number'] == random_package[0]['package number'] and l['choice'] != \
                                            random_package[0]['choice']:
                                        list_random.remove(t)
                else:
                    list_random.remove(random_package[0])
                    occupied.clear()
                    continue

            else:
                 list_random.remove(random_package[0])
                 continue

        if len(list_random) == 0:
            del first_point_floor[0]
            len_first_point = len_first_point - 1

def losowanie_paczki(list_random):

    # losowanie paczki do ustawienia
    random_package = random.sample(list_random, 1)
    a = random_package[0]['choice']
    if a == 'width':
        auxiliary = random_package[0]['length']
        random_package[0]['length'] = random_package[0]['width']
        random_package[0]['width'] = auxiliary

    if a == 'height':
        auxiliary = random_package[0]['length']
        random_package[0]['length'] = random_package[0]['height']
        random_package[0]['height'] = auxiliary

    return random_package

def edge(start_length, start_width, start_height, end_height, end_length, end_width):

    for h in range(start_height, end_height + 1):

        for i in range(start_length, end_length + 1):
            o.append([i, start_width, h])
            o.append([i, end_width, h])

        for j in range(start_width + 1, end_width):
            o.append([start_length, j, h])
            o.append([end_length, j, h])

        if h == start_height or h == end_height:
            for i in range(start_length + 1, end_length):
                for j in range(start_width + 1, end_width):
                    o.append([i, j, h])
    return o

def sprawdzenie(occupied):
    for j in check_package:
        for k in occupied:
            if k == j:
                if k not in o:
                    occupied.clear()
                    return

def czy_nie_w_powietrzu(start_length, start_width, start_height, end_length, end_width):
        check = (end_length + 1) * (end_width + 1)
        for i in range(start_length, end_length):
            for j in range(start_width, end_width):
                for ob in o:
                    if [i, j, start_height] == ob:
                        check = check - 1
        if check / ((end_length + 1) * (end_width + 1)) >= 0.2:
            return 1
        else:
            return 0


# wprowadzenie danych powierzchni:
# area = input("Podaj wymiary powierzchni: \n dlugosc, szerokosc, wysokosc \n")
area = '20,30,20'
area = area.split(",")
area = [int(size) for size in area]
obraz.plot_cuboid1([area[0]/2, area[1]/2, area[2]/2], (area[0], area[1], area[2]))

best_arrangement_of_packages = []

# pobranie danych paczek z excela
file_path = "/home/sylwia/program/paczki.xlsx"
text = pd.read_excel(file_path, na_values='n/a')
# dodanie dodakowego klucza do paczek, aby ulozyc paczki (losowanie bez zwracania)
text2 = text.copy()
text3 = text.copy()
text['choice'] = 'length'
text = text.to_dict('records')
text2['choice'] = 'width'
text2 = text2.to_dict('records')
text3['choice'] = 'height'
text3 = text3.to_dict('records')
#lista paczek z wyborem ulozenia
package = []

for d in range(len(text)):
    package.append(text[d])
    package.append(text2[d])
    package.append(text3[d])

#lista paczek z zajętymi punktami
occupied = []
#lista ułożonych paczek
arranged = []
#zajeta objętość
v = [0]
#obwody paczek
o =[]
#lista zajętych punktow przez paczki
check_package = []
# max wartosci punktow paczek
max_point_width = []
max_point_height = []
# pierwszy punkt paczki
first_point = []
#początkowe punkty do ukladania po dlugosci i szerokosci
start_point = []
start_point_w = []
first_point_floor = []
# listy zapisujace punkty do rysowania
draw_point = []
length_width_number = []
#pietro
floor = 0
osobnik =[]

ukladanie_dlugosc()
ukladanie_szerokosc()

for i in range(5):
    ukladanie_dlugosc_kolejne()
    ukladanie_szerokosc_kolejne()
print("Ilość ułożonych paczek stojących na pierwszym piętrze: ", len(arranged))
print("Ułożone paczki stojące na podłożu: ", arranged)
ukladanie_pietro()

for i in range(0, len(text)):
    osobnik.append(0)
    for j in arranged:
        if text[i]['package number'] == j['package number']:
            osobnik[i] = 1
print("Ilość ułożonych paczek w zadanej przestrzeni: ", len(arranged))
print("Ułożone paczki w zadanej przestrzeni: ", arranged)
print("Zajęta objętość przez paczki: ", (v[0] * 100)/(int(area[0]) * int(area[1]) * int(area[2])))
print("Osobnik: ", osobnik)
plt.show()