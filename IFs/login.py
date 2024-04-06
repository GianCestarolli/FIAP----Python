user = input("Digite seu nome de usuário:  ")
user = user.title()

if user == "Admin":
    password = input("Digite sua senha:  ")
    if password == "senha123":
        code = int(input("Digite o código de verificação:  "))
        if code == 1909:
            print("Bem-vindo Admin")
        else:
            print("Código incorreto!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário incorreto!")
