transactions = [
    (1,"user1",150),
    (2,"user3",100),
    (3,"user2",150),
    (2,"user2",100)]

totals = {}

for _,user,amount in transactions:
    print(f"{_} {user} {amount} ")
    
    if user in totals.keys():
        totals[user] += amount
    else:
        totals[user] = amount
        
print(totals["user2"])
        

