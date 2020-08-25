import timeit
events= {"French Revolution":1789,"Industrial":1760,"Greek":1821,"Serbian":1748}
start = timeit.timeit()
x = events[input("Enter the revolution: ")] 
y = events[input("Enter the revolution: ")] 

if x<y:
    x,y =y,x

print("The print the diffrence: ",x-y)
end = timeit.timeit()

print("Time required:",end-start)