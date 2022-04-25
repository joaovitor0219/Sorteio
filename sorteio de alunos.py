import random
aluno1 = input("Nome do aluno: ")
aluno2 = input("Nome do aluno: ")
aluno3 = input("Nome do aluno: ")
aluno4 = input("Nome do aluno: ")
sorteio = random.randint(1,4)

if sorteio == 1:
    print(f"O aluno {aluno1} apagará o quadro!")

elif sorteio == 2:
    print(f"O aluno {aluno2} apagará o quadro!")

elif sorteio == 3:
    print(f"O aluno {aluno3} apagará o quadro!")

elif sorteio == 4:
    print(f"O aluno {aluno4} apagará o quadro!")
