# GitHub username: lopezram503
# Date: 7/29/26
# Description: This code finds all prime numbers up to and including the given limit.


def list_of_primes_up_to(limit=100):

    """ Returns a list of all prime numbers up to and including the limit."""

    # This line creates a list where every number starts as prime
    prime_list = [True] * (limit + 1)

    prime_list[0] = False

    prime_list[1] = False

    # This line starts checking numbers beginning with 2
    divisor = 2

    # This line continues until the divisor is greater than the square root of the limit
    while divisor <= limit ** 0.5:

        # This line checks if the current number is still marked as prime
        if prime_list[divisor]:

          # These steps marks all multiples of the current divisor as not prime
           multiple = divisor * 2

           while multiple <= limit:

                prime_list[multiple] = False

                multiple = multiple + divisor

        divisor = divisor + 1

    # This line creates a list of all numbers still marked as prime
    primes = [number for number in range(2, limit + 1) if prime_list[number]]

    # This line returns the completed list of prime numbers
    return primes

# print(list_of_primes_up_to(20))


