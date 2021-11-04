def matchingSocks(numberofSocks, arrayofSocks):
    socksDict = {}
    global numberofPairs 
    numberofPairs = 0   
    for a in range(numberofSocks):         
        if not str(arrayofSocks[a]) in socksDict:
            socksDict[str(arrayofSocks[a])] = 1
        else:
            socksDict[str(arrayofSocks[a])] += 1
    for key in socksDict:
        if socksDict[key] % 2 == 0:
            numberofPairs += socksDict[key] // 2
        else:
            numberofPairs += (socksDict[key]-1) // 2
    return numberofPairs
 

