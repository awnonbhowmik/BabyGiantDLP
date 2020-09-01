from sympy import isprime
from numpy import ceil, sqrt
from time import time
from random import randint

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return "inverse doesn't exist"

    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def DLP(g, x, p):
    if isprime(p):
        return int(pow(g, x, p))
    else:
        #print("prime modulo needed")
        return "prime modulo needed"


def baby_giant(g, h, p):
    N = int(ceil(sqrt(p-1)))  # note that phi(p)=p-1

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tabool = {int(pow(g, i, p)): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = int(pow(g, N * (p - 2), p))

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * int(pow(c, j, p))) % p
        if y in tabool:
            return j * N + tabool[y]

    # Solution not found
    return None


#g, x, p = input("Enter g, x and p for g^x mod p: ").split()

# g = int(g)
# x = int(x)
# p = int(p)

g = randint(2,2000)
x = randint(2,2000)
while True:
    p = randint(2,2000)
    if isprime(p):
        break

t1 = time()
h = DLP(g, x, p)
print("{}^{} = {} mod {}".format(g, x, h, p))
# print(h)

print("x = {}".format(baby_giant(g, h, p)))
print("Time elapsed: {} seconds".format(time()-t1))
