# Autor: Geovanna
# Projeto : Lista de Pizzaria

print("Pizzaria Mamamia")
nome =input(print(f"Qual é seu nome?"))
cardapio = ["Pizzaiolo", "Muçarela", "Calabresa", "Portuguesa"]
pergunta = input(" Deseja mais algo?")

resposta= input(f"Boa noite, {nome}. Este é nosso cardapio: {cardapio}")
pedido = [input("Insira seu pedido:")]

while pergunta != "não":
     cardapio = ["Pizzaiolo", "Muçarela", "Calabresa", "Portuguesa"]
     print (cardapio)
     pedido.append = [input("Insira seu pedido:")]
     pergunta = input(" Deseja mais algo?")

print (f"{nome}, seu pedido é: {pedido}")