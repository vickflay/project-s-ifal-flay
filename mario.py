def linha():
    x=int(input("Numero da linha? "))
    print("🟥" * x)
    x -=1

def pilar():
    x=int(input("Numero do pilar? "))
    while x>0:
        print("🟨")
        x-=1

def cubo():
    x=int(input("Numero do cubo? "))
    y=x
    while x>0:
        print("🟩" * x)
        x-=1

escolha =input("escolha:linha, pilar, cubo:")
if escolha== "linha":
    linha()

elif escolha== "pilar":
    pilar()
elif escolha== "cubo":
    cubo()

else :
    print("Nao encontrado...")

