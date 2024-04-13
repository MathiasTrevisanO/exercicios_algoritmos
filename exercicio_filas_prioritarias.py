import queue
import random

priority_queue = queue.PriorityQueue()

def add_pacient(priority_queue, condition):
    priority = random.randint(1, 100) 
    priority_queue.put((priority, condition))

def attend_pacient(priority_queue):
    while not priority_queue.empty():
        condition = priority_queue.get()
        print(f"Atending pacient with condition: {condition}")
        if priority_queue.empty():
            print("Pacients queue is empty")
    
    
def main():
    add_pacient(priority_queue, 'A')
    add_pacient(priority_queue, 'B')
    add_pacient(priority_queue, 'C')
    add_pacient(priority_queue, 'D')
    add_pacient(priority_queue, 'E')
    add_pacient(priority_queue, 'F')
    add_pacient(priority_queue, 'G')
    
    attend_pacient(priority_queue)

if __name__ == '__main__':
    main()
