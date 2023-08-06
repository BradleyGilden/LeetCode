"""                           Solution                                """

def isPalindrome(x: int) -> bool:
    xstr = str(x)
    if (xstr == xstr[::-1]):
        return True
    else:
        return False

"""                          Test Solution                            """

if __name__ == "__main__":
	print(isPalindrome(101))
	print(isPalindrome(-101))
	print(isPalindrome(10))
	print(isPalindrome(123))
	print(isPalindrome(0))
