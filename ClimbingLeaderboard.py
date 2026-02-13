import math
import os
import random
import re
import sys

def createRank(scores):
    rank = []
    currScore = scores[0]
    count = 1
    
    for score in scores:
        if score != currScore:
            currScore = score
            count += 1
        rank.append(count)
        
    return rank


def climbingLeaderboard(ranked, player):
    rank = createRank(ranked)
    ranked.append(-1)
    rank.append(rank[-1]+1)
    
    res = []
    
    pointer = len(ranked)-1
    for playerScore in player:
        while pointer >= -1:
            if pointer - 1 >= 0:
                print(playerScore, ranked[pointer], rank[pointer])
                if playerScore > ranked[pointer-1]:
                    pointer -= 1
                elif playerScore == ranked[pointer-1]:
                    res.append(rank[pointer-1])
                    break
                else:
                    if playerScore >= ranked[pointer]:
                        res.append(rank[pointer])
                        break
                    else:
                        res.append(rank[pointer]+1)
                        break
            else:
                if playerScore >= ranked[pointer]:
                    res.append(rank[pointer])
                    break
                else:
                    res.append(rank[pointer]+1)
                    break
                        
    return res
  
                    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
