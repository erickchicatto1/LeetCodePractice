def transactionsOperations(transactions):

    totals = {}

    for _,user,amount in transactions:
        print(f"{_} {user} {amount} ")
        
        if user in totals.keys():
            totals[user] += amount
        else:
            totals[user] = amount
    
    print(totals["user1"])        
    print(totals["user2"])
    print(totals["user3"])
    
        
if __name__ =="__main__":
    transactions = [
    (1,"user1",150),
    (2,"user3",100),
    (3,"user2",150),
    (2,"user2",100)]
    
    transactionsOperations(transactions)
        
    
