if __name__ == '__main__':
    i = 0
t=0
NameList = []
ScoreList = []
arr = [] 
for _ in range (int(input())):
    name = input()
    score = float(input())
    NameList.append(name)
    ScoreList.append(score)
    i+=1

ScoreList1 = sorted(ScoreList)
ScoreSet = set(ScoreList1)
ScoreList2 = list(ScoreSet)
if (len(ScoreList2)>1):
    
    number = ScoreList2[1]
    for i in range (0, len(ScoreList)):
        if(number == ScoreList[i]):
            arr.append(NameList[i])
            t+=1
    arr.sort()
    #print(arr[0])
    for i in range (0, len(arr)):
        print(arr[i])
else:
    print(NameList[0])
    

