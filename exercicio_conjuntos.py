A = {1,2,3,4,5,6,7,8,9}
B = {1,2,3,4,5,6,7,8,9,10,11,12}


uniao = A.union(B)
print(uniao)

intersecao = A.intersection(B)
print(intersecao)

diferenca = B.difference(A)
print(diferenca)

dif_simetrica = B.symmetric_difference(A)
print(dif_simetrica)


quadrados = {x**2 for x in range(10)}

print(quadrados)

imutavel = frozenset([1,2,3])

print(imutavel)