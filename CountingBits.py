class Solution:

    def countBits(self, n: int) -> List[int]:

        ArrayToStore = []
        helperOperation = 0
        Ones = 0

        # 1. make the number
        for i in range(n+1):
            #2. create the number , convert to binary
            actual = i #copiamos el numero , para no arruinar el contador for
            unos_del_numero = 0

            #desarmamos el numero como licuadora
            while actual > 0:
                unos_del_numero += actual % 2
                actual = actual // 2

            ArrayToStore.append(unos_del_numero)

        return ArrayToStore
