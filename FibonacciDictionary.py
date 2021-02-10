Dict={0:0, 1:1}
def fibo(n):
    if n not in Dict:
        val=fibo(n-1)+fibo(n-2)
        Dict[n]=val
    return Dict[n]
n=int(input("Enter the value of n:"))
print("Fibonacci(", n,")= ", fibo(n))

# uncomment to take input from the user
nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):```
       print(fibo(i), end=" , ")
