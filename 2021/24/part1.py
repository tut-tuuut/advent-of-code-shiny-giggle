from itertools import product
from monad import monad
import utils as u

biggest_number = 0
for a in range(1,10):
    print(('▓'*a).ljust(10,'░'), end="\r")
    for b,c,d,e,f,g,h,i,j,k,l,m,n in product(range(1,10), repeat=13):
        _,_,_,z = monad(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
        if z == 0:
            number = int(''.join((a,b,c,d,e,f,g,h,i,j,k,l,m,n)))
            if number > biggest_number:
                biggest_number = number
print("")
u.answer_part_1(biggest_number)