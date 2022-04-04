class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for v in zip(*strs):
            if len(set(v)) == 1:
                result += set(v).pop()

            else:
                break
        return result
