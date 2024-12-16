import time
import random

flag = 'ACSI{doNT_bE_Gr33dY_j528c}'
ac = True
TIME_LIMIT = 200 # in ms

def get_testcase(test_number):
    testcase = ""
    sol = []
    
    with open(f'./in/{test_number}.in', 'r') as file:
        testcase = file.read()
    with open(f'./out/{test_number}.out', 'r') as file:
        sol = file.readlines()
        for i in range(len(sol)):
            sol[i] = sol[i][:-1]
    return testcase, sol       

def check_testcase(user_input, sol):
    for i, line in enumerate(user_input):
        if line != sol[i]:
            # print(f'Given: ({line}), Correct: ({sol[i]})')
            return False
    return True    
    
def run_test(test_number, idx): # test_number is secret, idx is the order with which the testcase is given
    global ac    
    
    # Get testcase
    testcase, sol = get_testcase(test_number)
    print(f'Testcase #{idx}:')
    print(testcase)
    
    
    # Get user input
    user_input = []
    try:
        for i in range(len(sol)):
            line = str(input()).strip()
            user_input.append(line)
            
    except:
        ac = False
        return f"#{idx}: RUN TIME ERROR"

    # Check user input
    start_time = time.time()
    try:
        if check_testcase(user_input, sol):
            end_time = time.time()
            duration = int((end_time - start_time) * 1000)
            if duration < TIME_LIMIT:
                return f"#{idx}: PASSED - {duration}ms"
            else:
                ac = False
                return f"#{idx}: TIME LIMIT EXCEEDED - {duration}ms"
            
        else:
            ac = False
            return f"#{idx}: WRONG ANSWER"

    except:
        ac = False
        return f"#{idx}: RUN TIME ERROR"
    
    
def main():
    test_numbers = [i for i in range(100)]
    random.shuffle(test_numbers)
    
    results = []
    for idx, test_number in enumerate(test_numbers):
        results.append(run_test(test_number, idx))
    
    print('\n\nRESULTS:')
    for result in results:
        print(result)
    
    if ac:
        print(flag)

if __name__ == "__main__":
    main()
