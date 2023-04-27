# VMC-CSC Challenge #4

Write a program that takes in a string and returns the longest substring that contains at most k distinct characters. The program should:

* Prompt the user to enter a string.
* Prompt the user to enter a value for k.
* Find the longest substring of the string that contains at most k distinct characters.
* Print out the longest substring.

Here are some additional details:

* The program should assume that the string contains only lowercase English letters.
* The program should handle the case where the longest substring appears more than once in the string.
* If there are multiple substrings with the same length that is the longest in the string, the program should return any one of those substrings.

Here's an example of what your program might look like in action:

```
Enter a string: abcabcbbd
Enter a value for k: 2
The longest substring with at most 2 distinct characters is: bcbb
```

For example, in the string "abcabcbbd", the longest substring with at most 2 distinct characters is "bcbb", which contains only the characters "b" and "c". Here, we have 2 distinct characters.

In the same string "abcabcbbd", the longest substring with at most 3 distinct characters is "abcabcbb", which contains the characters "a", "b", and "c". Here, we have 3 distinct characters.