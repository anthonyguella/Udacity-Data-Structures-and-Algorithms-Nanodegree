For this problem I chose to use a hash map to store the cached values for instant retrieval of the node and value. I used a doubly linked list to keep track of the most recently used values and size. This allowed me to quickly set the head(most recently used) and pop that back for removal.

The time complexity of get() is O(1)
Reason: No loops, constant time

The space complexity of get() is O(1)
Reason: Only one variable is allocated


The time complexity of set() is O(1)
Reason: No loops, constant time

The space complexity of set() is O(n)
Reason: The dictionary is as large as the amount fo keys
