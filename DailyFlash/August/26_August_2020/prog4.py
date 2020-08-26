list=  [98,21,76,56,91,13] 

second_largest = [x for x in list if x != max(list) ]

third_largest = max([x for x in second_largest if x != max(second_largest)  ])
print(third_largest)