import random

pozitiv = []
negativ = []
szamok = [random.randint(-51, 51) for i in range(101)]

for i in szamok:
    if i < 0:
        negativ.append(i)
    else:
        pozitiv.append(i)