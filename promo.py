idade = int(input("Qual sua idade?"))
total_compra = float(input("Qual o valor da sua compra?"))

if idade >= 65:
    if total_compra >= 100:
        print("Você irá receber 10% de desconto!")
    else:
        print("Você não irá receber desconto.")
else:
    print("Você está fora da idade para o desconto.")
    