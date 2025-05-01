def generate_list_trios(list_a, list_b, list_c):
	result_list = [] #O(1)
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n^2)
			for element_c in list_c:#O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(n^3)
				
	return result_list #O(n^3)

#Este algoritmo es #O(n^3)