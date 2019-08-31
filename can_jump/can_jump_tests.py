from can_jump import Solution

def testOne():
    s = Solution()
    assert s.canJump([1,2,3])

def testTwo():
    s = Solution()
    assert s.canJump([1,0,1]) == False

def main():
    testOne()
    testTwo()

if __name__ == '__main__':
    main()