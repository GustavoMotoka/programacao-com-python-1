def somar(a: int ,b: int) -> int:
    '''
    Função para somar dois números 
    '''
    return a + b
print(somar(2, 2))
print(somar("Olá", "Mundo"))
# O Type Hint não impede a string de passar
# Mas ajuda na organização
help(somar)
print(somar.__doc__)