tekst = input("Wpisz tekst: ")

tekst = tekst.split()
tabela = {}

for i in set(tekst):
    tabela[i] = tekst.count(i)

print(tabela) 