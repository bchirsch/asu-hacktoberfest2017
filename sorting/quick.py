def partition(numbers, low, high):
	i = (low - 1) 	#index of smaller element
	pivot = numbers[high]

	for j in range(low, high):

		if numbers[j] <= pivot:
			# TODO: increment index of the smaller element
                        i = i+1
                        numbers[i], numbers[j] = numbers[j], numbers[i]
                        
	numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
	return(i + 1)

# Main variables
# numbers[] -> array to be sorted
# low -> starting index
# high -> ending index

def quick(numbers, low, high):
	if low < high:
		# pi is the partioning index
		pi = partition(numbers, low, high)
		#recursively call quicksort
                quick(numbers, low, pi - 1)
                quick(numbers, pi + 1, high)
	return numbers;
