I decided to use recursion for problem 4 because you can't be sure how many groups deep you will have to search. I used the or operator on the output so it only takes one call to report True for the output to be True.

The time complextity of is_user_in_group() is O(n)
Reason: There are two for loops that are not nested.

The space complexity of is_user_in_group() is O(1)
Reason: Only one variable is allocated