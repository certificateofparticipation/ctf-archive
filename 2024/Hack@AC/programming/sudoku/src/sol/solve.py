from pwn import *

r = remote("localhost", 2001)

for _ in range(100):
    print("Starting ...")
    start = r.recvuntil(b":")
    raw = r.recv().splitlines()[1:-1]
    grid = []

    for i in raw:
        row = i.split()
        grid.append(row)

    # print(grid)
    
    p = process("./sol.exe")
    for row in grid:
        newrow = b''
        for i in row:
            newrow += i + b' '
        p.sendline(newrow)
    
    solved = [] 
    for _ in range(9):
        row = p.recvline().strip()
        r.sendline(row)
        solved.append(row)
    
    for row in solved:
        print(row.decode('ascii'))
    p.close()
    
data = r.recvall().splitlines()
for i in data:
    print(i)
r.close()
