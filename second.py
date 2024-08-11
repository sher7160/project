def main():
    print("== Basic Calculator ==")

num1=float(input("enter any number :"))
num2=float(input("enter any number :"))
print("selcet operators :")
print("1,For Addition :")
print("2,For Multiplication :")
print("3,Substraction :")
print("4,For Division :")
Choice=input("select one of above :")
if Choice in ["1","2","3","4"]:
    if Choice == "1":
        print(num1+num2)
    elif Choice=="2":
        print(num1*num2)
    elif Choice=="3":
        print(num1-num2)
    elif Choice=="4":
        print(num1/num2)


main()
        

    


2


    