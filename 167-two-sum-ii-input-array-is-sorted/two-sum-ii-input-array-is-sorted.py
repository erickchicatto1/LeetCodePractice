class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointerLeft = 0
        pointerRight = len(numbers)-1
        SumToReturn = []

        while(pointerLeft < pointerRight):
            #1.
            suma = numbers[pointerLeft] + numbers[pointerRight]
            #2.
            if suma == target:
                SumToReturn.append(suma)
                return [pointerLeft+1,pointerRight+1,]
            #3. 
            if suma < target:
                pointerLeft += 1
            #4 como devolver los 2 indicies modificados?    
            elif suma > target:
                pointerRight -= 1
            






            






