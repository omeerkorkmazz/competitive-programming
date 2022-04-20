Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.

Note: From the dictionary B each word can be taken any number of times and in any order.
Example 1:

Input:
n = 12
B = { "i", "like", "sam","sung", "samsung", "mobile","ice","cream", "icecream","man", "go", "mango" }
A = "ilike"

Output:
1

Explanation:
The string can be segmented as "i like".

Example 2:

Input:
n = 12
B = { "i", "like", "sam","sung", "samsung", "mobile","ice","cream", "icecream", "man", "go", "mango" }

A = "ilikesamsung"

Output:
1

Explanation:
The string can be segmented as 
"i like samsung" or "i like sam sung".
 

Your Task:
Complete function which takes a string and list of strings as a parameter and returns 1 if it is possible to break words, else return 0. You don't need to read any input or print any output, it is done by driver code.


Expected time complexity: O(s^2)

Expected auxiliary space: O(s) , where s = length of string A

 

Constraints:
1 ≤ N ≤ 12
1 ≤ s ≤ 1100 , where s = length of string A
 The length of each word is less than 15.