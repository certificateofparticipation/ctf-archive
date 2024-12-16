import time
import random

flag = "ACSI{su_r00t_cat_fl@9}"
ac = True
nums = ['1','2','3','4','5','6','7','8','9']
TIME_LIMIT = 200 # in ms

def get_puzzle(test_number):
    puzzle = []
    with open(f"./in/{test_number}.in", 'r') as file:
        input_data = file.readlines()
        for line in input_data:
            puzzle.append(line.strip().split())
    return puzzle            

def check_sudoku(grid, test_number):
    original = get_puzzle(test_number)
    isMatching = True
    for i in range(9):
        for j in range(9):
            if original[i][j] != '0' and original[i][j] != grid[i][j]:
                isMatching = False
    
    if not isMatching:
        return False
        
    for i in range(9):
        row = [grid[i][j] for j in range(9)]
        if sorted(row) != nums:
            return False

    for i in range(9):
        column = [grid[j][i] for j in range(9)]
        if sorted(column) != nums:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if sorted(square) != nums:
                return False

    return True

def run_test(test_number, idx):
    global ac    
    
    with open(f"./in/{test_number}.in", 'r') as file:
        input_data = file.read()
    print(f'\nPuzzle #{idx}:')
    print(input_data)
    print('')
    
    grid = []
    try:
        for _ in range(9):
            line = input()
            line = line.strip().split()
            for _ in range(9):
                line.append('0')
            grid.append(line[:9])
    except:
        ac = False
        return f"#{idx}: RUN TIME ERROR"

    start_time = time.time()
    try:
        if check_sudoku(grid, test_number):
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
    
    print('''
Welcome to Sudoku!
I'll give you challenges, you have to solve them!
Return the solved puzzle in the same format as I gave it to you.
          ''')
    
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
