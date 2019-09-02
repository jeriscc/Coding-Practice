from move_zeros import Solution

s = Solution()

def testBasic():
    nums = [1, 2, 0, 3, 0, 0]
    s.moveZeros(nums)
    assert nums == [1, 2, 3, 0, 0, 0]


def testTwo():
    nums = [1, 2, 2, 3, 0, 0]
    s.moveZeros(nums)
    assert nums == [1, 2, 2, 3, 0, 0]


def testThree():
    nums = [0, 0, 0, 1, 2, 3]
    s.moveZeros(nums)
    assert nums == [1, 2, 3, 0, 0, 0]


def main():
    testBasic()
    testTwo()
    testThree()


if __name__ == '__main__':
    main()
