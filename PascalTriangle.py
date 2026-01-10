class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]

        for i in range(1,numRows):
            x = []
            y = a[i-1]
            for j in range(0,len(y)+1):
                if j == 0 or j == len(y):
                    x.append(1)
                else:
                    x.append(y[j]+y[j-1])
            a.append(x)
        return a