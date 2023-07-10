# 890. Find and Replace Pattern
# Medium

# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.

# Solution start provided:
# class Solution:
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:


# SOLUTION:

from typing import List
class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def make_map(string):
            counter = 1
            map = []
            seen = []
            for i in range(len(string)):
                char = string[i]
                if char in seen:
                    map.append(seen.index(char))
                map.append(counter)
     
                counter += 1
                seen.append(char)
            return map
            
        pattern_map = make_map(pattern)
        output = []
        for word in words:
            if len(word) != len(pattern):
                continue # skips to next word if the word is not the same length as the pattern
            word_map = make_map(word)
            if word_map == pattern_map:
                output.append(word)
        print(output)
        return output
    
    
# TEST
# make an instance of the Solution class:
solution = Solution()
words = ["abc","cba","xyx","yxx","yyx"]
pattern = "abc"

solution.findAndReplacePattern(words, pattern)
