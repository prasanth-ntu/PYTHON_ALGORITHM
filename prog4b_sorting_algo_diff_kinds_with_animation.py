''''

 Title              : An animation of random data with different sorting algo
 Purpose:           : An imrovised and live animation - Better than pyplot implemented earlier 
 Version            : 2
 Version changes    : 1.Added list size as additional argument
                    : 2. marker shapre and color will be randomly selected by algo)
 Instruction        : argv[0] - Type of algo to choose
                    : argv[1] - No of items to be sorted
                    : argv[2] - Speed of exexcution
 Author             : Prasanth (prasanth007@e.ntu.edu.sg)
 Date last mod      : 7 Aug 2017
 Reference [1]      : https://matplotlib.org/examples/animation/random_data.html
'''

DEBUG = False

#========================
#       ANIMATION
#=========================
import numpy as np
import matplotlib.pyplot as plt
# The easiest way to make a live animation in matplotlib is to use one of the Animation classes.
import matplotlib.animation as animation
from random import shuffle, choice
from time import sleep

fig, ax = plt.subplots()             # Create a figure (640x480) object and a AxesSubplot object with Axes(0.125,0.11;0.775x0.77)

# These line variable is initialised here. Later, it will be updated in main() function
L = []
line, = ax.plot(L, 'r+')             # An arbitrary no of (x,y) groups can be specified 
#ax.set_ylim(0,len(L))
plt.xlabel("index")
plt.ylabel('value [index]')

def update(data):
    """
    DESCRIPTION:
        The function to call at each frame
    ARGUMENT 1:
        The next value in frames
    """
    line.set_ydata(data)
    return line,

def data_gen():
    """
    DESCRIPTION:
        Source of data to pass 'func' update and each frame of the animation
        In our case, it's a generator function
    """
    while True:
        #yield np.random.rand(100)
        data = [1,2,3,4,5,6,7,8,9,10]
        print (data)
        yield data


#========================
#       MONKEY SORT
#=========================
def monkeySort(L):
    
    plt.title("MONKEY SORTING ALGO", color='blue', fontweight = 'bold')
    iteration_text = ax.text(.78, 1.02, '', transform=ax.transAxes)

    iteration = 0

    # if the list is not sorted, you keep sorting them randomly

    # BEST CASE: O(n) where n = len(L)
    # WORST CASE: Unbounded
    while not sorted(L) == L:
        iteration += 1
        shuffle(L)
        #print (L)
        #BUGGY #plt.text(.5,.5 , str(iteration))
        #BUGGY #plt.annotate(str(iteration), xy = (5.7,5.7))
        iteration_text.set_text('iterations= %d' % iteration)
        yield (L)


    plt.text(0,len(L)-.1*len(L),"Finished sorting", color = "green")
    
    while True:
        yield L
        
        if DEBUG: print ("DEBUG:", "Finishing sorting")
        if DEBUG: print ("DEBUG:", "No of while loop iterations:", iteration)

        ani.event_source.stop()
        #plt.close('all')

#========================
#       BUBBLE SORT
#=========================
def bubbleSort(L):                          # O(n*n) = O(n^2) where n - len(L)
    if DEBUG: print ("DEBUG:", "Beginning sorting")

    plt.title("BUBBLE SORTING ALGO", color='blue', fontweight = 'bold')

    swappingPerformed = True
    # Does multiple passing until no more swaps
    while swappingPerformed:                # O(len(L)-1) - Outer loop iterations
        swappingPerformed = False
        # Performs comparisons & swapping
        for i in range(len(L)-1):           # O(len(L)-1) for every iter of outer loop- 
            if L[i] > L[i+1]:
                swappingPerformed = True
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
            
        if DEBUG: print ("DEBUG:", "List being sorted:", L)
        yield L

    plt.text(0,len(L)-.1*len(L),"Finished sorting", color = "green")
        
    while True:
        yield L
        if DEBUG: print ("DEBUG:", "Finishing sorting")
        ani.event_source.stop()
        #plt.close('all')

#========================
#       SELECTION SORT
#=========================
def selectionSort(L):
    plt.title("SELECTION SORTING ALGO", color='blue', fontweight = 'bold')
        
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        if DEBUG: print ("DEBUG", "List being sorted", L)
        yield(L)

    plt.text(0,len(L)-.1*len(L),"Finished sorting", color = "green")

    while True:
        yield L
        if DEBUG: print ("DEBUG:", "Finishing sorting")
        ani.event_source.stop()
        #plt.close('all')


# interval - Delay between frames in milliseconds
#ani = animation.FuncAnimation(fig, update, bubbleSort(L[:]), interval=30)
#plt.show()


#========================
#       MERGE SORT
#=========================
# GLOBAL VARIABLE
mergeSortResult = []

def mergeSort(L):           # O(log(len(L))), as at each recursion, the problem is broken half
    """
    INPUT: L (unsorted list)
    RETURN: A sorted list
    DESCRIPTION:
        - Depth Firt Search => Conquer smallest piece down before moving to the larger pieces
    """
    global mergeSortResult
    
    # [BASE CASE] if the list of length 0 or 1, it's already sorted
    if len(L) < 2:
        return L[:]
    # if the list has 2 or more elements, split into 2 lists and sort each (RECURSIVELY)
    else:
        # this finds the mid point of the list so that we can divide in to 2 halves
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        L = merge(left,right)

        # GLOBA:L VARIABLE where the results from this function are stored
        mergeSortResult.append(L)
                    
        if DEBUG: print (L)
        return L
        

def merge(left, right):         # O(len(L)), where L is the longest list => Linear growth 
    """
    INPUT: left, right (sorted lists)
    RETURN: combined sorted list of left and right
    """
    mergedList = []
    i, j = 0, 0

    # Look for smaller element in each list and move them to the right of the new list
    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            mergedList.append(left[i])
            i += 1
        else:
            mergedList.append(right[j])
            j += 1

    # when right sublist is empty
    while i < len(left):
        mergedList.append(left[i])
        i += 1

    # when left sublist is empty
    while j < len(right):
        mergedList.append(right[j])
        j += 1

    return mergedList


def mergeSortResults(L):
    """
        HELPER FUNCTION TO PLOT THE RESULTS ONTO THE CHART
        I used this function as the mergeSort algo uses recurive call & performs DFS
        
        This function calls the mergeSort algo;
        collates the result from the merge sort algo using a global variable;
        does some tweaks to the merge sort result so that it can be presented on the screen
        & it nicely plots the results in the chart
    """
    if DEBUG: print ("Actual LIST:", L)
    result= mergeSort(L[:])
    if DEBUG: print ("SORTED LIST:", result)

    mergeSortResultModified = [mergeSortResult[0]]
    if DEBUG: print (mergeSortResultModified)

    # In this loop, we extract the info from 'mergeSortResult' & reformat it in 'mergeSortResultModified'
    for sortedList in mergeSortResult[1:]:
        tempList = mergeSortResultModified[-1][:]
        if DEBUG: print ("templist:", tempList)
        for itemToDelete in sortedList:
            if itemToDelete in tempList:
                tempList.remove(itemToDelete)
        for itemToAdd in sortedList:
            tempList.append(itemToAdd)
        mergeSortResultModified.append(tempList)
        if DEBUG:
            print ("mergeSortResultModified last index value:", mergeSortResultModified[-1])
            print ("len(mergeSortResultModified):", len(mergeSortResultModified))

    # In this loop, we extract the info from 'mergeSortResultModified' & do some padding and
    #   store it into 'finalSortedResults'
    finalSortedResults = mergeSortResultModified[:]
    for index in range(len(mergeSortResultModified)):
        if DEBUG: print ("BEFORE APPENDING:", mergeSortResultModified[index])
        for itemToAppend in L[:]:
            if itemToAppend not in mergeSortResultModified[index]:
                finalSortedResults[index].append(itemToAppend)
        if DEBUG: print ("AFTER APPNEDING:", finalSortedResults[index])

    plt.title("MERGE SORTING ALGO", color='blue', fontweight = 'bold')

    for sortedList in mergeSortResultModified:
        if DEBUG: print (sortedList)
        yield (sortedList)

    plt.text(0,len(L)-.1*len(L),"Finished sorting", color = "green")
    
    while True:
        yield (sortedList)
        ani.event_source.stop()
        #plt.close('all')


#ani = animation.FuncAnimation(fig, update, mergeSortResults(L), interval=50)
#plt.show()  

#========================
#       MAIN
#=========================
def main():
    import sys, string, random

    global n

    # First argument is the sorting algo to choose (NO DEFAULT, RANDOMLY SELECTED
    if sys.argv[1:2]:
        a = int(sys.argv[1])
    else:
        a = random.randint(1,4)

    if sys.argv[3:]:
        inMilliSecond = int(sys.argv[3])
    else:
        inMilliSecond = 50

    if sys.argv[2:]:
        n = int(sys.argv[2])
    else:
        n = 200
    
    global L, line

    # Generate a list of 'n' integers statring from 0 to n-1 and shuffle them
    L = [i for i in range(n)]
    shuffle(L)

    # Randomly choose a marker color and style
    markerColor = random.choice(['b','g', 'r', 'c', 'm', 'y', 'b'])
    markerStyle = random.choice(['x', '+', '.', '2', '*', 'd', '_', '|'])
    line, = ax.plot(L, markerColor+markerStyle)             # An arbitrary no of (x,y) groups can be specified 
    ax.set_ylim(0,len(L))
    plt.xlabel("index")
    plt.ylabel('value [index]')
    
    # Create the graphical objects...
    if a == 1:
        ani = animation.FuncAnimation(fig, update, monkeySort(L), interval=inMilliSecond)
    elif a == 2:
        ani = animation.FuncAnimation(fig, update, bubbleSort(L), interval=inMilliSecond)
    elif a ==3:
        ani = animation.FuncAnimation(fig, update, selectionSort(L), interval=inMilliSecond)
    elif a == 4:
        ani = animation.FuncAnimation(fig, update, mergeSortResults(L), interval=inMilliSecond)
    else:
        ani = animation.FuncAnimation(fig, update, mergeSortResults(L), interval=inMilliSecond)

    # ...and run!
    plt.show()

# Call main when run as script
if __name__ == '__main__':
    main()
