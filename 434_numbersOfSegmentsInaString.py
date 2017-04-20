import unittest



class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())




class QueueTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        s = Solution()

        self.assertEquals(s.countSegments("Hello, my name is John"), 5)
        self.assertEquals(s.countSegments("What the fuck"), 2)



if __name__ == '__main__':
    unittest.main()