class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Initialize an empty list to store results
        lst = []

        # Populate the list with numbers from 1 to n (inclusive)
        for i in range(1, n + 1):
            lst.append(i)

        # Iterate over the list and apply FizzBuzz logic
        for y in range(len(lst)):
            # Check if number is divisible by both 3 and 5 first
            # This avoids replacing it early with just "Fizz" or "Buzz"
            if lst[y] % 3 == 0 and lst[y] % 5 == 0:
                lst[y] = "FizzBuzz"
            # If divisible only by 3, replace with "Fizz"
            elif lst[y] % 3 == 0:
                lst[y] = "Fizz"
            # If divisible only by 5, replace with "Buzz"
            elif lst[y] % 5 == 0:
                lst[y] = "Buzz"

        # Convert all items in the list to strings
        lst = list(map(str, lst))

        # Return the final list
        return lst
