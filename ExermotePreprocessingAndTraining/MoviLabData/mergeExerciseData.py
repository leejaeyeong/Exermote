import csv
import os 

# 디렉토리 내의 csv 운동 데이터를 ExerciseData.csv 파일로 합친다.  

title = ["time",'eSense Name','Ax','Ay','Az','Gx','Gy','Gz','title','label']

csvFileList = []
for i in os.listdir('./') :
    if i.find('.csv') != -1  :
        csvFileList.append(i)
if csvFileList.count('ExerciseData.csv') == 1 :
    del csvFileList[csvFileList.index('ExerciseData.csv')]
    
data = []
for csvFile in csvFileList :
    f = open(csvFile,'r')
    rdr = csv.reader(f)
    for line in rdr :
        data.append(line)
    f.close()

f = open('ExerciseData.csv','w',newline='',encoding='utf-8')
wr = csv.writer(f)
wr.writerow(title) 

for line in data :
    if 'time' in line :
        continue
    wr.writerow(line)
f.close()


