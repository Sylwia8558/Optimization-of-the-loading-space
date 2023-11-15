  Program został napisany strukturalnie w języku Python. Stosując działanie algorytmu genetycznego maksymalizuje zajętą przestrzeń ładowni przez zadane paczki. Uzyskane wyniki zostały przedstawione na wykresie z wykorzystaniem bibliotek numpy oraz matplotlib, natomiast w konsoli zwracana jest informacja o ułożonych oraz nieułożonych paczkach. 
  
#Przyjęte założenia programu:
  •Przestrzeń załadunku to nieobracalny prostopadłościan o wymiarach (długość,
    szerokość, wysokość)
  •Paczki to prostopadłościany o wymiarach (długość, szerokość, wysokość)
  •Każda paczka jest obracalna, można je układać na każdym boku
  •Nie uwzględniono aspektu wagi (problemu plecakowego) paczek
  •Nie wzięto pod uwagę błędu pomiaru paczek oraz ładowni

#Zobrazowanie pojęć algorytmu w programie:
  W programie podstawowe pojęcia danego algorytmu przedstawiono w następujący sposób:
Osobnik – paczki, które są układane w przestrzeni ładunkowej
Populacja – sposoby ułożenia paczek w przestrzeni ładunkowej
Chromosom – paczka
Gen – cecha paczki: długość, szerokość, wysokość
Allel – wartość cechy: długość, szerokość, wysokość


#Wprowadzanie danych:

Przed uruchomieniem programu użytkownik w załączonym pliku Excel wprowadza informacje o paczkach wpisując długość, szerokość oraz wysokość w odpowiednich miejscach tabeli. Dane te zostają przeniesione do programu. Po uruchomieniu programu użytkownik w konsoli po otrzymaniu polecenia wprowadza wymiary powierzchni załadunkowej odpowiednio: długość, szerokość, wysokość. Użytkownik musi pamiętać o wprowadzaniu danych wymiarów do programu w tych samych jednostkach.

