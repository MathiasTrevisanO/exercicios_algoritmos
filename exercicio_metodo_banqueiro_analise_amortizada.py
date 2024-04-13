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

class TestResourceAllocation(unittest.TestCase):
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

    def test_resource_allocation(self):
        processes = [2, 3, 5]
        requests = [
            [1, 0, 1],
            [2, 0, 0],
            [0, 0, 1]
        ]
        
        for idx, process in enumerate(processes):
            with self.subTest(process=process):
                if np.all(requests[idx] <= self.request[process-1]):  # Corrected here
                    self.available_resources -= requests[idx]
                    self.allocation[process-1] += requests[idx]
                    self.request[process-1] -= requests[idx]
                    
                    safe = check_safe_state(self.available_resources, self.allocation, self.request, self.credit)
                    
                    cost_amortized = calculate_amortized_cost(np.sum(requests[idx]), self.credit[process-1], requests[idx])
                    
                    if cost_amortized >= 0:
                        self.assertTrue(safe)
                        self.assertGreaterEqual(cost_amortized, 0)
                    else:
                        self.assertFalse(safe)
                        self.assertLess(cost_amortized, 0)
                
                else:
                    self.assertFalse(np.all(requests[idx] <= self.request[process-1]))  # Corrected here

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
