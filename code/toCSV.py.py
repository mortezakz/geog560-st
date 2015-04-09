'''
Created on Apr 2, 2015

@author: sks5122
'''

csFile = "C:/Users/sks5122/Desktop/Geog560_SpaceTime/final/geog560-st/data/"

clickDict={}
writeableString = ""
keys=[]
count = 0
clickstream = open(csFile+"clickstream_example_dump.txt")

header = True
for line in clickstream :
    clickDict = eval(line)
    if (header) :
        keys=clickDict.keys()
        firstKey = True
        for akey in keys :
            if (firstKey) :
                writeableString = writeableString + akey
                firstKey = False
            else :
                writeableString =  writeableString + "," + akey 
        header = False
    else :
        writeableString = writeableString + "\n"
        rowKeys = clickDict.keys()
        orderedVals=["NA"]*14
        for akey in rowKeys :
            if (akey ==  keys[0]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[0] = valsList
                else :
                    orderedVals[0] = str(clickDict[akey]).replace(',',';')
            elif (akey == keys[1]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[1] = valsList
                else :
                    orderedVals[1] = str(clickDict[akey]).replace(',',';')                
            elif (akey ==  keys[2]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[2] = valsList
                else :
                    orderedVals[2] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[3]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[3] = valsList
                else :
                    orderedVals[3] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[4]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[4] = valsList
                else :
                    orderedVals[4] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[5]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[5] = valsList
                else :
                    orderedVals[5] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[6]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[6] = valsList
                else :
                    orderedVals[6] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[7]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[7] = valsList
                else :
                    orderedVals[7] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[8]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[8] = valsList
                else :
                    orderedVals[8] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[9]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[9] = valsList
                else :
                    orderedVals[9] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[10]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[10] = valsList
                else :
                    orderedVals[10] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[11]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[11] = valsList
                else :
                    orderedVals[11] = str(clickDict[akey]).replace(',',';')
            elif (akey ==  keys[12]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[12] = valsList
                else :
                    orderedVals[12] = str(clickDict[akey]).replace(',',';')
            elif (akey == keys[13]) :
                if (isinstance(clickDict[akey], list)) :
                    valsList = []
                    for value in clickDict[akey] :
                        valsList.append(str(value).replace(',',';'))
                        orderedVals[13] = valsList
                else :
                    orderedVals[13] = str(clickDict[akey]).replace(',',';')
        firstRec = True
        for oVal in orderedVals :
            if (firstRec) :
                writeableString = writeableString + str(oVal)
                firstRec=False
            else :
                writeableString = writeableString + "," + str(oVal)
    count = count + 1
    print(count)
#writeableFile = open("C:/Users/sks5122/Desktop/Geog560_SpaceTime/final/geog560-st/data/clickstreamData.csv")
with open(csFile+"clickstreamCSV.csv", "w") as writeableFile:
    writeableFile.write(writeableString)