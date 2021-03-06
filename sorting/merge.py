def merge(numbers, l, m, r):

	n1 = m - 1 + 1
	n2 = r - m

	# temp
	L = [0] * (n1)
	R = [0] * (n2)

	for i in range (1, n1):
		# TODO: copy data to temp array L[]
		L[i] = numbers[l + i - 1]

	for j in range(1, n2):
		# TODO: copy data to temp array R[]
		R[j] = numbers[m + j]

	i = 0		# initial index of first subarray
	j = 0		# initial index of second subarray
	k = l 		# initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] < R[j]:
			# TODO: set array index k equal to L[i]
			numbers[k] = L[i]
			i = i + 1
		else:
			# TODO: set array index k equal to R[j]
			numbers[k] = R[j]
			j = j + 1
		k += 1

	while i < n1:
			# TODO: copy remaining elements of L[] into numbers[k]
			numbers[k] = L[i]
			# TODO: increment k and i
			i = i + 1
			k = k + 1

	while j < n2:
			# TODO: copy remaining elements of R[] into numbers[k]
			numbers[k] = R[j]
			# TODO: increment k and j
			j = j + 1
			k = k + 1

def mergesort(numbers, l, r):

	if l < r:

		# find middle point
		m = (l+r)//2

		# TODO: sort first and second halves
		mergesort(numbers,l,m)
		mergesort(numbers,m+1,r)
		merge(numbers, l, m, r)

	return numbers;
