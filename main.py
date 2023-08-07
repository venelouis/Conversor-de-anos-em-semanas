# Weeks in Years (Semanas em Anos)!

''''
Um programa que converte número de anos em semanas, por exemplo:
se o "input" for 2, então o output(saída) deve ser 52 = 104,
porque temos 52 semanas em 1 ano.
'''

print("\nConversor de anos em semanas.\n")
years = input('Digite o número de anos: ')
# precisamos mudar o "type" (converter) para calcular corretamente o valor do "input" para "int" ou não.
weeks = 52 * int(years)
# para imprimir ("printar") corretamente o resultado (que é = int) com uma mensagem (que é uma string) precisamos converter o resultado novamente em string, como pode ser visto abaixo:
#print(type(weeks))
#print(type(years))
# Então para imprimir corretamente este é o código:
print("Existem "+str(weeks)+ " semanas em: "+years+ " anos.")

