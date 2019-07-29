For this Huffman Coding problem I decided to use a min heap to allow for easy merging of the frequency nodes. I used Pythons heapq library to make the addition and removal of nodes easier.

The time complexity of encode() is O(nlogn)
Reason: make_frequency_dict takes O(n) time, min_heapify_dict takes O(n) time, merge_nodes takes O(logn), make_codes takes O(n), get_encoded_text takes O(n). These all result in a complexity of nlogn

The space complexity of encode() is O(n)
Reason: n is the size of the string. There is a linear space complexity.


The time complexity of decode() is O(n)
Reason: There is a for loop going through each character in the encoded_text

The space complexity of decode() is O(1)
Reason: Only one variable is allocated
