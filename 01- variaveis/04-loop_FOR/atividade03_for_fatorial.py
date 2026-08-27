# Autor: Geovanna Carolaine
# Projeto: Fatorial

numero = int(input(f"Digite o fatorial desejado: "))
fatorial = 1

for i in range (1,numero +1):
   fatorial=fatorial*i

print(f"O fatorial do numero {numero} é {fatorial}")
    