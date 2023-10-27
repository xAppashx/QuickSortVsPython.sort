In one of my previous repositories, I revealed the difference of efficiency between 4 sorting algorithms: Insertion, Bubble, Merge, and Quick sort. The results showed that the Quick Sort was the fastest sorting algorithm out of those 4. Learn more at the following repository: https://github.com/xAppashx/TimeComparaisonOfSortingAlgs

In this repository, we are comparing the efficiency of the Quick sort with Python’s proprietary .sort() method.
This method allows any Python developer to simply sort any given array, without the need of importing any library, nor referencing any extern function. It is extremely convenient and allows us to sort any array with one simple line of code. But how good is it? 

The file called “TimeComparison” puts this .sort() method to the test and compares it with the Quick Sort. We generate an array of controlled length, but containing random values. This allows us to compare the time it takes for both methods to sort an array of length n, whilst creating a realistic, non-biased case for both sorting methods. We then record how much time it took each method to sort the array, and we then repeat this process with an array of length n + 1. 

Plotting all the obtained execution times, we proceed to create a graph that shows visually which of the sorting methods is faster at each n-lengthed array. We can also from that graph recognize a pattern that allows us to estimate the execution time when sorting an array of an even higher length. This graph is present as an annex file called “Result”. 

We can see just how unbelievably faster the .sort() method is compared to my implementation of the Quick Sort. 
This demonstrates that the Quick Sort, despite its name and fame, is still sub-optimal compared to other sorting methods. If you code in Python and ever need to sort an array, the best choice to make is to keep it simple and use the already included .sort() method.
