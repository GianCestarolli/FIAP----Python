cores = ["Azul", "Verde", "Vermelho"]

r = input("Digite uma cor: ").title()

if r in cores:
    print(f"{r} está na lista !")
else:
    print(f"{r} não está na lista")
