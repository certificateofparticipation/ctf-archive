from pwn import *

r = remote("localhost", 2002)

for _ in range(100):
    print("Starting ...")
    start = r.recvuntil(b":\n")
    
    raw = b''
    while r.can_recv():
        raw += (r.recvline())
    
    lines = raw[:-1].splitlines()
    
    p = process("./sol")
    p.sendline(lines[0])
    
    for i in range(len(lines) - 1):
        p.sendline(lines[i+1])
        if i % 2 == 1:
            ans = p.recv()
            # print(ans)
            r.sendline(ans[:-1])

    p.close()
    
endmsg = r.recv().splitlines()
for i in endmsg:
    print(i)
r.close()
