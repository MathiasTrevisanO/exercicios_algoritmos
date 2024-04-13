
import heapq
def k_largest_elements(array, k):
    return heapq.nlargest(k, array)

def k_min_elements(array, k):
    return heapq.nsmallest(k, array)

def main():
    
    array = [3, 10, 4, 7, 8, 20, 15]
    k = 3

    print("k_largest_elements:")
    print(k_largest_elements(array, k))
    
    print("k_min_elements:")
    print(k_min_elements(array, k))
    
if __name__ == '__main__':
    main()