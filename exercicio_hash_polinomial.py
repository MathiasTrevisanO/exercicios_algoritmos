import random

def polynomial_hash(tag_name, coefficients, m):
    n = len(tag_name)
    hash_value = 0
    for i in range(n):
        # Use o operador de módulo para garantir que o índice dos coeficientes seja válido
        coef_idx = i % len(coefficients)
        hash_value += coefficients[coef_idx] * (ord(tag_name[i]) ** i)
    return hash_value % m

tag_names = ["PSLLL-3123219", "PSLL-3123219", "PSL-3123219", "PSH-3123219", "PSHH-3123219", "PSHHH-3123219"]

# Escolha de coeficientes primos
coefficients = [2, 3, 5, 7, 11, 13]

# Tamanho da tabela de hash
table_size = 30

hash_table = [None] * table_size

for tag in tag_names:
    hash_value = polynomial_hash(tag, coefficients, table_size)
    if hash_table[hash_value] is None:
        hash_table[hash_value] = tag
    else:
        print(f"Colisão detectada para a tag '{tag}' no índice {hash_value}")
        
print("\nTabela Hash Resultante:")
for i in range(table_size):
    print(f"Índice {i}: {hash_table[i]}")
