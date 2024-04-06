age = int(input("Quando seu carro foi fabricado?  "))
brand = input("Qual a marca do carro?  ")
brand = brand.title()

if brand == "Volvo":
    if 2013 <= age <= 2015:
        print("Seu carro é um Volvo e foi fabricado entre 2013 e 2015")
    elif age < 2013:
        print("Seu carro é um Volvo e foi fabricado antes de 2013")
    else:
        print("Seu carro é um Volvo e foi fabricado depois de 2015")
else:
    print("Seu carro não é um Volvo")

    
