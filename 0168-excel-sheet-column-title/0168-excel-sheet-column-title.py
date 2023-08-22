class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while columnNumber > 0:
            result.append(mapping[(columnNumber-1)%26])
            columnNumber = (columnNumber -1)//26

        return ''.join(reversed(result))