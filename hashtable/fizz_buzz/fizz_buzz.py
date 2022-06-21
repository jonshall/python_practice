"""fizz_buzz.py

Find fizzbuzz in string array from given number
"""
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # answer list
        answer = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        
        # List of divisors which we will iterate over.
        divisors = [3, 5]

        for num in range(1, n + 1):

            num_answer_str = []

            for key in divisors:
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_answer_str
                if num % key == 0:
                    num_answer_str.append(fizz_buzz_dict[key])

            if not num_answer_str:
                num_answer_str.append(str(num))

            # Append the current answer str to the answer list
            answer.append(''.join(num_answer_str))

        return answer
