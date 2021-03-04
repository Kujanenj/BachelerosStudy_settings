def parseFile(fileName):
        indexOfField = 0
        fullResultsMap={}
        fieldList=[]
        fieldsToIgnore=["label","grpThreads","allThreads"]
        with open(fileName) as file:
            firstLine = file.readline()
            fieldList=firstLine.split(',')
            fieldList[-1]=fieldList[-1].strip()
            lines=file.readlines()
            for nonSplitted in lines:
                line = nonSplitted.split(',')
                line[-1] = line[-1].strip()
                if(line[0] == "Transaction Controller"):
                    continue
                if not line[0] in fullResultsMap:
                        fullResultsMap[line[0]]={}
                      
                for field in fieldList:
                    if(field in fieldsToIgnore):
                        continue
                    indexOfField=fieldList.index(field)
                    if not field in fullResultsMap[line[0]]:
                   
                        fullResultsMap[line[0]][field]=[line[indexOfField]]
                   
                    else:
                        fullResultsMap[line[0]][field].append(line[indexOfField])
            return fullResultsMap
def calculateAverageDeviation(values,averageValue):
    sum = 0
    for value in values:
        sum += abs(averageValue - int(value))
    return round(sum/len(values),2)
def calculateAverage(values):

    sum = 0
    numOfEntries = 0
    for value in values:
        sum += int(value) 
        numOfEntries+=1
    return sum/numOfEntries
def printResults(resultsMap):
    for entry,labels in resultsMap.items():
        print()
        print()
        print(entry)
        for label,values in labels.items():
            print("-----")
            print(label)
            for type,value in values.items():
               print(type + " " + str(value))
def addResults(firstEntry,secondEntry):
    newEntry={}
    print(firstEntry)
    print(secondEntry)
    for label,values in firstEntry.items():
        print(label)
        print(values)
        newEntry[label]={}
        for type,value in values.items():
            newEntry[label][type] = value + secondEntry[label][type]
    return newEntry
def main():
    results=parseFile("results3.csv")
    averageMap = {}
    for entry in results :
        averageMap[entry]={}
        for label in results[entry]:
            averageMap[entry][label]={"average":calculateAverage(results[entry][label])}
            averageMap[entry][label]["deviation"]=calculateAverageDeviation(results[entry][label],averageMap[entry][label]["average"])
    averageMap["combinedAverages"]=addResults(averageMap["REST GET expenses"],averageMap["REST GET users"])
    printResults(averageMap)
main()