n=int(input("Enter a number: "))
g=int(input("Guess it's binary: "))

print("Decimal: ", n, " -  Binary: ", bin(n)[2:])
print("Your guess: ", g)

print("12: ", bin(12)[2:])
print("10: ", bin(10)[2:])
print("12 AND 10: ", 12 & 10)
print("12 OR 10: ", 12 | 10)