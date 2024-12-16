import random

for f in range(100):
    file = open(f"./in/{f}.in",'w')

    t = 150
    file.write(str(t) + '\n')
    for tn in range(t):
        file.write(str(20) + '\n')
        gears = []
        for i in range(20):
            gears.append(str(random.randint(100,600)))
        file.write(' '.join(gears) + '\n')
    
    file.close()