list =[10,20,30,40,50]
import numpy as np

narr = np.array(list)
narr
type(narr)

# gives dataype = U6 for set in np array
charlist = ["A","B","C","D"]
charlist
narrchar = np.array(charlist)

# check output care fully it differs
numarr = np.array([1.1,1.2,1.3,1.4])
numSet = np.array({1.1,1.2,1.3,1.4})
numTuple = np.array((1.1,1.2,1.3,1.4))
numarr
numTuple
numSet

# gives dataype = object for set in np array
arrStr = np.array({"aditya","Shivaji","mali"})

arrStrli = np.array(["aditya","Shivaji","mali"])
arrStr
arrStrli
numli = ["aditya","Shivaji","mali",18,1,1998]
arrcom = np.array(numli)
arrcom

numMix = [100,200,"aditya","Shivaji","mali",18,1,1998]
numMix = np.array(numMix)
numMix

mularr = [[1,2,3,4],[5,6,7,8]]
numMix = np.array(mularr)
numMix

mularr = [(1,2,3,4),(5,6,7,8)]
numMix = np.array(mularr)
numMix


cric = {1:"adi",2:"Mali"}
cric1 = {1:"adi",2:"Mali"}
dictNum = np.array([cric,cric1])
dictNum

set1 = {1,2,3,4}
set2 = {5,6,7,8}
setNum = np.array([set1,set2])
setNum

# arange(Start,Stop,Step)
numArray = np.arange(1,20,4)
numArray
 

numArray = np.arange(1,10)
numArray = np.arange(1,20,4,dtype=float)

numArray


numArray = np.arange(20).reshape(4,5)
numArray

numArray = np.arange(27).reshape(3,3,3)
numArray