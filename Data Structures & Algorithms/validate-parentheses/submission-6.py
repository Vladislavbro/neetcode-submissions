class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque


        dq = deque()
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        open_brackets = ['(', '[', '{']
        for i in range(len(s)):
            # print(f's[i] = {s[i]}')
            if s[i] in brackets.keys() and len(dq) == 0:
                return False
            if s[i] in open_brackets:
                dq.append(s[i])
                # print(dq)
            elif brackets[s[i]] == dq[-1]:
                # print(2)
                dq.pop()
                # print(dq)
            else:
                # print(5)
                return False

        # print(len(dq))
        if len(dq) > 0:
            return False
        return True