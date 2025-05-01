def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)   #O(n)
	for index in range(min(list_len, 10)): #O(n)
		print(list_to_print[index]) #O(n)

#Este algoritmo es O(n)