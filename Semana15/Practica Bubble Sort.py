def bubble_sort(list_to_sort):
	# Repetimos la iteración de la lista por todos los elementos para moverlos al final
    for outer_index in range(0, len(list_to_sort) - 1):
    # Usamos esta variable para revisar si hemos movido elementos
        has_made_changes = False
		# Le restamos uno al length para parar en el penultimo elemento
    # Usamos el indice exterior para restar las ejecuciones de
    # los elementos que ya estan ordenados al final
    for index in range(0, len(list_to_sort) - 1 - outer_index):
        # Guardamos los valores del elemento actual y el siguiente
        current_element = list_to_sort[index]
        next_element = list_to_sort[index + 1]

        print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')

        # Si el actual es mayor al siguiente, intercambiamos sus posiciones
        if current_element > next_element:
            print('El elemento actual es mayor al siguiente. Intercambiandolos...')
            list_to_sort[index] = next_element
            list_to_sort[index + 1] = current_element
            has_made_changes = True

    # Si no hemos movido elementos, la lista ya esta ordenada
        if not has_made_changes:
            return


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort(my_test_list)

print(my_test_list)