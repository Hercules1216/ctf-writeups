import math

#### Given
n = 485
e = 53
c = "153 75 309 310 74 203 208 401 310 371 363 451 125".split(" ")

#### Calculated
# p - Small int of the prime factorization of n
# q - larger int of the prime factorization of n
###

p = 5
q = 97

# d is calculated like so
print((p-1)*(q-1)) # gives right answer
d = pow(e,-1) % ((p-1)*(q-1)) #Does not give right answer
# d = (53^-1) % 384
print(d)

for cLetter in c:
    print(chr(pow(int(cLetter), 29, 485)), end="")
    #                 c         d   n