#fibonacci_generator

def fib(n):
    a=0
    b=1

    print(a)
    print(b)

    for i in range(2,n):
        c= a + b
        a = b
        b = c
        print(b)
 
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print("Done")

        while True:
            try:
                n = int(input("Enter a number: "))
                if n < 0:
                    print("Enter a positive number")
                else:
                    break
            except ValueError:
                print("Enter a valid number")

                
fib(10)

    
  

    

