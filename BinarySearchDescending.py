

def BusquedaBinaria(lista,target):
    indexIzq = 0
    indexDer = len(lista)-1
    
    while indexIzq <= indexDer:
        medio = (indexIzq+indexDer)//2 #punto importante 
        valorMedio = lista[medio]

        if valorMedio == target:
            return medio # retorna el index
        elif target < valorMedio:
            indexDer = medio -1
        else:
            indexIzq = medio + 1    
    return -1


if __name__ =="__main__":
    
    MyList = [1,2,3,7,5]

    #ordenar la lista de menor a mayor 
    for i in range(len(MyList)):
        for j in range(len(MyList)-1):
            if MyList[j] > MyList[j+1]:
                MyList[j+1],MyList[j] = MyList[j],MyList[j+1]
                        
    print(BusquedaBinaria(MyList, 7))
    
    
