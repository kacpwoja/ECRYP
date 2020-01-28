
def legendre_symbol(a: int, p: int):
    """ Jacobi -> factorize denominator, return multiplications of legendres
        Check if x^2 === a mod p has solutions -> no. of solutions is 1+legendre(a,p)
        pseudoprime - if base a, and p is an odd prime not dividing a^2 - 1, then
        x = (a^2p - 1)/(a^2 - 1) is a pseudoprime of base a
    """
    x = (int((p-1)/2))
    y = pow(a,x,p)
    if y == 0: return 0
    if y == 1: return 1
    if y-p == -1: return -1
    else: return "err"



if __name__ == "__main__":
    print(legendre_symbol(128, 5))
    print(legendre_symbol(35, 7))
    print(legendre_symbol(56, 13))