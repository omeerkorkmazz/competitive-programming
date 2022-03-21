Given a large list of positive integers, count the number of k-subsequences.
A k-subarray of an array is defined as follows:
It is a subarray, i.e. made of contiguous elements in the array
The sum of the subarray elements, s, is evenly divisible by _k, _i.e.: sum mod k = 0.
Given an array of integers, determine the number of k-subarrays it contains.  For example, k = 5 and the array nums = [5, 10, 11, 9, 5].  The  10 k-subarrays are: {5}, {5, 10}, {5, 10, 11, 9}, {5, 10, 11, 9, 5}, {10}, {10, 11, 9}, {10, 11, 9, 5}, {11, 9}, {11, 9, 5}, {5}.

**Function Description **
Complete the function kSub in the editor below. The function must return a long integer that represents the number of k-subarrays in the array.
kSub has the following parameter(s):
    k:  the integer divisor of a k-subarray
    nums[nums[0],...nums[n-1]]:  an array of integers

Constraints
1 ≤ n ≤ 3 × 105
1 ≤ k ≤ 100
1 ≤ nums[i] ≤ 104

Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function.
The first line contains an integer, _k, _the number the sum of the subarray must be divisible by.
The next line contains an integer, n, that denotes the number of elements in nums.

Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer that describes nums[i].

Sample Case 0
Sample Input For Custom Testing

Sample Input 0
3 
5 
1
2
3
4
1

Sample Output 0
4

Explanation 0
The 4 subarrays of nums having sums that are evenly divisible by k = 3 are {3}, {1, 2}, {1, 2, 3}, {2, 3, 4}.