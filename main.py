from helpers import is_palindrome, find_longest_palindrome

def longest_palindrome(str):
    """
    Efficiently Checks for the longest palindrome substring with the help of our
    utility function findLongestPal()
    Time Complexity: O(N**2)
    Space Complexity: O(1)
    :param str:
    :return: str: the longest palindrome
    """
    result = ""
    for i in range(len(str)):
        for_odd = find_longest_palindrome(str, i, i)  # for a string with an odd number of length
        for_even = find_longest_palindrome(str, i, i+1)  # for a string with an odd number of length

        '''comparison of the temp variables(for_odd and for_even)
         to the current loop result and finally assign to result variable'''
        result = max(for_odd, for_even, result, key=len)

    return result

def minPalindromeCuts(string, i, j):
    """
    :param string:
    :param i:
    :param j:
    :return: int: minimum cuts needed to get palindrome substrings
    """
    if i >= j or is_palindrome(string[i:j+1]):
        return 0
    # todo

if __name__ == '__main__':
    input = input('Enter string: ').lower()
    print("Palindrome?: {}".format(is_palindrome(input)))
    print(""
      "Longest Palindrome: {}".format(longest_palindrome(input))
    )
    print(
        "Minimum Palindrome Cuts: {}".format(minPalindromeCuts(input, 0, len(input)-1))
    )
