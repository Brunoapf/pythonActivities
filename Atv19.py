number = int(input("Write a number: "))

is_prime = True

for x in range(2, number):
    if number % x == 0:
        is_prime = False
        break

if is_prime:
    print("Is prime")
else:
    print("Is not prime")