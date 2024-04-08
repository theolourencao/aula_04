nome_valido: bool=False
salario_valido: bool=False
porc_valido: bool=False


nome: str
porc:str
salario:str

porc_ajustado:float
salario_ajustado:float

while nome_valido==False:
    nome=input("insira seu nome: ")
    if len(nome)>0:

        if len(nome.split(' '))>1:
            print('Nome Válido')

            nome_valido=True
        
        else:
            print("Digite seu nome completo, não o inicial!")
        
            
    else:
        print("Não deixe o seu nome zerado!!")
        #nome = input("Digite o seu nome completo: ")


    
while salario_valido==False:
    salario=input("Insira seu salário: ")
    try:
        #salario = float(input("Digite a sua remuneração: "))
        salario_ajustado = float(salario)
        if salario_ajustado>0:
            print("Salário maior que zero, não tão pobre assim...")
            salario_valido=True
        else:
            print("Você inseriu um salário negativo ou zerado que isso kkk")
    except:
        print("Você inseriu um valor não numérico no salário")


while porc_valido==False:
    porc=input('Insira seu percentual de bônus: ')
    try:
        #salario = float(input("Digite a sua remuneração: "))
        porc_ajustado = float(porc)
        if porc_ajustado>0:
            print("Salário maior que zero, não tão pobre assim...")
            porc_valido=True
        else:
            print("Você inseriu um salário negativo ou zerado que isso kkk")
    except:
        print("Você inseriu um valor não numérico no salário")


def calcula_bonus(remun, porc_ajustado):
    bonus= 1000+(remun*porc_ajustado/100)
    
    return bonus

print("Saudações meu querido "+nome+ ", o seu bônus foi de "+str(calcula_bonus(salario_ajustado, porc_ajustado)))