

#Make an array for the sorting of the selection 

array = [13, 4, 9, 5, 3, 16, 12] #array

def selectionSort(array): #function statement 


	n = len(array)


	for i in range(n):#<--- whatever the lenght of the array is how many times you are going to run the loop

		#Initially assume the first element of the unsorted part as the minimum

       mininum = i 

       for j in range(i+1, n):

        	if (array[j] < array[mininum]):

        		mininum = j

        
        #Swap the minimum element with the first element of the unsorted part

        temp = array[i]
        array[i] = array[mininum]
        array[mininum] = temp

    return array 

 print(selectionSort(array))

        
         








