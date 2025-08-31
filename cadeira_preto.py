#Um cabeçalho de arquivo é um bloco no início do código que serve para descrever metadados sobre o arquivo.
#Serve como um guia rápido para o desenvolvedor entender o contexto do arquivo antes de ler o código
# ====================================================
# Arquivo: cadeira_preto.py
# Autor: Vitor Calliari
# Data: 25/08/2025
# Descrição: Arquivo criado em sala de aula para atividade.
# ====================================================
"""
Uma docstring documenta módulos, classes, funções e métodos dentro do código e faz parte da documentação oficial do código.
Pode ser utiliza em tempo de execução através do comando help().
Documenta o código para facilitar o entendimento de outros desenvolvedores
"""

"""
A diferença entre docstrings e o cabeçalho do arquivo é que o cabeçalho do arquivo é um comentário simples
feito com # com informações básicas do projeto, porém não é lido pelo Python.
Já o Docstring é uma string especial que é interpretada pelo Python e pode ser utilizada ativamente
com comandos dentro do código.
"""


# Segue atividade, implemente os métodos abaixo:

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    maior = nums[0]
    for n in nums[1:]:
        if n > maior:
            maior = n
    return maior


def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    return n % 2 == 0
  

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    if n < 0:
        raise ValueError("Não é possível calcular o fatorial")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

