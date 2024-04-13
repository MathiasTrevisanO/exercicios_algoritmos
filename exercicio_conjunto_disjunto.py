def disjoint_set(list1, list2):
    # Convertendo as listas em conjuntos
    set1 = set(list1)
    set2 = set(list2)
    
    # Encontrando elementos disjuntos usando a função difference()
    disjoint_tags = set2.difference(set1)
    
    return list(disjoint_tags)

def main():
    list1 = ['PSLL-123123', 'PSLL-123124', 'PSLL-123125', 'PSLL-123125', 'PSLL-123125']
    list2 = ['PSLL-123123', 'PSLL-123124', 'PSHH-151875', 'PSHH-111111', 'PSHH-987455', 'PSHH-432141']
    
    disjoint_tags = disjoint_set(list1, list2)
    print("List2 TAGs that are not in list1:", disjoint_tags)

if __name__ == "__main__":
    main()
