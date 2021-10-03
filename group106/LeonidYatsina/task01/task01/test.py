def linear_search(numbers, x): 
    for index in range(len(numbers)): 
        if numbers[index] == x: 
            return index 
    return -1 
 
def test(result, awaiting_result): 
    if result == awaiting_result: 
        print("Ok") 
    else: 
        print("Ошибка", result, "!=", awaiting_result)  
 
test(linear_search([5, 2, 8, 15, 11], 1), -1) 
test(linear_search([5, 2, 8, 15, 11], 8), 2) 
test(linear_search([5, 2, 8, 15, 11], 15), 3) 
test(linear_search([5, 2, 8, 15, 11], 5), 0)