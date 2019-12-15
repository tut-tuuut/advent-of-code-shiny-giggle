import intcode

def sandbox():
    print('first program:')
    c = intcode.Computer([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    for o in c.run([]):
        print(o, end=',')
    print('\n')
    print('second program:')
    c = intcode.Computer([1102,34915192,34915192,7,4,7,99,0])
    for o in c.run([]):
        print(o)
        print(f'length of o: {len(str(o))} (should be 16)')
    print('third program:')
    c = intcode.Computer([104,1125899906842624,99])
    for o in c.run([]):
        print(f'this should be 1125899906842624: {o}')
    

sandbox()