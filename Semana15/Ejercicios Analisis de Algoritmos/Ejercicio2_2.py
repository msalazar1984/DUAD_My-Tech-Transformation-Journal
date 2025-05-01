def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: #O(n)
		for element_b in list_b: #O(n^2)
			if element_a == element_b:#O(n^2)
				return True           #O(n^2)
				
	return False #O(n^2)

#Este algoritmo es #O(n^2)