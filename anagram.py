# %% 
def radix_sort_task2(lst): 
    """
    Performs radix sort on a 2-D list containing item of same length by comparing elements. 
    Counting sort is utilized to compare elements with its respective characters. 

    :param lst: A 2-dimensional list containing elements which are strings of same length 
    :return: A 2-dimensional list with elements sorted based on the first value in each list

    Best/Worst Time Complexity: O(LM) -
    L - Number of elements in the list
    M - Number of characters in the string in the list
    Worst case time complexity is same as best case time complexity. The function will have to check
    each character and sort it using counting sort. 

    Total Space Complexity: O(LM)
    Auxiliary Space: O(L)
    The input list gives a space complexity of O(LM) and each counting sort will need O(N+L) where
    N is the number of unique characters for a string in the list. Since there are only 26 alphabets, N is a constant.
    Therefore, the total space complexity is O(LM). Likewise for auxiliary, since N is constant, 
    the auxiliary space complexity is O(L). 
    """

    length = len(lst[0][0])

    col = 0 
    while col < length:
        # Initialize count array
        count_array = [None]*26
        for i in range(len(count_array)):
            count_array[i] = []
        
        # Update count array to get frequency of each item 
        for item in lst:
            val = ord(item[0][len(item[0])-1-col])-97
            count_array[val].append(item)
        
        # Update input array
        index = 0
        for i in range(len(count_array)):
            item = i 
            frequency = count_array[item]
            for j in range(len(frequency)):
                lst[index] = count_array[item][j]
                index = index+1
        
        col += 1
    
    return lst 

# %%
def optimized_radix_sort_task2(lst):
    """
    Optimized version of radix sort by preprocessing sorting elements based on its length 
    , executing classic radix sort on elements of similar length and combine them together.

    :param lst: A 2-dimensional list containing elements which are strings of same length 
    :return: A 2-dimensional list with elements sorted based on the first value in each list

    Best/Worst Time Complexity: O(LM)
    L - Number of elements in the list
    M - Number of characters in the longest string in the list
    The function will allocate elements in specific index of a new list based on its length, which 
    gives O(M) time complexity. Then, for each non empty bucket, the function will run radix sort which gives
    O(LM) time complexity. Therefore, the best and worst time complexity are O(LM).

    Total Space Complexity: O(LM)
    Auxiliary Space: O(L+M)
    The input list gives a space complexity of O(LM). An additional list is created 
    based on the longest string which gives O(M) additional space. Since the function 
    calls function radix_sort_task2, it would use O(L) additional space as well. Therefore, 
    the final space complexity is O(LM) and auxilairy space is O(L+M).  

    """

    if len(lst) == 0:
        return lst

    # Find element with max length
    max_item = len(lst[0][0])
    for item in lst:
        if len(item[0]) > max_item:
            max_item = len(item[0])
    
    # Initialize count array
    count_array = [None] * (max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []
    
    # Update count array to get the frequency 
    for item in lst:
        count_array[len(item[0])].append(item)

    # Perform radix sort
    i = 0 
    index = 0
    while i < len(count_array):
        if count_array[i] != []:
            count_array[i] = radix_sort_task2(count_array[i])
            for j in range(len(count_array[i])):
                lst[index] = count_array[i][j]
                index = index + 1
        
        i += 1     
    
    return lst

# %%
def anagram_counting_sort(string,islist1): 
    """
    This function sorts a string using counting sort in ascending order based on 
    its ASCII value.

    :param string: A string value
    :param islist1: A boolean value to check if the string belongs to first list
    :return: 
    if islist1 == True: a list containing sorted string and original string
    else: a list containing sorted string

    Best/Worst Time Complexity: O(k) - 
    k - Number of characters in the string
    The function will create a temporary list to store the frequency of each character. Since
    base is a constant, it is a constant operation. The function will iterate over each item in 
    the list and add into the temporary list, which gives O(k) time complexity. Therefore, the 
    final time complexity is O(k).

    Total Space complexity: O(1)
    Auxiliary Space: O(1)
    Since input is a string and the size of temporary list initialized is constant, this
    function does not require any additional memory.

    """
    base = 26

    # Initialize count array 
    count_array = [0] * (base+1)

    # Update count array
    for item in string:
        val = item[0] 
        count_array[ord(val)-97] = count_array[ord(val)-97] + 1
    
    # Update string
    old_str = string
    new_str = ""
    for i in range(len(count_array)): 
        item = i
        frequency = count_array[i]
        for j in range(frequency):
            new_str += chr(item+97)

    if islist1: # Only store list1 original strings
        return [new_str,old_str]
    else:
        return [new_str]

# %%
def remove_duplicates(lst):
    """
    This function removes duplicated values from a 2-d list.

    :param lst: A sorted 2-dimensional list
    :return: A sorted 2-dimensional list with no duplicated inner list value

    Best/Worst Time Complexity: O(n)
    n - The number of elements in the list
    Since the list is sorted, the function is able to utilize pointers to remove the duplicates
    linearly in O(n).

    Total Space Complexity :O(n)
    Auxiliary Space: O(n)
    This function creates an empty list which stores the unique elements. The maximum elements
    that the list can store is n elements. Therefore, the auxiliary space complexity is O(n).
    """
    if len(lst) == 0:
        return lst

    i = 0
    j = 0
    res = []
    while i+1 < len(lst):
        if lst[i+1][0] == lst[j][0]:
            i += 1
        else:
            lst[j+1], lst[i+1] = lst[i+1], lst[j+1]
            i += 1
            j += 1
    
    for i in range(j+1):
        res.append(lst[i])

    return res
# %%
def words_with_anagrams(list1,list2):
    """
    This functions compare two lists of words and find all words in the first list
    which have an anagram in the second list.

    :param list1: List of strings, containing lowercase characters from a-z, no duplicates
    :param list2: List of strings, containing lowercase characters from a-z, no duplicates										
    :return: A list containing words from first list which have an anagram in the second list

    Best/Worst Time Complexity: O(L1M1 + L2M2)
    L1 - Number of elements in list1 
    L2 - Number of elements in list2
    M1 - Number of characters in the longest string in list1
    M2 - Number of characters in the longest string in list2
    The time complexity of this function is mainly contributed by the optimized_radix_sort_task2 function. Since
    we have two input lists which are list1 and list2, the time complexity would give O(L1M1 + L2M2). In
    the searching operation, each element is being checked only once only, which gives a linear time operation. 
    Therefore, the best and worst case complexities are O(L1M1 + L2M2). 

    Total Space Complexity: O(L1M1 + L2M2)
    Auxiliary Space: O(L1+M1+L2+M2)
    The total space complexity of this function is mainly contributed by input lists list1 and list2, which gives
    O(L1M1) and O(L2M2) respectively. For auxiliary space, it is contributed by the optimized_radix_sort_task2 function where
    each function called on each list will give O(L1+M1) and O(L2+M2) additional memory respectively. In this function, 
    a temporary list is used to store the final result, in which its size can only grow up to length of L1. Therefore,
    the total space complexity of this function is O(L1M1+L2M2).  

    """

    # Sort in anagram order
    for i in range(len(list1)):
        list1[i] = anagram_counting_sort(list1[i],True)
    
    for j in range(len(list2)):
        list2[j] = anagram_counting_sort(list2[j],False)

    # Run radix sort
    list1 = optimized_radix_sort_task2(list1)
    list2 = optimized_radix_sort_task2(list2)

    # Remove duplicates in list2
    list2 = remove_duplicates(list2)

    pointer_right = 0
    pointer_left = 0
    res = []

    # Compares elements of list1 with elements of list2
    while pointer_left < len(list1) and pointer_right < len(list2):
        left_item = list1[pointer_left]
        right_item = list2[pointer_right]
        
        # Perform length comparison
        if len(right_item[0]) > len(left_item[0]):
            pointer_left += 1
        elif len(left_item[0]) > len(right_item[0]):
            pointer_right += 1
        else: 
            if left_item[0] == right_item[0]:
                res.append(left_item[1])
                pointer_left += 1
            else: 
                # Perform character comparison
                for i in range(len(left_item[0])): 
                    if left_item[0][i] > right_item[0][i]:
                        pointer_right += 1
                        break
                    elif left_item[0][i] < right_item[0][i]:
                        pointer_left += 1
                        break
        
    return res