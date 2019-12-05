#!/usr/bin/env python
# coding: utf-8

# 
# # CS110 Fall 2019 - Assignment 1
# # Divide and Conquer Sorting Algorithms
# 
# This assignment focuses on the implementation of sorting algorithms and analyzing their performance both mathematically (using theoretical arguments on the asymptotic behavior of algorithms ) and experimentally (i.e., running experiments for different input arrays and plotting relevant performance results). 
# 
# Every CS110 assignment begins with a check-up on your class responsibilities and professional standing, as well as your ability to address one of the course LOs #ComputationalSolutions. Thus to complete the first part of this assignment, you will need to take a screenshot of your CS110 dashboard on Forum where the following is visible:
# your name.
# your absences for the course have been set to excused up to session 2.2 (inclusively).
# This will be evidence that you have submitted acceptable pre-class and make-up work for a CS110 session you may have missed. Check the specific CS110 make-up and pre-class policies in the syllabus of the course.
# 
# 
# **NOTES:**
# 
# 1. Your assignment submission needs to include the following resources:
#     * A PDF file must be the first resource. This file must be generated from the template notebook where you have written all of the answers (check this link for instructions on how to do this). Make sure that the PDF displays properly (all text and code can be seen within the paper margins).
#     * Make sure that you submit a neat, clearly presented, and easy-to-read PDF. Please make sure to include page numbers
#     * Your second resource must be the template notebook you have downloaded from the gist provided and where you included your answers. Submit this file directly following the directions in this picture:
# 
# <img src="images/upload.png" width="800" height="200">
# 
# 
# 2. Questions (1)-(7) will be graded on the indicated LOs, please make sure to consult their descriptions and rubrics in the course syllabus. You will not be penalized for not attempting the optional challenge.
# 
# 3. After completing the assignment, evaluate the application of the HCs you have identified prior to and while you were working on this assignment and footnote them (refer to [these guidelines](https://docs.google.com/document/d/1s7yOVOtMIaHQdKLeRmZbq1gRqwJKfezBsfru9Q6PcHw/edit) on how to incorporate HCs in your work). 
# Here are some examples of weak applications of some of the relevant HCs:
# 
#     * Example 1: “#algorithms: I wrote an implementation of the Bubble sort”. 
#         * This is an extremely superficial use of the HC in a course on Algorithms, and your reference will be graded accordingly. Instead, consider what constitutes an algorithm (see Cormen et al, sections 1.1 and 1.2). Once you have a good definition of an algorithm, think of how this notion helped you approach the implementation of the algorithm, analyze its complexity and understand why it’s important to write an optimal python implementation of the algorithm.
#     * Example 2: “#dataviz: I plotted nice curves showing the execution time of bubble sort, or I plotted beautiful curves with different colors and labels.”
#         * Again, these two examples are very superficial uses of the HC #dataviz. Instead consider writing down how do the plots and figures helped you interpret, analyze and write concluding remarks from your experiments. Or write about any insight you included in your work that came from being able to visualize the curves.
#     * Example 3: “#professionalism: I wrote a nice paper/article that follows all the directions in this assignment.” 
#         * By now, you should realize that this is a poor application of the HC #professionalism. Instead, comment on how you actively considered the HC while deciding on the format, length, and style for writing your report.
# 
# 4. Your code will be tested for similarity using Turnitin, both to other students’ work and examples available online. As such, be sure to cite all references that you used in devising your solution. Any plagiarism attempts will be referred to the ASC.
# 
# 
# ** Complete the following tasks which will be graded in the designated LOs and foregrounded HCs:**
# 
# ## Question 1. [HCs #responsibility and #professionalism; #ComputationalSolutions]
# 
# Submit a PDF file with a screenshot of your CS110 dashboard with the information described above.
# 
# 

# 

# ## Question 2. [#SortingAlgorithms, #PythonProgramming, #CodeReadability] 
# 
# Write a Python 3 implementation of the three-way merge sort discussed in class using the code skeleton below. You should also provide at least three test cases (possibly edge cases) that demonstrate the correctness of your code. Your output must be a sorted **Python list**.

# In[2]:


# set all counters to 0

def counters():
    global counter0
    global counter1
    global counter3
    global counter4
    global counter5
    global counter6
    global counter7
    counter0 = 0
    counter1 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0


# In[3]:


# start the counter for the steps counting
counter0=0

def merge (lst, left, mid, right):
    
    ''' 
    MergeSort algorithm is an algorithm that consists of two procedures:
    Merge and Sort. This function will input the whole list (lst), the 
    first index of the subarray (left), the last index of the subarray
    (right), and the length of the sorted subarray (mid), which will be
    merged.
    
    '''
    # counter for the steps
    global counter0
    
    # initialize a list equal to the subarray size
    listSize = [mid[0]-left +1]
    
    # iterate over the length of subarray
    for middlei in range (1, len(mid)):
        
        # add step
        counter0+=1
        
    # append to list size the difference between middle index and the previous element
        listSize.append(mid[middlei] - mid[middlei-1])
        
    # add to the list size the difference between right element and last index
    listSize.append(right - mid[-1])
    
    # array of 0s - the size of the subarray, to be replaced...                      
    array = [[0]*listSize[i] for i in range(len(listSize))]
    
    # add step
    counter0+=len(listSize)
    
    
    # iterate over the subarray length
    for i in range (0, listSize[0]):
        
        # add step
        counter0+=1
        
        # replace the elements in the previous array with elements from the actual list
        array[0][i] = lst[left+i]
                        
    #iterate over the length of subarray to replace elements from the actual list                        
    for ind_Array in range(1, len(array)):
        
        # add step
        counter0+=1
        
        for ind_Key in range(0, listSize[ind_Array]):
            
            # add step
            counter0+=1
            array[ind_Array][ind_Key]=lst[mid[ind_Array-1]+ ind_Key+1]
    
    # add a large element at the end of the list for sorting purposes
    for arr in array:
        
        # add step
        counter0+=1
        arr.append(float("inf"))
                        
    # array of 0s to store the keys of the sublist                      
    indices_array = [0 for i in range(len(array))]
    
    # add step
    counter0+=len(array)
    
    for key in range (left, right+1):
        
        # add step
        counter0+=1   
        
        # assume that the first subarray has the next sorted key
                        
        minimum_now = array[0][indices_array[0]]
        lst[key] = minimum_now
        indices_array[0]+=1
        last = 0
        
        # test the assumption
                        
        for arr_index in range(1, len(array)):
            
            # add step
            counter0+=1
            current_key = array[arr_index][indices_array[arr_index]]
            
            # check if the current key is smaller than the minimum
            if current_key < minimum_now:
                
                # add step
                counter0+=1
                
            # if so, then replace
                minimum_now = current_key
                
            # add this index to the indices array
                indices_array[arr_index] += 1
                
            # remove the last element stored
                indices_array[last] -= 1
                
            # replace with this index
                last = arr_index
                        
    # the minimum element of the list will be places in the rightmost part
        lst[key] = minimum_now
    
    return lst


# In[4]:


# start the counter for steps counting
counter1 = 0

def kWayMerge(lst, left, right, k=3):
    '''
    Implements k-way merge sort, where k is 3, therefore three-way mergesort.
    
    Input:
    lst: a Python list OR numpy array (your code should work with both of these data types)
    left & right: two indexes that are the start and end of a part of an array/
    subarray that will be sorted
    k: the sublists that the algorithm will be creating. Since we need 3-way mergesort
    we set k to 3.
    
    Output: a sorted Python list
    
    '''
    global counter1
    
    # the maximum number of sublist that the algorithm can create
    k_max = right-left+1
    
    # add step
    counter1 +=1 
    
    # if the list has one element, the function terminates
    if k_max <= 1:
        return
    
    # if k that is set is bigger than the list size, set default k
    else:
        if k_max < k:
            k = 3
            
    # find middle indices
        mid_indices = [((_*(right-left))//k) + left for _ in range(1,k)]
        
        #add step
        counter1 += k
        
    # Dynamic+Recursive Programming! Call this funtion (kWayMerge) for k-sublists.
    # Then call merge function to merge the k-sublists.
        kWayMerge(lst, left, mid_indices[0], k)
        kWayMerge(lst, mid_indices[-1] +1, right, k)
        
        for middlei in range(1, len(mid_indices)):
            
            # add step
            counter1+=1
            
            kWayMerge(lst, mid_indices[middlei-1] +1, mid_indices[middlei], k)
    
    return merge(lst, left, mid_indices, right)


# In[5]:


# another generic version of measuring runtime for every function

# i did not use this function because the other one was easier to plot

# however this is more general and it could be used for any given function

'''
import time
import random
def timeIt(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start
orderset = [0,10,100,1000,10000]
timeset_3way = []

for i in orderset:
    randomarray_ext= random.sample(range(10000), i)
    timeset_3way.append(
        timeIt(
            kWayMerge, 
            randomarray_ext, 
            0, 
            len(randomarray_ext)-1, 
            3 
        )
    )
timeset_3way 

'''



# another way to measure time:

# i did not use this function because it does not store time in a list

'''

%time kWayMerge([randomarray], 0, len(randomarray)-1, k)


'''


# In[6]:


# Please ignore this cell. This cell is for us to implement the tests 
# to see if your code works properly. 


# In[7]:


'''
Edge case tests:

'''
counters()

# sorted array
kWayMerge ([1,2,3,4,5,6], 0, 5, 3)
print("Case 2, steps: ",counter1+counter0)

counters ()

# somewhat sorted array
kWayMerge ([1,4,3,2,6,5], 0, 5, 3)
print("Case 2, steps: ",counter1+counter0)

counters ()

# big input size
kWayMerge (([7,2,3,4,1,9]*1000), 0, 5999, 3)
print("Case 3, steps: ",counter1+counter0)


# ## Question 3.  [(#SortingAlgorithms, #PythonProgramming, #CodeReadability, #ComputationalCritique] 
# 
# Implement a second version of a three-way merge sort that calls selection sort when sublists are below a certain length (of your choice) rather than continuing the subdivision process. Justify what might be an appropriate threshold for the input array for applying selection sort.

# In[8]:


# start a counter
counter3 = 0

# create a function which returns a sorted array from selection sorting algorithm
def selectionSort(A):
    
    global counter3
    
    # iterate over the length of the list
    for i in range(len(A)):
        
        minid = i
        
        # add step
        counter3+=1
        
        # iterate from the second element to the length of the list
        for j in range(i+1, len(A)):
            
            # add step
            counter3+=1
            
            # check if current minimum is smaller than the jth index
            if A[minid] > A[j]:
                
                # add step
                counter3+=1
                minid = j
        
        temp = A[i]
        A[i] = A[minid]
        A[minid] = temp
    
    return A


# In[9]:


# start a counter 
counter4 = 0

def extendedThreeWayMerge(lst, left, right, k=3):
    '''
    Implements the second version of a three-way merge sort, while calling selection sort 
    for sorting if the sublist is more than 100.
    
    Input:
    lst: a Python list OR numpy array (your code should work with both of these data types)
    left & right: two indexes that are the start and end of a part of an array/
    subarray that will be sorted
    k: the sublists that the algorithm will be creating. Since we need 3-way mergesort
    we set k to 3.
    
    Output: a sorted Python list
    
    '''
    global counter4
    
    # the maximum number of sublist that the algorithm can create    
    k_max = right-left+1
    
   # add step 
    counter4+=1
    
    # if the list has one element, the function terminates
    if k_max <= 1:
        return
    
    # if the subdivision is smaller or equal to 100, use Selection Sort
    elif k_max <= 100:
        
        # call selection sort
        selectionSort(lst)
        
    else:
        
    # if k that is set is bigger than the list size, set default k
        if k_max <k:
            k=3
            
            # find middle indices
    mid_indices = [((_*(right-left))//k) + left for _ in range(1,k)]
    counter4+=k
    
    # Dynamic+Recursive Programming! Call kWayMerge for k-sublists.
    # Then call merge function to merge the k-sublists.
    
    kWayMerge(lst, left, mid_indices[0], k)
    kWayMerge(lst, mid_indices[-1] +1, right, k)
    
    for middlei in range(1, len(mid_indices)):
        
        # add step
        counter4 +=1
    
        kWayMerge(lst, mid_indices[middlei-1] +1, mid_indices[middlei], k)
        
    return merge(lst, left, mid_indices, right)
    
extendedThreeWayMerge ([8,2,5,4,1,6], 0, 5, 3)


# In[10]:


'''
Edge case tests:

'''
counters()

# sorted array
print(extendedThreeWayMerge ([1,2,3,4,5,6], 0, 5, 3))
print(counter3+counter4+counter1+counter0)

counters()

# somewhat sorted array
print(extendedThreeWayMerge ([1,4,3,2,6,5], 0, 5, 3))
print(counter3+counter4+counter1+counter0)

counters()

# big input size
extendedThreeWayMerge (([7,2,13,18,1,9,5,2,65]*1000), 0, 8999, 3)
print(counter3+counter4+counter1+counter0)


# In[11]:


# Please ignore this cell. This cell is for us to implement the tests 
# to see if your code works properly. 


# ## Question 4 [#SortingAlgorithms, #PythonProgramming, #CodeReadability] 
# 
# Bucket sort (or Bin sort) is an algorithm that takes as inputs an $n$-element array and the number of buckets, $k$, to be used during sorting.  Then, the algorithm distributes the elements of the input array into $k$-different buckets and proceeds to sort the individual buckets. Then, merges the sorted buckets to obtained the sorted array. Here is pseudocode for the BucketSort algorithm:
# 
# <img src="images/bucket.png" width="800" height="200">
# 
# The BucketSort above calls the function **GetBucketNum** (see the pseudocode below) to distribute all the elements of array $A$ into $k$-buckets.  Every element in the array is assigned a bucket number based on its value (positive or negative numbers). **GetBucketNum** returns the bucket number that corresponds to element $A[i]$.   It takes as inputs the element of the array, $A[i]$, the max and min elements in $A$, the size of the intervals in every bucket (e.g., if you have numbers with values between 0 and 100 numbers and 5 buckets, every bucket has an interval of size $20 = [100-0]/5$).  Notice that in pseudocode the indices of the arrays are from 1 to $n$. Thus, GetBucketNum consistently returns a number between 1 and $n$ (make sure you account for this in your Python program).
# 
# <img src="images/getbucketnum.png" width="800" height="200">
# 
# Write a Python 3 implementation of BucketSort that uses the selection sort algorithm for sorting the individual buckets in line 10 of the algorithm.

# In[12]:


# import math library for ceil function
import math

# start a counter
counter5 = 0

def bucketSort(lstt, k):
    """Implements BucketSort
    
    Input:
    lst: a Python list OR numpy array (your code should work with both of these data types)
    k: int, length of lst
    
    Output: a sorted Python list"""
    
    global counter5
    
    # assign the minimum value of the list
    minimum_bs = min(lstt)
    
    # assign the maximum value of the list
    maximum_bs = max(lstt)
    
    # find the bucket size
    size_bs = math.ceil((maximum_bs-minimum_bs)/k)
    
    # create an empty list to be filled later
    sorted_array_bs = []
    
    # create a list of 0s to the size of k
    buckets_bs = [0]*k
    
    #iterate over k
    for i in range(k):
        
        # replace with the empty list 
        buckets_bs [i] = []
        
        # add step
        counter5+=1
        
    # iterate over lstt
    for i in lstt:
        
        # add step
        counter5+=1
        
        # call the function of getting bucket number
        funct = GetBucketNum(i,minimum_bs,maximum_bs,size_bs,k)
        
        # append it to the empty list
        buckets_bs[funct].append(i)
   
    # iterate over k
    for i in range(k):
        
        # add step
        counter5+=1
        
        # call the selection sort function, which was used before
        buckets_bs[i] = selectionSort(buckets_bs[i])
        
    # iterate over k
    for i in buckets_bs:
        
        # add step
        counter5+=1
        
        # iterate over i 
        for j in i:
            
            # add a step
            counter5+=1
            
            # append to the sorted array
            sorted_array_bs.append(j)
            
    return sorted_array_bs

# start step counting
counter6 = 0

def GetBucketNum(x,minimum_bs,maximum_bs,size_bs,k):
    
    global counter6
    
    counter6+=1
    
    # check if x is maximum, if so, remove one element from k
    if x == maximum_bs:
        j = k-1
    
    # check if x is minimum, if so, j is set to 0
    elif x == minimum_bs:
        j = 0
    
    # otherwise, j will be appended elements, until x is bigger than the maximum
    else:
        j = 0
        
        while x > minimum_bs+(size_bs*j):
            counter6+=1
            j = j+1
        j=j-1
    return j


A = [2,11,11,12,3,55,52,99,88,11,45,32,77,99,32,65,81]
bucketSort(A,10)


# In[13]:


'''
Edge case tests:
'''

counters()

# sorted array
bucketSort([1,2,3,4,5,6], 4)
print("Case 1, steps: ",counter3+counter5+counter6)

counters()

# somewhat sorted array
bucketSort ([1,4,3,2,6,5], 4)
print("Case 2, steps: ",counter3+counter5+counter6)

counters()

# big input size
bucketSort (([56,2,67,4,1,9]*1000), 20)
print("Case 3, steps: ",counter3+counter5+counter6)


# In[14]:


# Please ignore this cell. This cell is for us to implement the tests 
# to see if your code works properly. 


# ## Question 5 [#SortingAlgorithms, #PythonProgramming, #CodeReadability] 
# 
#  Implement a second version of the BucketSort algorithm. This time in line 10 of BucketSort use the Bucket sort recursively until the size of the bucket is less than or equal to k, the base case for the recursion.
# 
# 

# In[15]:


counter7=0
def extendedBucketSort(lstt, k):
    """Implements the second version of the BucketSort algorithm
    
    Input:
    lst: a Python list OR numpy array (your code should work with both of these data types)
    k: int, length of lst
    
    Output: a sorted Python list"""
# it is the same function as bucketSort except that it calls selectionSort 
# to sort each bucket
    global counter7
    
    minimum_bs = min(lstt)
    maximum_bs = max(lstt)
    size_bs = math.ceil((maximum_bs-minimum_bs)/k)
    sorted_array_bs = []
    buckets_bs = [0]*k
    
    for i in range(k):
        counter7+=1
        buckets_bs[i] = []

    for i in lstt:
        counter7+=1
        funct = GetBucketNum(i,minimum_bs,maximum_bs,size_bs,k)
        buckets_bs[funct].append(i)
    
    for p in range(k):
        counter7+=1
        if buckets_bs[p] != []:
            counter7+=1
            buckets_bs[p] = bucketSort(buckets_bs[p],2*k-p)

    for i in buckets_bs:
        counter7+=1
        for j in i:
            counter7+=1
            sorted_array_bs.append(j)
    return sorted_array_bs
extendedBucketSort(A,len(A))


# In[16]:


'''
Edge case tests:
'''

counters()

# sorted array
bucketSort([1,2,3,4,5,6], 4)
print("Case 1, steps: ",counter3+counter5+counter6+counter7)

counters ()

# somewhat sorted array
bucketSort ([1,4,3,2,6,5], 4)
print("Case 2, steps: ",counter3+counter5+counter6+counter7)

counters()

# big input size
bucketSort (([56,2,67,4,1,9]*1000), 20)
print("Case 3, steps: ",counter3+counter5+counter6+counter7)


# In[17]:


# Please ignore this cell. This cell is for us to implement the tests 
# to see if your code works properly. 


# ## Question 6 [#ComplexityAnalysis, #ComputationalCritique] 
# 
# Analyze and compare the practical run times of regular merge sort (i.e., two-way merge sort), three-way merge sort, and the extended merge sort from (3) by producing a plot that illustrates how every running time and number of steps grows with input size. Make sure to:
# 1. define what each algorithm's complexity is
# 2. enumerate the explicit assumptions made to assess each run time of the algorithm's run time.
# 3. and compare your benchmarks with the theoretical result we have discussed in class.
# 

# In[18]:


# set all counters to 0

def counters():
    global counter0
    global counter1
    global counter3
    global counter4
    global counter5
    global counter6
    global counter7
    counter0 = 0
    counter1 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0


# In[22]:


import time
import numpy as np
import matplotlib.pyplot as plt 

x1, y1, x2, y2, x3, y3 = [],[],[],[],[],[] 
y4, y5, y6 = [],[],[] 
elem_num = np.random.randint(1000, 10000, 100) 
elem_num= selectionSort(elem_num)
    
for z in elem_num:
    array_graph = list(range(z))
    np.random.shuffle(array_graph)
    
    counters()
    start = time.time()
    kWayMerge(array_graph,0,z-1,3)
    end = time.time()
    y1.append(end-start) 
    x1.append(z)
    y4.append (counter0+counter1)

    
    counters()
    start = time.time()
    extendedThreeWayMerge(array_graph,0,z-1,3)
    end = time.time()
    y2.append(end-start) 
    x2.append(z)
    y5.append(counter0+counter1+counter3+counter4)
    
    counters()
    start = time.time()
    kWayMerge(array_graph,0,z-1,2)
    end = time.time()
    y3.append(end-start) 
    x3.append(z)
    y6.append (counter0+counter1)
    
    
plt.plot(x1,y1, label = "3-Way Merge")
plt.plot(x2,y2, label = "Extended K-Merge") 
plt.plot(x3,y3, label = "2-Way Merge") 
plt.xlabel("Input")
plt.ylabel("Time")
plt.legend()
plt.show()

plt.plot(x1, y4, label = "3-Way Merge") 
plt.plot(x2, y5, label = "Extended K-Merge") 
plt.plot(x3, y6, label = "2-Way Merge") 
plt.xlabel("Input")
plt.ylabel("Steps")
plt.legend()
plt.show()


# **Merge Complexity**
# 
# By the end of the merge function, there are two-for loops. Loops run k-times, which is the number of sublists we have. So, neglecting the smaller operations we can say that the complexity is $\Theta(k*n)$. However there are two scenarios; k can be a constant or equal to n. When k is equal to n, then complexity changes drastically to  $\Theta(n^2)$. So, usually merge will have average case of $\Omega(n)$ and  worst-case of $O(n^2)$.

# **K-Way MergeSort**
# 
# This function splits the list into k-number of smaller lists. The maximum splits that this function can make is n, which means each element of the list is put into a list alone. From the merge function, to calling itself, we spot the recursiveness in this function which results in:
# 
# $$T(n) = k*T(n/k) + \Theta(n).$$
# 
# If we apply a=b=k Theorem, the relation takes the shape of: $$n^{\log_ba} = n^{\log_kk} = n.$$ which then results to:
# 
# $T(n) = \Theta(n^{\log_ba}*\log_k n) = \Theta(n*\log_k n)$.
# 
# 

# **Three-Way MergeSort and Two-Way MergeSort**
# 
# Since Three-Way MergeSort and Two-Way MergeSort are special cases, from the formula above, we can extract the time complexity for both.
# 
# **Three-Way MergeSort**
# 
# $$T(n) = 3T(n/3) + O(n)  {\displaystyle \Rightarrow }  
# O (n log_3 n) $$
# 
# 
# 
# 
# **Two-Way MergeSort**
# 
# $$T(n) = 2T(n/2) + O(n)  {\displaystyle \Rightarrow } 
# O (n log_2 n)$$

# **Extended Three-Way MergeSort**
# 
# This function is Three-Way MergeSort with a tweak; we use selection sort algorithm to sort a given subarray. Therefore, it depends on the number of subarrays how time-complexive this algorithm might be. We expect it to be no much more different from Three-Way Merge Sort, especially when k is bigger, and Selection Sort is not called. When k is smaller, than it might perform a little bit more slower than the simple Three-Way MergeSort, because of Selection Sort Time Complexity. We need to find the optimal threshold to make it perform better.

# In[20]:


# IMPLEMENTATION PURPOSES


# ## Question 7. [#ComplexityAnalysis, #ComputationalCritique] 
# 
# Analyze and compare the practical run times of regular merge sort (i.e., two-way merge sort), Bucket sort and recursive sort from (5) by producing a plot that illustrates how each running time grows with input size. Make sure to:
# 1. define what each algorithm's complexity is
# 2. enumerate the explicit assumptions made to assess each run time of the algorithm's run time.
# 3. and compare your benchmarks with the theoretical result we have discussed in class.
# 

# In[21]:


# RuntimeBucketSort
x1, y1, x2, y2 = [],[],[],[]



for z in elem_num:
    array_graph = list(range(z))
    np.random.shuffle(array_graph)
    start = time.time()
    bucketSort(array_graph,1000)
    end = time.time()
    y1.append(end-start) 
    x1.append(z)
    start = time.time()
    extendedBucketSort(array_graph,1000)
    end = time.time()
    y2.append(end-start) 
    x2.append(z)
    
plt.plot(x1,y1, label = "Bucket Sort") 
plt.plot(x2,y2, label = "Extended Bucket Sort") 
plt.xlabel("Input")
plt.ylabel("Time")
plt.legend()
plt.show()


# **Bucket-Sort and its extended form**
# 
# In Bucket Sort we assume that the elements of the list are distributed uniformly, and the complexity depends on the number of buckets. If we find the most optimal way to assign elements to buckets, this algorithm is very efficient. 
# 
# So the average time complexity is:
# 
# $ O (n+k) $ 
# 
# while the worst case scenario is: 
# 
# $O(n ^2)$
# 
# which also explains the Extended Bucket Sort scenario.
# 
# 

# ## [Optional challenge] Question 8 (#SortingAlgorithm and/or #ComputationalCritique) 
# 
# Implement k-way merge sort, where the user specifies k. Develop and run experiments to support a hypothesis about the “best” value of k.

# I have implemented Three-Way MergeSort as a special case of K-Way MergeSort, so the first answer explains both the optional challenge and the first question. 
# 

# In[ ]:




