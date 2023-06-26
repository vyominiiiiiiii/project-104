import csv

with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
    fileData.pop(0)
    newData=[]

for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))

n=len(newData)
sum=0

for x in newData:
    sum+=x

mean=sum/n
print("mean is "+str(mean))