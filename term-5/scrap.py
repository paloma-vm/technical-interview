class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def make_map(string):
            counter = 1
            map = []
            for i in range(len(string)):
                map.append(counter)
                if i < len(string) - 1 and string[i] == string[i+1]:
                    map.append(counter)
                else: 
                    counter += 1
            return map
            
        pattern_map = make_map(pattern)
        output = []
        for word in words:
            if len(word) != len(pattern):
                continue # skips to next word if the word is not the same length as the pattern
            word_map = make_map(word)
            if word_map == pattern_map:
                output.append(word)
        return output