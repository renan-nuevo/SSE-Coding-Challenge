def is_palindrome(str):
    """Reverse the string and compare original to the
    reversed one to check if string is a Palindrome
    :param str:
    :return: bolean:
    """
    return str[::-1] == str

def find_longest_palindrome(str, l, r):
    """
    this function will check if the left and right portion relative
    to an index(the middle of a possible palindrome substring ) is equal
    to get the start and end index of a palindrome
    :param str:
    :param l:
    :param r:
    :return: str: the longest palindrome relative to an index of the string
    """
    while l >= 0 and r < len(str) and str[l] == str[r]:
        l -= 1
        r += 1

    return str[l+1:r]
