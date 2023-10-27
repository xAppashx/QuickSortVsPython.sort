
#Setting up parameters
def QuickSort(ArrayToSort): 
      
      Array = ArrayToSort.copy()
      SortedArray = QuickSortRecursion(Array, 0, len(Array)-1)
      return (SortedArray)
#Def QuickSort


# Will do the recursion part
def QuickSortRecursion(Array, Low, High):
      
      if (Low < High):
            
            Pi = Particiones(Array, Low, High)
            QuickSortRecursion(Array, Low, Pi - 1)
            QuickSortRecursion(Array, Pi+1, High)
      # if
      
      return(Array)
      
#def QuickSortRecursion


# Sorts the array
def Particiones(Array, Low, High):
      
      Lengh = len(Array) 
      Pivot = Array[High]
      Small = Low - 1 
      
      for Loop in range(Low, High):
               
               #Sets up all nums inferior to the pivot to the left of the array
               if (Array[Loop] < Pivot): 
                     Small = Small + 1
                     Temp = Array[Small]
                     Array[Small] = Array[Loop]
                     Array[Loop] = Temp
               #if (Array[Loop] < Pivot)
               
      #For Loop in range
      
      
      #Sets the pivot in its respective spot
      Temp = Array[Small + 1]
      Array[Small + 1] = Array[High]
      Array[High] = Temp
      
      return (Small + 1)
      
# def Particiones
