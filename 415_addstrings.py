import unittest



class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.addAmount(num1) + self.addAmount(num2))

    def addAmount(self, numbers):
        total = 0
        digital = 0
        for number in reversed(numbers):
            amount = int(number) * (10**digital)
            total += amount
            digital += 1
        return total




class QueueTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_size(self):
        s = Solution()

        self.assertEquals(s.addStrings('792', '689'), str(1481))
        self.assertEquals(s.addStrings('1321', '76'), str(1397))



if __name__ == '__main__':
    unittest.main()