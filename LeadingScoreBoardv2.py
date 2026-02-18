def createRank(scores):
    rank = []
    currScores = scores[0]
    count = 1
    
    for score in scores:
        if score != currScores:
            currScores = score
            count += 1
        rank.append(count)
    return rank

def climbingLeaderboard(ranked,player):
    rank = createRank(ranked)
    ranked.append(-1)  #acomodar a ranked
    rank.append(rank[-1]+1) #acomodar a rank

    res = []
    
    pointer = len(ranked) -1
    
    for playerScore in player:
        
        while pointer >= -1:
            if pointer  - 1 >= 0:
                
                print(playerScore,ranked[pointer],rank[pointer])
                if playerScore > ranked[pointer-1]:
                    print("this is a rankedPointer",ranked[pointer-1])
                    pointer -= 1
                elif playerScore == ranked[pointer-1]:
                    print("this is a rankedPointer",ranked[pointer-1])
                    res.append(rank[pointer-1])
                    break
                else:
                    if playerScore >= ranked[pointer]:
                        print("this is a rankedPointer",ranked[pointer])
                        res.append(rank[pointer])
                        break
                    else:
                        res.append(rank[pointer]+1)
                        break
                        
            else:
                if playerScore >= ranked[pointer]:
                    print("This is a rankedPointer",ranked[pointer])
                    res.append(rank[pointer])
                    break
                else:
                    res.append(rank[pointer]+1)
                    break
    return res
                
                
if __name__ == "__main__":
    
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    
    climbingLeaderboard(ranked,player)
                
'''

ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
Rankings únicos de ranked: [1, 2, 2, 3, 4, 5]

Empezamos desde el final (60 → rank 5).

playerScore = 50 → menor que 60 → rank 6

playerScore = 65 → entre 60 y 75 → rank 5

playerScore = 77 → entre 75 y 80 → rank 4

playerScore = 90 → igual que 90 → rank 2

playerScore = 102 → mayor que 100 → rank 1

Esto coincide con el resultado esperado: [6, 5, 4, 2, 1].

'''
    
