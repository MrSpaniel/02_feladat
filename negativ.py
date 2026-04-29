import random

pozitiv = []
negativ = []
szamok = [random.randint(-50, 50) for i in range(100)]

for i in szamok:
    if i < 0:
        negativ.append(i)
    else:
        pozitiv.append(i)

y = len(negativ)

print(f'A generált számok között {y} negatív szerepelt.')