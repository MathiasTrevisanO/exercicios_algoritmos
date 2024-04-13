from sortedcontainers import SortedDict
import pandas as pd

rb_tree = SortedDict()

file_path = "" #Set any csv file to search a key

# Lê o arquivo CSV
df = pd.read_csv(file_path, sep=";")

# Acessa apenas a primeira coluna do DataFrame
tags = df.iloc[:, 0]

# Itera sobre as tags e adiciona à Red-Black Tree
for tag in tags:
    rb_tree[tag] = tag

# Imprime a Red-Black Tree
# print("Red-Black Tree:")
# for key, value in rb_tree.items():
#     print(key, ":", value)

# Procurando chaves que começam com "PIT"
prefixo = "PIT"
count = 0
print("\nChaves que começam com '{}':".format(prefixo))
for chave in rb_tree.keys():
    if chave.startswith(prefixo):
        print(chave)
        count += 1

# Imprime a quantidade de chaves que começam com "PIT"

print("\nQuantidade de chaves que começam com '{}':".format(prefixo))
print(count)
