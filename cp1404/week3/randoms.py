"""
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
# On line 1, random integers between 5 and 20 (including 5 and 20) are printed. The smallest number I see is 5 and the largest number is 20.
#
# On line 2, print out random integers starting at 3 and increasing by 2 each time until 10 (excluding 10). The smallest number I see is 3 and the largest number is 9. Line 2 does not generate 4 because the range starts at 3 and increases in step size 2.
#
# On line 3, print out a random floating point number between 2.5 and 5.5. The minimum number is 2.5 and the maximum number is 5.5.

import random
random_number = random.randint(1, 100)
print(random_number)
