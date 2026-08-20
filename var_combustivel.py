# Autor: Grupo 2
# Projeto: Cálculo Gasolina X Etanol

print("Qual combustivél é mais vantajoso abastecer atualmente")
nome = input("Qual seu nome?")
etanol = float(input("Qual o valor do etanol na sua região atualmente?"))
gasolina = float(input("Qual o valor da gasolina na sua região atualmente?")) 

resultado = etanol/gasolina

if resultado < 0.70 :
       print(f"Vale mais a pena utilizar etanol")

else  :
        print(f"Gasolina é mais vantajoso")

