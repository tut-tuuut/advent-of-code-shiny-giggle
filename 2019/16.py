def tens(integer):
    return abs(integer)%10

def fft(inputSeq):
    pattern = [0,1,0,-1]
    sequence = list(map(int,list(str(inputSeq))))
    outputSeq = []
    for outputPosition in range(len(sequence)):
        print(f'position {outputPosition}')
        for i,inputEl in enumerate(sequence):
            print(f'{pattern[(1 + i//(outputPosition+1))%len(pattern)]}*{inputEl}')

def sandbox():
    inputSeq = 12345678
    fft(inputSeq)

sandbox()