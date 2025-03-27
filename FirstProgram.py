#print("hi This is a pycharm")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
while True:
    print("1.ADDITION")
    print("2.SUBTRACTION")
    c=input("choose any one number between 1-3:")
    if c=='3':
        print("You choose invalid number..!")
        continue
    n=int(input("Enter a n  number:"))
    m=int(input("Enter a m number:"))
    if c=='1':
        print(f"addtion result:{add(n,m)}\n")
    elif c=='2':
        print(f"Subtraction reslt:{subtract(n,m)}\n")



