
def stack_sort(list):
    stack = []
    for value in list:
        stack.append(value)
    
    sorted_list = []
    
    while stack:
        value = stack.pop()
        index = 0
        while index < len(sorted_list) and value > sorted_list[index]:
            index += 1
        
        sorted_list.insert(index, value)
    
    return sorted_list
    
def main():
    # Input
    list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # Output
    # A lista ordenada é [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print(stack_sort(list))

if __name__ == '__main__':
    main()