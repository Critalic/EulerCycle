graph = [[1,1,0],
         [0,1,1],
         [1,0,1]
          ]


def eulerCycle(graph):
    checkedList = []
    #Gets all connections and puts them in checkedList
    for i in range(len(graph)):
        for b in range(len(graph[i])):
            if( graph[i][b]==1 ) : checkedList.append([i,b])


    index2 = 1
    ties=[]
    b = len(checkedList)
    sortedcheckedList = [checkedList.pop(0)]
    numberOfIterations =0
    while(len(checkedList)!=0):
        if(len(sortedcheckedList)==0):
            sortedcheckedList = [checkedList.pop(0)]
            l = sortedcheckedList[len(sortedcheckedList)-1][index2]
        else:
            l = sortedcheckedList[len(sortedcheckedList) - 1][index2]
        oldCheckedListLength = len(checkedList)

        for n in range (len(checkedList)-1) :
            if(checkedList[n][0]==l and checkedList[n][1] ==l) :
                sortedcheckedList.append(checkedList.pop(n))

        for i in range (len(checkedList)) :
           if(checkedList[i][0] == l) :
                sortedcheckedList.append(checkedList.pop(i))

                break
        if(oldCheckedListLength == len(checkedList)) :
            checkedList.append(sortedcheckedList.pop(len(sortedcheckedList) - 1))
            checkedList.append(sortedcheckedList.pop(len(sortedcheckedList) - 1))

        numberOfIterations+=1
        if(numberOfIterations > 1000):
            for d in range(len(sortedcheckedList)-2):
                if(sortedcheckedList[d][0] == sortedcheckedList[d][1]):
                    ties.append(sortedcheckedList.pop(d))
            for d in range (len(checkedList)-2):
                if(checkedList[d][0]==checkedList[d][1]):
                    ties.append(checkedList.pop(d))
        if (numberOfIterations > 2000):
            sortedcheckedList = "The graph doesn't have an Euler's cycle"
            break

    for i in range (len(graph)):
        print(graph[i])
    print("Ейлерів цикл: ", sortedcheckedList)
    print(ties)












eulerCycle(graph)