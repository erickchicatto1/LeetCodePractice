def recycle_old_combinations(dbFolder,threshold=3):
    all_files = []
    max_val=0
    
    for f in dbFolder:
        if f == "one" or f == "two":
            all_files.append(f)
            
    if len(all_files) <= threshold:
        return 
    
    if all_files[0] >= max_val:
        max_val = all_files[0]
        


dbFolder = [1,2,3,4]
recycle_old_combinations(dbFolder)