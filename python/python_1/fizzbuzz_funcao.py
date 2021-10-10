def fizzbuzz(n):
    if n % 3 == 0 and not n % 5 == 0:
        return "Fizz"
    if n % 5 == 0 and not n % 3 == 0:
        return "Buzz"
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if not n % 3 == 0 and not n % 5 == 0:
        return n


print(fizzbuzz(n=int(input("Digite um valor: "))))
