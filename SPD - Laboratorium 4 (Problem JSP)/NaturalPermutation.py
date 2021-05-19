from Generator import RandomNumberGenerator
import copy
import math

class NaturalPermutation:
    def __init__(self, seed, n, m):  
        #Zrodlo losowania
        self.seed = seed
        #Liczba zadan
        self.n = n
        #Liczba maszyn
        self.m = m
        #Czas wykonania i-tej operacji w zadaniu j-tym
        self.p = []
        #Maszyna na której ma wykonywać się i-ta operacja w zadaniu j-tym
        self.u = []
        #Ilość operacji dla danego zadania
        self.O = []
        #Kolejność wykonywania zadań
        self.Pi = []
        #Inicjalizacja obiektu
        rng = RandomNumberGenerator(seed)    

        #Inicjalizacja kolejnosci
        for i in range(1, self.n+1):
            o = rng.nextInt(1, math.floor(m*1.2)) + 1
            self.O.append(o)
            tmp1 = []
            for j in range(1, o+1):
                tmp1.append(rng.nextInt(1, 29))
            self.p.append(copy.deepcopy(tmp1))

        for i in range(0, self.n):
            tmp2 = []
            for j in range(1, self.O[i]+1):
                tmp2.append(rng.nextInt(1, m))
            self.u.append(copy.deepcopy(tmp2))

        z = 0;
        for i in range(1, self.m+1):
            tmp3 = []
            for j in range(0, self.n):
                for k in self.u[j]: 
                    if(k == i):
                        z = z + 1
                        tmp3.append(z)
                        break
            self.Pi.append(tmp3);


    def __str__(self):
        str1 = "=======================================================================\n"
        return str1 + "p: " + str(self.p) + "\n" + str1 + "u: " + str(self.u) + "\n" + str1 + "Pi: " + str(self.Pi) + "\n" + str1