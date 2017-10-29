def insertion(numbers):
        for i in range(1, len(numbers)):
		j = i
                #While loop to check if previous element is larger 
                #If previous element is smaller, continue traversing
		while j > 0 and numbers[j-1] > numbers[j]:
                        #Swap elements, decrement j
                        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                        j -= 1
	return numbers
