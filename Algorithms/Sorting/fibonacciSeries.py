def fibonacci_series(end):
	fibonacci_series_list = [0,1]
	for num in range(end):
		fibonacci_series_list.append(fibonacci_series_list[num]+fibonacci_series_list[num+1])
	return fibonacci_series_list

list = fibonacci_series(10)

print(list)