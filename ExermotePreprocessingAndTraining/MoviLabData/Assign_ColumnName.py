import os
import csv


# 해당 디렉토리에 있는 모든 .csv 파일 열 이름을 지정합니다. 

title = ["time",'eSense Name','Ax','Ay','Az','Gx','Gy','Gz','title','label']

csvFileList = []
for i in os.listdir('./') :
    if i.find('.csv') != -1  :
        csvFileList.append(i)

for csvFile in csvFileList :
    f = open(csvFile,'r')
    rdr = csv.reader(f)
    data = []
    for line in rdr :
        data.append(line)
    f.close()

    if data[0][0] == 'time' :
        continue
    

    f = open(csvFile,'w',newline='')
    wr = csv.writer(f)
    wr.writerow(title) 
    for line in data :
        wr.writerow(line)
    f.close()

    print(csvFile + ' 파일 열 이름 지정완료.')