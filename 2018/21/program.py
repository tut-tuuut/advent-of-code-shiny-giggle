import utils

# ip 2 -> variable d
initial_zero = 0
z, u, d, t, q, c, s = initial_zero, 0, 0, 0, 0, 0, 0

# 0. seti 123 0 4
q = 123
# 1. bani 4 456 4
q &= 456
# 2. eqri 4 72 4
q = int(q == 72)

# 3. addr 4 2 2
# 4. seti 0 0 2
# 5. seti 0 1 4

# 6. bori 4 65536 1
# 7. seti 16031208 7 4
# 8. bani 1 255 3
# 9. addr 4 3 4
# 10. bani 4 16777215 4
# 11. muli 4 65899 4
# 12. bani 4 16777215 4
# 13. gtir 256 1 3
t = int(256 > u)
# 14. addr 3 2 2
d = t + d  # if t > 256 goto 16 -> 28
# 15. addi 2 1 2
d += 1  # => goto 17
# 16. seti 27 3 2
d = 27  # => goto 28
# 17. seti 0 9 3
t = 0
# 18. addi 3 1 5
c = t + 1
# 19. muli 5 256 5
c *= 256
# 20. gtrr 5 1 5
c = int(c > u)  # if c > u goto  23 -> 26
# 21. addr 5 2 2
d = d + c  # goto 23
# 22. addi 2 1 2
d = d + 1  # goto 24
# 23. seti 25 7 2
d = 25
# 24. addi 3 1 3
t += 1
# 25. seti 17 4 2
d = 17  # -> 18


# 26. setr 3 1 1
u = t
# 27. seti 7 5 2
d = 7  # -> 8


# 28. eqrr 4 0 3
t = int(q == z)
# 29. addr 3 2 2
d = t + d  # -> 31 -> end
# 30. seti 5 1 2
d = 5  # -> 6
print(z, u, d, t, q, c, s)
