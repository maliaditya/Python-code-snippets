import array as arr

marks = arr.array('i',[45,46,69,52,85])

print(marks)

marks = arr.array('i',(45,46,69,52,85))

print(marks)
marks = arr.array('i',{45,46,69,52,85})

print(marks)
marks = arr.array('i',{45:"A",46:"C",69:"D",52:"E"})

print(marks)


list = [2.3,4.5,34.3,45.3]
arraya = arr.array('f', list)

print(arraya)


list = [2,3,4,56,6,6]
arraya = arr.array('f', list)

print(arraya)

list = "aditya"
arraya = arr.array('u', list)

print(arraya)


list = ["a","b","c","d"]
arraya = arr.array('u', list)

print(arraya)



companyArr = arr.array('i',[3,2,1,5,6,9])
print(companyArr)
arr2  = arr.array(companyArr.typecode,(a for a in companyArr))
arr2.append(411)
print(arr2)
print(companyArr)

print(companyArr[2:])
print(companyArr[2:3])
print(companyArr[-5:-2])
print(companyArr[-4:])


jerNo = arr.array('i',{18:"kolhi",7:"Dhoni",41:"Shreyas"})

jerNo.insert(3,12)
jerNo

highestscore = arr.array("i",[1,5,6,2,3,8])
highestscore

jerNo.extend(highestscore)
jerNo


wickets = [100,500,600,200]
jerNo.fromlist(wickets)
jerNo
jerNo.remove(200)
jerNo
jerNo.pop()
jerNo

jerNo.reverse()
jerNo

jerNo.index(41)

jerNo.append(200)
jerNo.count(200)

jerNo.tolist()

jerNo.buffer_info()






