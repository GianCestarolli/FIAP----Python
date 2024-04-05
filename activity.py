time = int(input("Que horas são?  "))
temp = int(input("Qual a temperatura?  "))

if 6<= time < 12:
    if temp >= 22:
        print("Dar uma caminhada no parque.")
    else:
        print("Ficar em casa estudando.")
if 12 <= time < 18:
    if temp >= 22:
        print("Jogar bola.")
    else:
        print("Jogar videogame.")
if time >= 18:
    print("Hora de se preparar para dormir.")
