def accounts():
    while True:
        u=[]
        date=input("Enter todays' date:")
        name=input("Enter The Customer Name:")
        if name=="q":
            break
        item=input("Enter The Item Names:")
        if item=="q":
            break
        i=item.split()
        list=[]
        n=[]
        for elemant in i:
            quantity=int(input(f"Enter The Quantity of {elemant}:"))
            cost=int(input(f"enter the cost of {elemant} per line:"))
            total=quantity*cost
            list.append(f"{elemant} price:{total}Rs")
            p=u.append(total)
            sum_of_numbers=sum(u)
            item_quantitity=f"{elemant}:{quantity}"
            p1=n.append(f"{item_quantitity} lines")
        information=f"\nDate:{date}\nCustomer Name:{name}\nItem Names:{item}\nItem qunatities: {n}\nItem Prices: {list}\ntotal:{sum_of_numbers}\n----------------------------------------------------------------------"
        print(information)
        with open("accounts.txt","a") as add:
            add.writelines(information)
accounts()