# 🐍 Fundamentos de Python

Repositório criado para estudar os principais conceitos iniciais da linguagem **Python**, começando por variáveis e saída de dados até estruturas condicionais.

## 📚 Conteúdos

* [Variáveis](#-variáveis)
* [Print](#-print)
* [F-String](#-f-string)
* [If](#-if)
* [Elif](#-elif)
* [Else](#-else)
* [Exemplo completo](#-exemplo-completo)
* [Conclusão](#-conclusão)

---

## 📦 Variáveis

Uma **variável** é utilizada para armazenar um valor na memória do programa.

Em Python, não é necessário declarar previamente o tipo da variável. Basta criar um nome e atribuir um valor utilizando `=`.

### Exemplo

```python
nome = "Geovanna"
idade = 15
altura = 1.65
estudante = True
```

Nesse exemplo:

| Variável    | Valor        | Tipo    |
| ----------- | ------------ | ------- |
| `nome`      | `"Geovanna"` | `str`   |
| `idade`     | `15`         | `int`   |
| `altura`    | `1.65`       | `float` |
| `estudante` | `True`       | `bool`  |

### Principais tipos

```python
nome = "Geovanna"      # str
idade = 15             # int
altura = 1.65          # float
estudante = True       # bool
```

Para descobrir o tipo de uma variável, podemos utilizar `type()`:

```python
idade = 15

print(type(idade))
```

Resultado:

```text
<class 'int'>
```

---

## 🖨️ Print

A função `print()` é utilizada para **exibir informações no console**.

### Exibindo um texto

```python
print("Olá, mundo!")
```

### Exibindo uma variável

```python
nome = "Geovanna"

print(nome)
```

Resultado:

```text
Geovanna
```

### Exibindo várias informações

```python
nome = "Geovanna"
idade = 15

print(nome, idade)
```

Resultado:

```text
Geovanna 15
```

O `print()` é muito utilizado para mostrar resultados e acompanhar o funcionamento de um programa.

---

## 🧵 F-String

As **f-strings** facilitam a inserção de variáveis dentro de textos.

Para utilizar uma f-string, colocamos a letra `f` antes das aspas e usamos `{}` para inserir as variáveis.

### Exemplo

```python
nome = "Geovanna"
idade = 15

print(f"Meu nome é {nome} e eu tenho {idade} anos.")
```

Resultado:

```text
Meu nome é Geovanna e eu tenho 15 anos.
```

### Por que usar f-string?

Sem f-string:

```python
print("Meu nome é", nome, "e eu tenho", idade, "anos.")
```

Com f-string:

```python
print(f"Meu nome é {nome} e eu tenho {idade} anos.")
```

A f-string deixa o código **mais organizado, legível e fácil de escrever**.

---

# 🔀 Estruturas Condicionais

As estruturas `if`, `elif` e `else` permitem que o programa **tome decisões** de acordo com determinadas condições.

---

## 🟢 If

`if` significa **"se"**.

Ele executa um bloco de código somente quando uma condição é verdadeira.

### Exemplo

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

Como `idade` é 18, a condição `idade >= 18` é verdadeira e o programa executa o `print()`.

### Operadores de comparação

| Operador | Significado    |
| -------- | -------------- |
| `==`     | igual          |
| `!=`     | diferente      |
| `>`      | maior que      |
| `<`      | menor que      |
| `>=`     | maior ou igual |
| `<=`     | menor ou igual |

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

---

## 🟡 Elif

`elif` significa **"senão, se"**.

Ele permite verificar outra condição caso o `if` anterior seja falso.

### Exemplo

```python
nota = 7

if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprovado!")
```

Como a nota é `7`, a primeira condição é falsa e a condição do `elif` é verdadeira.

Resultado:

```text
Aprovado!
```

Podemos utilizar vários `elif`:

```python
nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muito bom")
elif nota >= 5:
    print("Regular")
```

---

## 🔴 Else

`else` significa **"senão"**.

Ele é executado quando nenhuma das condições anteriores é verdadeira.

### Exemplo

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Resultado:

```text
Menor de idade
```

O `else` não possui uma condição própria. Ele funciona como uma alternativa caso o `if` seja falso.

---

# 🧩 If + Elif + Else

Podemos utilizar os três juntos para criar decisões mais completas.

### Exemplo

```python
nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
```

O programa funciona da seguinte maneira:

```text
       nota >= 9?
          ↓
      ┌── SIM ──→ Excelente!
      │
      NÃO
      ↓
    nota >= 6?
      ↓
  ┌── SIM ──→ Aprovado!
  │
  NÃO
  ↓
Reprovado!
```

---

# 💻 Exemplo Completo

Aqui temos um pequeno programa utilizando **variáveis, f-string, print, if, elif e else**:

```python
nome = "Geovanna"
nota = 8

print(f"Olá, {nome}!")

if nota >= 9:
    print(f"{nome}, você teve um excelente resultado!")
elif nota >= 6:
    print(f"{nome}, você foi aprovada!")
else:
    print(f"{nome}, você precisa estudar mais.")
```

### Resultado

```text
Olá, Geovanna!
Geovanna, você foi aprovada!
```

---

# 🧠 Resumo

```python
# Variáveis
nome = "Geovanna"
idade = 15

# Print
print(nome)

# F-string
print(f"Meu nome é {nome}")

# If
if idade >= 18:
    print("Maior de idade")

# Elif
elif idade >= 13:
    print("Adolescente")

# Else
else:
    print("Criança")
```

### Em resumo:

* **Variáveis** → armazenam informações.
* **`print()`** → exibe informações na tela.
* **F-string** → permite colocar variáveis dentro de textos de maneira simples.
* **`if`** → verifica uma condição.
* **`elif`** → verifica uma nova condição caso a anterior seja falsa.
* **`else`** → executa quando nenhuma condição anterior foi atendida.

---

## 🚀 Próximos passos

Depois de dominar esses conceitos, os próximos assuntos recomendados são:

1. Entrada de dados com `input()`
2. Conversão de tipos (`int`, `float`, `str`)
3. Operadores matemáticos
4. Operadores lógicos (`and`, `or`, `not`)
5. Estruturas de repetição (`for` e `while`)
6. Listas
7. Tuplas
8. Dicionários
9. Funções
10. Projetos práticos

---

## 📌 Objetivo

Este README faz parte dos estudos de **Python para iniciantes**, servindo como material de consulta e prática dos principais fundamentos da linguagem.

> **Aprender programação é praticar. Leia o conceito, escreva o código e tente modificar os exemplos para entender como eles funcionam.** 🐍💻
