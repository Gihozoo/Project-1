def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m-1)


query = input("If you want to calculate r-permutations press 1\n"
              "If you want to calculate r-combinations press 2\n")

if query == "1":
    n = int(input("Write the number of objects (n) in this set\n"))
    r = int(input("Write the number of chosen objects (r) in your set\n"))

    if n > 0 and 0 <= r <= n:
        p = factorial(n) // factorial(n - r)

        print("The number of possible r-permutations is", p)

    else:
        print("One of the conditions is wrong, n must be a positive integer\n"
              "r must be a non negative integer less than or equal to n")

if query == "2":
    n = int(input("Write the number of objects (n) in this set\n"))
    r = int(input("Write the number of chosen objects (r) in your set\n"))

    if n > 0 and 0 <= r <= n:
        p = factorial(n) // (factorial(r) * factorial(n - r))

        print("The number of possible r-combinations is", p)

    else:
        print("One of the conditions is wrong, n must be a positive integer\n"
              "r must be a non negative integer less than or equal to n")