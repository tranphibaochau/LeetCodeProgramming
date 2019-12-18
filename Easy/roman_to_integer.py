"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999."""

def romanToInt(self, s: str) -> int:
	rti_dict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #create a dictionary to look up the value of each roman symbol
	total = 0 #final value
	#for each symbol in the string, if the value it stands for is less than the value of the next symbol, subtract it from the sum instead of adding it
	for i in range (0, len(s)):
		if i+1 < len(s) and rti_dict[s[i]] < rti_dict[s[i+1]]:
			total -=rti_dict[s[i]]
		else:
			total+= rti_dict[s[i]]
	return total
