from src.classes.Cidade import Cidade
import json

sair = False

arquivo = open("./src/bd/bd.json", 'r') 
lista_cidades = json.loads(arquivo.read())
arquivo.closer()

while sair == False:

    nome_cidade = input("Digite o nome da cidade:")
    populacao_cidade = int(input("Digite a população da cidade:"))
    sigla_estado = input("Digite a sigla do estado:")
    nome_estado = input("Digite o nome do estado")

    uf = {"sigla": sigla_estado, "nome": nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade,uf)

lista_cidades.append(nova_cidade)
 
resposta =  input('Deseja cadastrar outra cidade?')
   
if resposta.upper () == "N":
         sair = True

arquivo = open ("./src/bd/bd.json", 'w')
arquivo.write(json.dumps(lista_cidades))
