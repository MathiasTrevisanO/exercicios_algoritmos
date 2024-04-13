import heapq

def heap_sort(array):
    heapq.heapify(array)
    sorted_array = []
    while array:
        sorted_array.append(heapq.heappop(array))
    
    return sorted_array
    

def main():
    array = [12, 11, 13, 5, 6, 7]
    
    print(heap_sort(array))
if __name__ == '__main__':
    main()