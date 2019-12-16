def tens(integer):
    return abs(integer)%10

def outputElement(inputSequence, outputPosition):
    pattern = [0,1,0,-1]
    return tens(sum(map(lambda x: x[1] * pattern[((x[0]+1)//outputPosition)%len(pattern)], enumerate(inputSequence))) )

def fft(inputSeq):
    sequence = list(map(int,list(str(inputSeq))))
    outputSeq = map(lambda x: outputElement(sequence, x), range(1,len(sequence)+1))
    return ''.join(map(str, outputSeq))

def sandbox():
    inputSeq = '12345678'
    for _ in range(4):
        inputSeq = fft(inputSeq)
        print(inputSeq)

    inputSeq = '80871224585914546619083218645595'
    for _ in range(100):
        inputSeq = fft(inputSeq)
    print('test2 - this should be 24176176:')
    print(inputSeq[:8])

    inputSeq = '19617804207202209144916044189917'
    for _ in range(100):
        inputSeq = fft(inputSeq)
    print('test3 - this should be 73745418:')
    print(inputSeq[:8])

    inputSeq = '69317163492948606335995924319873'
    for _ in range(100):
        inputSeq = fft(inputSeq)
    print('test4 - this should be 52432133:')
    print(inputSeq[:8])

def part1():
    inputSeq = '59701570675760924481468012067902478812377492613954566256863227624090726538076719031827110112218902371664052147572491882858008242937287936208269895771400070570886260309124375604950837194732536769939795802273457678297869571088110112173204448277260003249726055332223066278888042125728226850149451127485319630564652511440121971260468295567189053611247498748385879836383604705613231419155730182489686270150648290445732753180836698378460890488307204523285294726263982377557287840630275524509386476100231552157293345748976554661695889479304833182708265881051804444659263862174484931386853109358406272868928125418931982642538301207634051202072657901464169114'
    for _ in range(100):
        inputSeq = fft(inputSeq)
    print('part1 - answer:')
    print(inputSeq[:8])

sandbox()
part1()