import intcode

def sandbox():
    c = intcode.Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    c.verbose = True
    for i in range(10):
        print(c.run([]))
    

sandbox()