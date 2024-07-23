class Solution:
    def mergeAlternately(self, word1, word2):
        # Initialize pointers for word1 and word2
        i, j = 0, 0
        result = []

        # Iterate through both strings
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append any remaining characters from word1
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # Append any remaining characters from word2
        while j < len(word2):
            result.append(word2[j])
            j += 1

        # Join the result list into a single string and return
        return ''.join(result)
    
