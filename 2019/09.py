import intcode

def sandbox():
    c = intcode.Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    for o in c.run([]):
        print(o, end=',')
    print('\n')
    

sandbox()