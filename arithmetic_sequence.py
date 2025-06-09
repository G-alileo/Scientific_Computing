# This code generates an arithmetic sequence starting from 'start',
# with a common difference of 'difference', and for 'terms' number of terms.
# It prints the sequence in a single line.

start = 5
difference = 3
terms = 8

# Function to generate the next term in the arithmetic sequence
def sequence_gen(prev, diff):
    """Returns the sum of two numbers."""
    return prev + diff

current = start
print("[",current, end=' ')

# This code generates an arithmetic sequence
for i in range(terms - 1):
    current = sequence_gen(current, difference)
    print(current, end=' ')
print("]")  # Print closing bracket for the sequence