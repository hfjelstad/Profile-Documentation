import re
import os

counter = 1
obj = ''
testDict = {}
maxDescriptionLenght = 0
print(os.listdir())
with open("/09-XML-Source/Annotation/varelager.txt") as x:
    for y in x:
        objDict = {}
        if re.search('====', y):
            obj = y.replace('=', " ").strip()
            testDict[obj] = []
            
            counter += 1
        else:
            try: 
                yList = y.split(' ')
                yName = yList[0]
                nameList = yName.split(":",1)
                #print(nameList[1])
                skipNumber = len(yList[0]) + 1 + len(yList[1]) + 1 +  len(yList[2]) + 1
                objDict['Type'] = nameList[0]
                objDict['Name'] = nameList[1]
                objDict['Container'] = yList[1]
                objDict['Description'] = y[skipNumber:].replace('\n',' ')
                if  len(objDict['Description']) < 2:
                    objDict['Description'] = "..."
                    objDict['Container'] = objDict['Container'].replace('\n',' ')
                if len(objDict['Description']) > maxDescriptionLenght:
                    maxDescriptionLenght = len(objDict['Description'])
            except:
                pass
        
        testDict[obj].append(objDict)              
            
typeLenght = 10
nameLenght = 30
containerLengt = 30

print(testDict)