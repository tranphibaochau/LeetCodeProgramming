class Solution:
    def numDecodings(self, s: str) -> int:
        def decode_with_memo(index, s, memo):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s)-1:
                return 1
            elif index in memo:
                return memo[index]
            answer =  decode_with_memo(index+1, s, memo) + (decode_with_memo(index+2, s, memo) if (int(s[index:index+2])< 27) else 0)
            memo[index] = answer
            return answer
        memo = {}
        if not s:
            return 0
        return decode_with_memo(0, s, memo)