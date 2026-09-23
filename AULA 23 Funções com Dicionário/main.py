personagens = []

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe = input("Digite a classe do seu personagem: ")
    nível = int(input("Digite o nível do seu personagem: "))
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "nível": nível
    }
    personagens.append(personagem)  
    
    print("PERSONAGEM CRIADO")
    print("Nome : ", personagem["nome"])
    print("Classe : ", personagem["classe"])
    print("Nível : ", personagem["nível"])
    

criar_personagem()
criar_personagem()
criar_personagem()