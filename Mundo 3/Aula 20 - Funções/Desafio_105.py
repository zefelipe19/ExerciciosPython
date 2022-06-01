'''Exercício Python 105: Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
import re


print(f"{' DESAFIO 105':=^100}")

def notas(*num, sit=False):
    '''Parâmetro: num, é\são as notas a serem calculadas;
    sit: 'sit' é o parâmetro que deve ser adcionado caso deseje ver a situação
    return: é o resultado que se tem quando chama a função notas
    '''
    n = {}
    med = sum(num) / len(num)
    n["Total"] = len(num)
    n["Maior Nota"] = max(num)
    n["Menor Nota"] = min(num)
    n["Média"] = f"{med:.2f}"
    if sit==True:
        if med >= 7:
            n["Situação"] = "BOA"
        elif med >= 5:
            n["Situação"] = "RAZOÁVEL"
        else:
            n["Situação"] = "RUIM"
    return n    
 
 
print(notas(5, 7.8, 9, 10, 2.3, 0, sit=True))
help(notas)

print("="*100)
