from course_reqs import Solution


def testBasic():
    s = Solution()
    courses = {
        'CSC400': ['CSC300', 'CSC100'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    assert  s.courses_to_take(courses) == ['CSC100', 'CSC200','CSC300', 'CSC400']


def testUntakeable():
    s = Solution()
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
    }
    assert s.courses_to_take(courses) == None

def testCycle():
    s = Solution()
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': ['CSC300']
    }
    assert s.courses_to_take(courses) == None

def main():
    testBasic()
    testUntakeable()
    testCycle()


if __name__ == '__main__':
    main()
