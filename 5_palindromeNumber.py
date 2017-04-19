import unittest



def check_palindromeV1(text):
	print len(text) / 2
	# get length of string
	# loop backward
	return True


def check_palindrome_recursive(text):
	#base case
	if len(text) == 1:
		return True

	if len(text) == 2 and (text[0] == text[1]):
		return True

	else:
		return text[0] == text[len(text)-1] and check_palindrome_recursive(text[1:len(text) - 1])



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        text = str(x)
        if len(text) == 1:
        	return True
        if len(text) == 2 and (text[0] == text[1]):
        	return True
        else:
        	return (text[0] == text[len(text)-1]) and self.isPalindrome(text[1:len(text) - 1])
			

class TestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test(self):
		self.assertEquals(check_palindrome_recursive('ACAACA'), True)
		self.assertEquals(check_palindrome_recursive('ABCCAA'), False)

	def test2(self):
		s = Solution()
		self.assertEquals(s.isPalindrome('ACAACA'), True)
		self.assertEquals(s.isPalindrome('ABCCAA'), False)


if __name__ == '__main__':
    unittest.main()