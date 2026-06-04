def fizzbuzz(n):

    for num in range(1, n + 1):

        if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            print("FizzBuzzBoom")
        elif num % 3 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0 and num % 7 == 0:
            print("FizzBoom")
        elif num % 5 == 0 and num % 7 == 0:
            print("BuzzBoom")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 7 == 0:
            print("Boom")
        
        else:
            print(num)

print(fizzbuzz(105))