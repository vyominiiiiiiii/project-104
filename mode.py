from collections import Counter
import csv

with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
    fileData.pop(0)
    newData=[]

for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

data=Counter(newData)

modeDataRange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurence in data.items():
    if 50<float(height)<60:
        modeDataRange["50-60"]+=occurence
        
    elif 60<float(height)<70:
        modeDataRange["60-70"]+=occurence

    elif 70<float(height)<80:
        modeDataRange["70-80"]+=occurence

modeRange,modeOccurence=0,0

for range,occurence in modeDataRange.items():
    if occurence>modeOccurence:
        modeRange,modeOccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode=float((modeRange[0]+modeRange[1])/2)
print(f"mode is ->{mode:2f}")
