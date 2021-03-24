import os
import time
import sys
"""
Format pliku z którego pobierane są dane:
1
2
5
6
4
14

Elementy ciągu odwołań muszą znajdować się pod sobą
"""

class Sym_3(object):
    def __init__(self, data):
        self.data = data

    def read(self):
        """Funkcja  wczyttuje dane z pliku do tablicy"""
        option = input(
            "Jeżeli chcesz dane pobrać z pliku wybierz T a jeśli chcesz wpisać samodzielnie wybierz N!")
        print()

        if option.upper() == "T":
            filename = input(
                "Podaj nazwę pliku, z którego chcesz wczytać dane: ")
            text_file = open(filename, "r")
            lines = text_file.readlines()
            text_file.close()

            length = int(len(lines))

            for i in range(0, length):
                self.data.append(int(lines[i]))

        elif option.lower() == "N":
            number = input("Podaj liczbę procesów która chcesz obslużyc:")
            for i in range(int(number)):
                self.data.append(
                    int(input("Podaj kolejny element ciągu odwołań:")))

        else:
            sys.exit("Nieprawidłowa wartość, podaj 'T' lub 'N'")

    def clear(self):
        name = 'raport_sym2.txt'
        text_write = open(name, "w")
        text_write.close()

    def fifo(self):
        """Funkcja symuluje działania algorytmu FIFO"""
        length = len(self.data)
        temp = []
        fault = 0
        top = 0
        k = 1
        s_fault = 'Tak'
        diff_numb=[]

        for i in range(0, length):
        	if self.data[i] not in diff_numb:
        		diff_numb.append(self.data[i])

        name = 'raport_sym2.txt'
        text_write = open(name, "a")
        n = int(input("Podaj wielkość kolejki:"))
        if n > length:
            print("wielkość kolejki większa jest  od iloścu podanych danych, proszę podac więcej danych bądź zmniejszyć wielkość kolejki")
            exit()
        if n>len(diff_numb):
        	print(f"Podane n równa się {n} a maksymalna liczba stron podanych w danych wejsciowych to {len(diff_numb)} więc n przyjmie wartość {len(diff_numb)} ")
        	n=len(diff_numb)
        speed = input("Podaj współczynnik prędkości symulacji")
        print()
        print(f"Elementy ciągu odwołań: {self.data}")
        print()
       	tab1=(n-3)*str("\t")
       	if n==2:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t{tab1}Zmiana:")
        elif n==1:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t{tab1}Zmiana:")
        else:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t\t{tab1}Zmiana:")
        print()
        text = str("\t\tAlgorytm\t\t FIFO\n\n")
        text_write.writelines(text)
        text = str(f"Krok:\t\tStrony w przetwarzaniu:\t\tZmiana: \n")
        text_write.writelines(text)

        for i in self.data:
            if i not in temp:
                if len(temp) < n:
                    temp.append(i)
                else:
                    temp[top] = i
                    top = (top+1) % n
                fault += 1
                s_fault = 'Tak'
            else:
                s_fault = 'Nie'
            if k < 10:
                print(f"krok {k}: ", end="\t")
                text = str(f"krok {k}:  \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            else:
                print(f"krok {k}: ", end="\t")
                text = str(f"krok {k}: \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            k += 1
            for j in temp:
                print(j, end="\t")
                time.sleep(1 / int(speed))
                text = str(f"{j} ")
                text_t = text.replace("\n", '  ')
                text_write.writelines(text_t)

            for j in range(n-len(temp)):
                print(" ", end="\t")
                time.sleep(1 / int(speed))
                text = str("  ")
                text_t = text.replace("\n", ' ')
                text_write.writelines(text_t)
            
            print("\t", end="\t")
            if n<=3:
            	text = str("\t\t\t")
            else:
            	text = str("\t\t")
            text_t = text.replace("\n", '')
            text_write.writelines(text_t)
            print(f" {s_fault}")
            text = str(f" {s_fault}")
            text_write.writelines(text)
            print()
            text = str("\n")
            text_write.writelines(text)

        average_fault = 100*(fault/len(self.data))
        print(
            f"Zamiana stron wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron")
        text = str(
            f"Zamiana stron wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron")
        text_write.writelines(text)
        text = str("\n\n\n")
        text_write.writelines(text)
        text_write.close()

    def lru(self):
        """Funkcja symuluje działania algorytmu LRU"""
        length = len(self.data)
        temp = []
        fault = 0
        top = 0
        k = 1
        o = 1
        old_page = []
        s_fault = 'Tak'
        diff_numb=[]

        for i in range(0, length):
        	if self.data[i] not in diff_numb:
        		diff_numb.append(self.data[i])

        name = 'raport_sym2.txt'
        text_write = open(name, "a")

        n = int(input("Podaj wielkość kolejki:"))
        if n > length:
            print("wielkość kolejki większa jest  od iloścu podanych danych, proszę podac więcej danych bądź zmniejszyć wielkość kolejki")
            exit()
        if n>len(diff_numb):
        	print(f"Podane n równa się {n} a maksymalna liczba stron podanych w danych wejsciowych to {len(diff_numb)} więc n przyjmie wartość {len(diff_numb)} ")
        	n=len(diff_numb)
        speed = input("Podaj współczynnik prędkości symulacji")
        print()
        print(f"Elementy ciągu odwołań: {self.data}")
        print()
        tab1=(n-3)*str("\t")
       	if n==2:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t{tab1}Zmiana:")
        elif n==1:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t{tab1}Zmiana:")
        else:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t\t{tab1}Zmiana:")
        print()
        text = str("\t\tAlgorytm\t\t LRU\n\n")
        text_write.writelines(text)
        text = str(f"Krok:\t\tStrony w przetwarzaniu:\t\tZmiana: \n")
        text_write.writelines(text)

        for i in self.data:
            if i not in temp:
                if len(temp) < n:
                    temp.append(i)
                    old_page.append(o)
                    o += 1
                    s_fault = 'Tak'

                else:
                    ix = old_page.index(min(old_page))
                    old_page[ix] = o
                    temp[ix] = i
                    o += 1
                    s_fault = 'Tak'

                fault += 1

            else:

                ix = old_page.index(min(old_page))
                if i == self.data[ix]:
                    old_page[ix] = o
                    o += 1
                else:
                    ind = temp.index(i)
                    old_page[ind] = o
                    o += 1
                s_fault = 'Nie'

            if k < 10:
                print(f"krok {k}: ", end='\t')
                text = str(f"krok {k}:  \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            else:
                print(f"krok {k}: ", end='\t')
                text = str(f"krok {k}: \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            k += 1
            for j in temp:
                print(j, end="\t")
                time.sleep(1 / int(speed))
                text = str(f"{j} ")
                text_t = text.replace("\n", '  ')
                text_write.writelines(text_t)

            for j in range(n-len(temp)):
                print(" ", end="\t")
                time.sleep(1 / int(speed))
                text = str("  ")
                text_t = text.replace("\n", ' ')
                text_write.writelines(text_t)

            print("\t", end="\t")
            if n<=3:
            	text = str("\t\t\t")
            else:
            	text = str("\t\t")
            text_t = text.replace("\n", '')
            text_write.writelines(text_t)
            print(f" {s_fault}")
            text = str(f" {s_fault}")
            text_write.writelines(text)
            print()
            text = str("\n")
            text_write.writelines(text)

        print()
        average_fault = 100*(fault/len(self.data))
        print(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron")
        text = str(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron\n")
        text_write.writelines(text)
        text = str("\n\n\n")
        text_write.writelines(text)
        text_write.close()

    def opt(self):
        temp = []
        length = int(len(self.data))
        count = 1
        fault = 0
        s_fault = 'Tak'
        diff_numb=[]

        for i in range(0, length):
        	if self.data[i] not in diff_numb:
        		diff_numb.append(self.data[i])

        name = 'raport_sym2.txt'
        text_write = open(name, "a")
        n = int(input("Podaj wielkość kolejki:"))
        speed = input("Podaj współczynnik prędkości symulacji")
        if n > length:
            print("wielkość kolejki większa jest  od iloścu podanych danych, proszę podac więcej danych bądź zmniejszyć wielkość kolejki")
            exit()
        if n>int(len(diff_numb)):
        	print(f"Podane n równa się {n} a maksymalna liczba stron podanych w danych wejsciowych to {len(diff_numb)} więc n przyjmie wartość {len(diff_numb)} ")
        	n=int(len(diff_numb))
        p_count = [None for i in range(n)]
        print(f"Elementy ciągu odwołań: {self.data}")
        print()
        tab1=(n-3)*str("\t")
       	if n==2:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t{tab1}Zmiana:")
        elif n==1:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t{tab1}Zmiana:")
        else:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t\t{tab1}Zmiana:")
        print()
        text = str("\t\tAlgorytm\t\t OPT\n\n")
        text_write.writelines(text)
        text = str(f"Krok:\t\tStrony w przetwarzaniu:\t\tZmiana: \n")
        text_write.writelines(text)
        print()
        for i in range(length):
            if count < 10:
                print(f"Krok {count}:  ", end="\t")
                text = str(f"krok {count}:  \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)
            else:
                print(f"Krok {count}: ", end="\t")
                text = str(f"krok {count}: \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)
            count += 1
            if self.data[i] not in temp:
                fault += 1
                if len(temp) < n:
                    temp.append(self.data[i])
                else:
                    for j in range(len(temp)):
                        if temp[j] not in self.data[i + 1:]:
                            temp[j] = self.data[i]
                            break
                        else:
                            p_count[j] = self.data[i + 1:].index(temp[j])
                    else:
                        temp[p_count.index(max(p_count))] = self.data[i]
                s_fault = 'Tak'
            else:
                s_fault = 'Nie'

            for j in temp:
                print(j, end="\t")
                time.sleep(1 / int(speed))
                text = str(f"{j} ")
                text_t = text.replace("\n", '  ')
                text_write.writelines(text_t)

            for j in range(n-len(temp)):
                print(" ", end="\t")
                time.sleep(1 / int(speed))
                text = str("  ")
                text_t = text.replace("\n", ' ')
                text_write.writelines(text_t)

            print("\t", end="\t")
            if n<=3:
            	text = str("\t\t\t")
            else:
            	text = str("\t\t")
            text_t = text.replace("\n", '')
            text_write.writelines(text_t)
            print(f" {s_fault}")
            text = str(f" {s_fault}")
            text_write.writelines(text)
            print()
            text = str("\n")
            text_write.writelines(text)


        print()
        average_fault = 100*(fault/len(self.data))
        print(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron")
        text = str(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron\n")
        text_write.writelines(text)
        text = str("\n\n\n")
        text_write.writelines(text)
        text_write.close()

    def lfu(self):
        """Funkcja symuluje działania algorytmu LRU"""
        temp = []
        length = len(self.data)
        c = 0
        k = 0
        b = 0
        fault = 0
        s_fault = 'Tak'
        count = 0
        diff_numb=[]

        for i in range(0, length):
        	if self.data[i] not in diff_numb:
        		diff_numb.append(self.data[i])

        name = 'raport_sym2.txt'
        text_write = open(name, "a")

        n = int(input("Podaj wielkość kolejki:"))
        if n > length:
            print("wielkość kolejki większa jest  od iloścu podanych danych, proszę podac więcej danych bądź zmniejszyć wielkość kolejki")
            exit()
        if n>len(diff_numb):
        	print(f"Podane n równa się {n} a maksymalna liczba stron podanych w danych wejsciowych to {len(diff_numb)} więc n przyjmie wartość {len(diff_numb)} ")
        	n=len(diff_numb)
        memory = [0 for i in range(n)]
        position = [0 for i in range(n)]
        memory_time = [0 for i in range(n)]
        speed = input("Podaj współczynnik prędkości symulacji")
        print()
        print(f"Elementy ciągu odwołań: {self.data}")
        print()
        tab1=(n-3)*str("\t")
       	if n==2:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t{tab1}Zmiana:")
        elif n==1:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t{tab1}Zmiana:")
        else:
        	print(f"Krok:\t\tStrony w przetwarzaniu:\t\t\t{tab1}Zmiana:")
        print()
        text = str("\t\tAlgorytm\t\t LFU\n\n")
        text_write.writelines(text)
        text = str(f"Krok:\t\tStrony w przetwarzaniu:\t\tZmiana: \n")
        text_write.writelines(text)
        for i in self.data:
            numb = 0
            var = 0

            if i not in temp:
                # lista tymczasowa do prechowywania czy na danej pozycji znajduje się wartość min memory
                example = [0 for k in range(n)]
                mem_min_index = memory.index(min(memory))
                p_min = min(position)  # przechowuje min wartość listy position
                f = position.index(min(position))
                # przechowuje minimalną wartość z listy m_memory
                m_memory = min(memory)
                for j in range(n):
                    if memory[j] == m_memory:
                        example[j] = 1
                for j in range(n):
                    if example[j] == 1 and position[j] == p_min:
                        var = j
                        break
                    else:
                        var = mem_min_index

                if len(temp) < n:
                    temp.append(i)
                    memory[c] = 1
                    position[c] = 1
                    c += 1
                    s_fault = 'Tak'
                    fault += 1
                else:
                    temp[var] = i
                    for j in range(0, b + 1):
                        if self.data[j] == i:
                            numb += 1
                    memory[var] = numb
                    position[var] += 1
                    s_fault = 'Tak'
                    fault += 1

            else:
                ind = temp.index(i)

                for j in range(0, b + 1):
                    if self.data[j] == i:
                        numb += 1

                memory[ind] = numb
                position[ind] += 1
                s_fault = 'Nie'

            b += 1

            if k < 10:
                print(f"krok {k+1}: ", end='\t')
                text = str(f"krok {k+1}:  \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            else:
                print(f"krok {k+1}: ", end='\t')
                text = str(f"krok {k+1}: \t\t")
                text_t = text.replace("\n", '')
                text_write.writelines(text_t)

            for j in temp:
                print(j, end="\t")
                time.sleep(1 / int(speed))
                text = str(f"{j} ")
                text_t = text.replace("\n", '  ')
                text_write.writelines(text_t)

            for j in range(n-len(temp)):
                print(" ", end="\t")
                time.sleep(1 / int(speed))
                text = str("  ")
                text_t = text.replace("\n", ' ')
                text_write.writelines(text_t)
                
            print("\t", end="\t")
            if n<=3:
            	text = str("\t\t\t")
            else:
            	text = str("\t\t")
            text_t = text.replace("\n", '')
            text_write.writelines(text_t)
            print(f" {s_fault}")
            text = str(f" {s_fault}")
            text_write.writelines(text)
            print()
            text = str("\n")
            text_write.writelines(text)
            k+=1
        print()
        average_fault = 100*(fault/len(self.data))
        print(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron")
        text = str(
            f"Zamiana wystąpiła {fault} razy, co stanowi {round(average_fault,2)}% wszystkich stron\n")

        text_write.writelines(text)
        text = str("\n\n\n")
        text_write.writelines(text)
        text_write.close()


data = []
xd = Sym_3(data)
xd.read()
xd.clear()
decision = True


"""------------------------------------------------------MENU--------------------------------------------------------"""
"""Wszystkie algorytmy testowane są na tych samych danych wejściowych aby była możliwość łatwego porówywania działania"""

while decision:
    option = input(
        "Podaj nazwę algorytmu który chcesz przetestować(dostępne algorytmy:fifo, lru, opt, lfu, jeśli chcesz wyjść wpisz 'exit' ")
    if option.lower() == 'fifo':
        xd.fifo()
    elif option.lower() == 'lru':
        xd.lru()
    elif option.lower() == 'opt':
        xd.opt()
    elif option.lower() == 'lfu':
        xd.lfu()
    elif option.lower() == 'exit':
        decision = False
    else:
        sys.exit(
            "Podano nieprawidłową opcję! Dozwolone są opcje fifo, lru, opt, lfu, exit")
