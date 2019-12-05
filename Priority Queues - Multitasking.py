
# coding: utf-8

# ○ Prepare a table containing a list of all the activities that you plan to do in the city of your
# rotation, with a short, compelling justification why they are interesting. Make sure you
# plan activities that involve visiting landmarks or other locations that highlight particular
# socio-culture aspects of the rotation city where you are. An activity is decomposed in a set of tasks which are exclusively of a cultural nature (not routine nor academic). Your
# assignment needs to include:
# 
# ■ at least 5 activities, and each activity can be subdivided into 3 to k tasks.
# 
# ■ At least 10 tasks on your list need to be a multitasking type of tasks.

# In[1]:


# import tabulate for plotting a neat table 

from tabulate import tabulate

# name the activities and decriptive information about them

activities = [['Hanok Village Visit', 'Beautiful traditional houses and clothings', '1,2,3,6,10'],
              ['N Seoul Tower', 'A good view of Seoul from the top of the Namsan Mountain','1,4,5,6,9'],
              ['Namdaemun Market', 'Cheap prices for authentic Korean fruit', '2,6,7,8,12'],
              ['Korean BBQ', 'Typical restaurant of Korea', '6,11,14,15,17'],
              ['KPop Karaoke', 'Listen and sing Korean Music', '3,6,11,13,16']]

# name the headers

headers = ['Activity', 'Reason of visit', 'Tasks to complete (see table below)']

# create a function to produce the table so that I can update it 

def showTable0():
    print(tabulate([tuple(x) for x in activities], headers=headers, tablefmt="fancy_grid"))
showTable0()

               


# In[3]:


# create the tasks and important descriptive information

### priorities to be updated ###

mydata = [[1, "T Money Card Recharge ", 5, "No", 0, 0, 0],
          [2, "Activate KakaoMap/Naver App", 1, "Yes", 0, 0,0],
          [3, "Take a bus", 30, "Yes", 1, 0,0],
          [4, "Buy a ticket for N Seoul Tower", 10, "No", 2, 0,0],
          [5, "Buy a CableCar Ticket", 10, "No", 2, 0,0],
          [6, "Exchange Currency to Won", 7, "No", 1, 0,0],
          [7, "Bring the shopping list", 0.5, "Yes", 0, 0,0],
          [8, "Bring a tote bag", 0.5, "Yes", 0, 0,0],
          [9, "Visit around N Seoul Tower", 60, "Yes", 7, 0,0],
          [10, "Roam around Hanok Village", 80, "Yes", 6, 0,0],
          [11, "Invite friends", 1, "Yes", 0, 0,0],
          [12, "Shopping/Namdaemun Market", 90, "Yes", 9, 0,0],
          [13, "Bring ARC [Korean ID]", 0.5, "Yes", 0, 0,0],
          [14, "Activate Google Translate App", 1, "Yes", 0, 0,0],
          [15, "Eat at KBBQ", 90, "Yes", 7, 0,0],
          [16, "Sing/Listen to Kpop at Karaoke", 90, "Yes", 8, 0,0],
          [17, "Take pictures", 15, "Yes", 0, 0,0]]

# create the headers of the table

headers = ['Task ID', 'Task Description', 'Task Duration', 'Multitasking', 'Dependencies', 'Status', 'Priority']

# create a function to show the table so I can reuse it to update

def showTable():
    print(tabulate([tuple(x) for x in mydata], headers=headers, tablefmt="fancy_grid"))
showTable()


# In[4]:


'''
Extract important data from the dataset created.
Tasks will be accessed by TASK ID.
'''

# turn tuple into a list
a = list(list(mydata))

# task ID
task_ID = [mydata[i][0] for i in range(17)]

print ('Task ID:', task_ID)

# task names

task_name = [mydata[i][1] for i in range(17)]

print ('Task Name:', task_name)

# task times
task_time = [mydata[i][2] for i in range(17)]

print ('Task Times:', task_time)

# multitasking tasks
multitasking = [mydata[i][3] for i in range(17)]

# dependencies
dependencies = [mydata[i][4] for i in range(17)]

# task status
status = [mydata[i][5] for i in range(17)]

print ('Task Status:', status)


# store multitasks task in multitask
multitask = []

# store nonmultitask tasks in nonmultitask
nonmultitask = []

for i in range(len(multitasking)):
    if multitasking[i]=='Yes':
        multitask.append(i+1)
    if multitasking[i]=='No' :
        nonmultitask.append(i+1)
    

print ('Multitasking possible (Task ID):', multitask)
print ('Multitasking not possible (Task ID):', nonmultitask)


# store dependent tasks in dependent
dependent = []

# store independent tasks in independent
independent = []

for i in range(len(dependencies)):
    if dependencies[i]==0:
        independent.append(i+1)
    else:
        dependent.append(i+1)
        
print ('Dependent tasks (Task ID):', dependent)
print ('Independent tasks (Task ID):', independent)
        

    


# ○ For multitasking tasks, how would you determine the optimal partitioning time? Test at
# least 2 different values or strategies and analyze their computational behavior.

# In[ ]:


# possible combination
impossible = [] 
best = []
secondbest = []

# time given
time=int(input('time:'))

def combinations(time): 
    '''
    This function inputs the time given by the user, and under the constraints of time, outputs the best
    multitasking combination in the given time.
    '''
    for i in multitask:
        for j in multitask:
            if mydata[i-1][2]==time and mydata[j-1][2]==time:
                bestcombi=[i+1,j+1]
                best.append(bestcombi) 
                if (mydata[i-1][2]==time or mydata[j-1][2]==time) and not(mydata[i-1][2]>time and mydata[j-1][2]>time) :
                    combination=[i+1,j+1]
                    secondbest.append(combination)  
            else:
                if mydata[i-1][2]!=time and mydata[j-1][2]!=time and mydata[i-1][2]>time and mydata[j-1][2]>time:
                        combi = [i+1,j+1]
                        impossible.append(combi)
    if best != []:
        return (print('Optimal tasks to be done:', best))
    else:
        if secondbest != []:
            return (print('Optimal tasks to be done:', secondbest))
        else: 
            return (print('There are no task you can finish completely now, but you can choose to do', time, ' minutes' 
                                  ' of the following combination' , impossible))
                
combinations(time)
            



    


# ### Answer: ###
# 
# This approach takes an input of time from the user. Under the constraints of time, it chooses from the list of multitasking tasks and it attempts to find the perfect combination of two tasks that take exactly the same time as the input given, and conduct them simultaneously. The algorithm assumes that the only two tasks can be multitasked at once (I have chosen this limit not to add to the complexity of time, as it already loops twice over the list.). It also assumes that conducting two tasks at once, if they are part of the multitasking list, will only take as much time as the task with the highest time takes (for instance, if task 1 takes 20 minutes, and task 2 takes 30 minutes, doing both task 1 and 2 simultaneously will take 30 minutes.).
# 
# 
# Limitation: The algorithm is not telling the user how to chunk the time, in case if there is no good combination of tasks. There is also repetition of the same task as a combination (task 10, task 10). I tried to debug the code by not letting i!=j be the same, but I ended up never having the combination of i==j==time, which I considered to be optimal. This bug could be addressed furthermore with the help of indexing inside the list.
# 
# 
# 
# 1. Take time input.
# 
# 2. Iterate over the list of multitask, filtered for time, and check if any two elements are equal to the given time.
# 
# *If yes*: 
#     
# Then append to the list of best combinations.
# 
# 
# *If not*:
# 
# Then check if one is equal to time and the others are not bigger than given time.
# 
# Then append to the list of second best combination.
# 
# 
# *Else*: 
# 
# Check two bigger tasks than time given and warn the user that he will not be able to finish everything.
# 
# 3. Output the best option first if it's not empty. 
# 4. If the best option is empty, output the second best, and if that is empty output the tasks that need to be chunked.
# 
# 
# 
#     
# 

# ### Part D [#PythonProgramming, #CodeReadability] ###
# ○ Write a Task Priority Scheduler in Python 3, which receives the list of tasks above as
# input and returns an optimal task schedule for you to follow. Please refrain from using
# any external Python library besides the random module.

# In[ ]:


# a given list of tasks
tasks = [1,2,3,4]


def prioritize (tasks):    
    '''
    This function is used to update priorities in a table.
    
    Input: A data structure that has the same columns as the table of tasks created in Part B.
    Output: Priorities assigned to each task. 
    
    '''
    for i in range(0, len(tasks)):
        priority = tasks[i][4] * 10000
        priority+=tasks[i][2]
        tasks[i][6] = priority
        
prioritize(mydata)
showTable()

# create a storage of priorities for the tasks in the given list

priorities1= [mydata[i][6] for i in range(len(tasks))]






# In[6]:


# Defining some basic binary tree functions
#
def left(i):         # left(i): takes as input the array index of a parent node in the binary tree and 
    return 2*i + 1   #          returns the array index of its left child.

def right(i):        # right(i): takes as input the array index of a parent node in the binary tree and 
    return 2*i + 2   #           returns the array index of its right child.

def parent(i):       # parent(i): takes as input the array index of a node in the binary tree and
    return (i-1)//2  #            returns the array index of its parent


# Defining the Python class MaxHeapq to implement a max heap data structure.
# Every Object in this class has two attributes:
#           - heap : A Python list where key values in the max heap are stored
#           - heap_size: An integer counter of the number of keys present in the max heap
class MaxHeapq:
    """ 
    This class implements properties and methods that support a max priority queue data structure
    """  
    # Class initialization method. Use: heapq_var = MaxHeapq()
    def __init__(self):        
        self.heap       = []
        self.heap_size  = 0

    # This method returns the highest key in the priority queue. 
    #   Use: key_var = heapq_var.max()
    def maxk(self):              
        return self.heap[0]     
    
    # This method implements the INSERT key into a priority queue operation
    #   Use: heapq_var.heappush(key)
    def heappush(self, key):   
        """
        Inserts the value of key onto the priority queue, maintaining the max heap invariant.
        """
        self.heap.append(-float("inf"))
        self.increase_key(self.heap_size,key)
        self.heap_size+=1
        
    # This method implements the INCREASE_KEY operation, which modifies the value of a key
    # in the max priority queue with a higher value. 
    #   Use heapq_var.increase_key(i, new_key)
    def increase_key(self, i, key): 
        if key < self.heap[i]:
            raise ValueError('new key is smaller than the current key')
        self.heap[i] = key
        while i > 0 and self.heap[parent(i)] < self.heap[i]:
            j = parent(i)
            holder = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = holder
            i = j    
            


# In[ ]:


class MinHeapq:
    #Min-Heap class
    def __init__(self):        
        self.heap       = []
        self.heap_size  = 0

    # This method returns the smallest key in the priority queue. 
    def mink(self):              
        return self.heap[0]     
    
    # This method implements the INSERT key into a priority queue operation
    def heappush(self, key):   
        """
        Inserts the value of key onto the priority queue, maintaining the max heap invariant.
        """
        self.heap.append(float("inf"))
        self.decrease_key(self.heap_size,key)
        self.heap_size+=1
        
    # This method implements the INCREASE_KEY operation, which modifies the value of a key
    # in the min priority queue with a smaller value. 
    def decrease_key(self, i, key): 
        if key > self.heap[i]: #main difference with the maxheapq (sign)
            raise ValueError('new key is bigger than the current key')
        self.heap[i] = key
        while i > 0 and self.heap[parent(i)] > self.heap[i]: #main difference with the maxheapq (sign)
            j = parent(i)
            holder = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = holder
            i = j    
            
    # This method implements the MIN_HEAPIFY operation for the MIN priority queue. The input is 
    # the array index of the root node of the subtree to be heapify.        
    def heapify(self, i): #same code as in previous pre-works
        l = left(i)
        r = right(i)
        heap = self.heap
        if l <= (self.heap_size-1) and heap[l]<heap[i]: #main difference with the maxheapq (sign)
            smallest = l
        else:
            smallest = i
        if r <= (self.heap_size-1) and heap[r] < heap[smallest]: #main difference with the maxheapq (sign)
            smallest = r
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(smallest)

    # This method implements the EXTRACT_MIN operation. It returns the smallest key in 
    # the min priority queue and removes this key from the min priority queue.
    def heappop(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        mink = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_size-=1
        self.heapify(0)
        return mink


# In[8]:


# heapify the list of priorities while using MinHeap

priorities_heapified = MinHeapq()

for key in priorities1:
    priorities_heapified.heappush(key)

# print heapified list of priorities 
print('Heapified list of priorities for the given task list:', priorities_heapified.heap)

# create an empty array of prioritized tasks
tasks_prioritized = [0 for i in range(len(tasks))]

# sort tasks accordingly to their priorities
for e in priorities_heapified.heap :
    idx = priorities1.index(e)
    tasks_prioritized[priorities_heapified.heap.index(e)] = tasks[idx]

    
print ('Order of tasks:', tasks_prioritized)

# order of tasks 

for e in tasks_prioritized:
    print (mydata[e-1][1])
    
times_added = [mydata[i-1][2] for i in tasks_prioritized]
print ('Time for execution:',sum(times_added), 'minutes')






# ### Answer: ###
# 
#  Scheduler takes a list of tasks and gives priority based on dependencies and time. After all the tasks have been assigned the specific priority, it takes the priorities of the given list of tasks, and it heapsorts its priorities. Once it heapsorts its priorities, it sorts the list of tasks as well, accordingly to priorities. The last output is the order of tasks. 
#  
#  
#  *1. Take a given list of tasks.
#  
#  *2. Assign priorities to all the data in the data structure based on a universal formula. (We multiply by 10000 to prevent any dependent task having smaller priority than and independent task, when its number of dependencies is multiplied by 10000 and we add its time.
#  
#   $priority = number of dependencies * 10000 + task duration$
#   
#   
#  *3. Take the priorities of the list of tasks given to the algorithm.
#  
#  *4. MinHeap the priorities list.(sort by the smallest number of priority, which is high priority and should be executed first)
#  
#  *5. Output the priorities list.
#  
#  *6. Take the initial task list, and update the tasks in the order of priorities.
#  
#  *7. Produce an ordered list of tasks.
#  
#  *8. Sum all of their task duration.
#  
#  *9. Output the time taken in total for all task execution.
# 

# *#composition*: Particular attention has been paid to interpret information in the style of a coder while commenting and answering the question, so that it is more easily understandable by the intended audience. I used specific language and format to explain the execution of the algorithm, by using numbers and words commonly used in programming.

# 
# ○ Produce a critical analysis of your scheduler, highlighting all the benefits in following the
# algorithmic directives and any failure modes it runs into.

# 
# ### Answer: ###
# 
# The Scheduler uses 6 functions to be fully executed (excluding the HeapSort algorithm). Each of these functions uses one for-loop maximum, which makes its complexity O(6n) in the worst-case scenario and average-case scenario, and the HeapSort Algorithm itself has a worst-case and average-case running time of O(nlogn). 
# 
# Having these two pieces of information, we can conclude that the  worst-case and average-case running time of the Scheduler will be $O(nlogn)$. 
# 
# As per space, the algorithm uses various storages instead of in-place sorting. However, HeapSort uses auxiliary space O(1), just like insertion sort, which makes it very space-efficient. This is why we can neglect the time complexity of the list storages created for other purposes than sorting. 
# 
# This algorithm would work well as a To-Do list, however, it does not show how one task is depended on another and which one should be conducted first. This means, the user has to find out themselves if there are pre-requirement for one task to be accomplished. This is why, for prioritizing tasks I have used a formula where the activities with least dependencies come up first. After counting for dependencies, I choose the quickest least dependent task to be executed first, so that the productivity is maximized before coming to dependent tasks.
# 
# The Scheduler is also limited in prioritizing based on the time of the day (for example: eating in a KBBQ is not something the user would do as the first thing in the morning) but for the sake of simplicity we do not consider the time of the day, only the duration of the task. 
# 
# Ways to improve:
# 
# The algorithm could account for more variables to increase its functionality. For example, the prioritizing function could account not only for dependencies and time, but also for multitasking, so that it creates the most optimal schedule for the user(in the formula, multitasking could be added). 
# 
# Extra care should be paid to the tradeoff between functionality and complexity, because if the complexity is increased hugely by adding more features, and the accuracy is increasing slowly, we should make an educated decision of choosing the right amount of added features. 
# 
# 
