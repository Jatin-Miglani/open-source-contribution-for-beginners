
n1 = float(input("Enter first number"))
n2 = float(input("Enter second number"))
op = input("Enter operation")

if op == "+":
    print(n1+n2)

elif op == "_":
    print(n1-n2)

elif op == "*":
    print(n1*n2)

elif op == "/":
    print(n1/n2)

elif op == "**":
    print(n1**n2)

else:
    print("invalid option")