"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Input: 123
Output: "One Hundred Twenty Three"
"""
class Solution:
    def numberToWords(self, num):
    	#corner case
        if num == 0:
            return 'Zero'
        num_str = str(num)
        #helper function to deal with chunk of 3-digit number
        def helper(num, suffix):
            s = ""
            if num == 0:
            	return s
            #common cases
            nums = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5:'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', \
            9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', \
            16: 'Sixteen', 17:'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'One Hundred', 200: 'Two Hundred', \
            300: 'Three Hundred', 400: 'Four Hundred', 500: 'Five Hundred', 600: 'Six Hundred', 700: 'Seven Hundred', \
            800: 'Eight Hundred', 900: 'Nine Hundred'}
            if num in nums:
                return (nums[num] + ' ' + suffix).strip()
            #get the number in the hundreds
            hundreds = (num//100) * 100
            if hundreds != 0: #if it's not zero, record it in the current string
                s+= nums[hundreds]
            remaining = num%100
            #before dealing with the tens, make sure to check if it is less than 21
            if remaining < 21:
                return (s + ' ' + nums[remaining] + ' ' + suffix).strip()
            #do the same thing for the tens
            tens = ((num%100)//10)* 10
            if tens != 0:
                s+= ' ' + nums[tens]
            ones = ((num%100)%10)
            if ones != 0:
                s+= ' ' + nums[ones]
            return (s + ' ' + suffix).strip() #returning with the appropriate suffix
        #calling the helper function after chunking the number into groups
        if len(num_str) > 9:
            return " ".join(x for x in [helper(int(num_str[0]), 'Billion'), helper(int(num_str[1:4]), 'Million'), helper(int(num_str[4:7]), 'Thousand'), helper(int(num_str[7:10]), '')] if x)
        elif len(num_str) > 6:
            remaining = len(num_str) - 6
            return " ".join(x for x in [helper(int(num_str[:remaining]), 'Million'), helper(int(num_str[remaining:remaining+3]), 'Thousand'), helper(int(num_str[remaining+3:]), '')] if x)
        elif len(num_str) > 3:
            remaining = len(num_str) - 3
            return " ".join(x for x in [helper(int(num_str[:remaining]), 'Thousand'), helper(int(num_str[remaining:]), '')] if x)
        else:
            return helper(num, '')
"""
#A good solution I found online:

def numberToWords(self, num):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n/10-2]] + words(n%10)
        if n < 1000:
            return [to19[n/100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n/1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'

"""
