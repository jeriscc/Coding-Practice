
"""
Given a string, find the number of unique palidome substrings
it contains.
"""
def palindromes(s: str) -> int:
    valid = set()
    for i in range(len(s)):
        left = i
        right = i
        while (left >= 0 and right < len(s)):
            if s[left] != s[right]:
                break
            else:
                if s[left: right + 1] not in valid:
                    valid.add(s[left: right + 1])
                left -= 1
                right += 1
        left = i
        right = i+1
        while (left >= 0 and right < len(s)):
            if s[left] != s[right]:
                break
            else:
                if s[left: right + 1] not in valid:
                    valid.add(s[left: right + 1])
                left -= 1
                right += 1
                
    return len(valid)

def tests():
    assert palindromes("aabaa") == 5
    assert palindromes("solution") == 7
    assert palindromes("aabaaxx") == 7

def main():
    tests()

if __name__ == '__main__':
    main()
