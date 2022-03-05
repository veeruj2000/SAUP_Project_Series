sum=0
while(True):
    num=input("Enter Price or Press q to quit: ")
    if(num!='q'):
        sum=sum+int(num)
        print(f'Order total so far: {sum}')
    else:
        print("The total bill is: ",sum,". Thanks for using our calculator.")
        break