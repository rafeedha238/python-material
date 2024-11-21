X=int(input("Enter the item Quantity"))
Y= X*100
if Y>1000:
    print(f"The Discounted cost is {Y-Y*0.10}")
else:
    print("no discount")
