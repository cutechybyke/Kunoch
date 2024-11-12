#This is for sorting a list of numbers in descending order.

def sorting_descending(X):
    # Where X represents numbers.
    return sorted(X, reverse=True)
# Now, we take inputs to be sorted
input = input("Please, enter only numbers and separate them with spaces:")

# This is to convert the inputs into list of integers.
X = list(map(int, input.split()))

sorted_X = sorting_descending(X)

print("Here are the numbers sorted in descending order:", sorted_X)
