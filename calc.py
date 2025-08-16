op=input("enter an operator(+ - * /)")
num1=int(input("enter number"))
num2=int(input("enter number"))
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print(f"{op} is not a valid operator")  
