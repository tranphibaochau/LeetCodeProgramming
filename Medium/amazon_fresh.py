"""
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana
Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output
Return an integer 1 if the customer is a winner else return 0.

Note"
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

"""

def is_af_winner(codelist, basket):
	if len(codelist) == 0:
		return 1
	if len(basket) == 0:
		return 0
	match = False
	for subgroup in codelist:
		if helper(subgroup, basket) == -1:
			return 0
		else:
			basket = basket[helper(subgroup, basket):]
	return 1

codelist = [['apple', 'apple'], ['apple', 'apple', 'banana']]
shoppingCart = ['apple', 'apple', 'apple', 'banana']
print(is_af_winner(codelist, shoppingCart))

