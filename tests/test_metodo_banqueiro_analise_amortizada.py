import numpy as np
import unittest

def check_safe_state(available, allocation, request, credit):
    work = available.copy()
    finish = np.zeros(len(allocation), dtype=bool)
    
    while True:
        found = False
        for i in range(len(allocation)):
            if not finish[i] and np.all(request[i] <= work + allocation[i]):
                work += allocation[i]
                finish[i] = True
                found = True
                credit[i] += 1
                break
        if not found:
            if np.all(finish):
                return True
            else:
                return False

def calculate_amortized_cost(credit_used, credit_before, request):
    return np.sum(request) + credit_before - credit_used

class TestCheckSafeState(unittest.TestCase):
    def setUp(self):
        self.allocation = np.array([[0, 1, 0],
                                     [2, 0, 0],
                                     [3, 0, 2],
                                     [2, 1, 1],
                                     [0, 0, 2]])

        self.request = np.array([[0, 0, 0],
                                  [2, 0, 2],
                                  [0, 0, 0],
                                  [1, 0, 0],
                                  [0, 0, 2]])

        self.available_resources = np.array([[10, 5, 7]])

        self.credit = np.zeros(len(self.allocation))

    def test_check_safe_state_with_deadlock(self):
        # Configuração para criar um estado de deadlock
        allocation_deadlock = np.array([[0, 1, 0],
                                        [2, 0, 0],
                                        [3, 0, 2],
                                        [2, 1, 1],
                                        [0, 0, 2]])

        request_deadlock = np.array([[0, 1, 0],  # Processo 1 solicita os recursos do processo 2
                                     [2, 0, 0],
                                     [3, 0, 2],
                                     [2, 1, 1],
                                     [0, 0, 2]])

        available_deadlock = np.array([[10, 5, 7]])  # Recursos disponíveis suficientes para processos em execução

        credit_deadlock = np.zeros(len(allocation_deadlock))

        # Verifica se o estado é considerado como deadlock
        self.assertTrue(check_safe_state(available_deadlock, allocation_deadlock, request_deadlock, credit_deadlock))

    def tearDown(self):
        print("Allocation Matrix:")
        print(self.allocation)
        print("Solicitation Matrix:")
        print(self.request)
        print("Available resources:")
        print(self.available_resources)
        print("Credit for Processes:")
        print(self.credit)
        print("-" * 50)

if __name__ == "__main__":
    unittest.main()
