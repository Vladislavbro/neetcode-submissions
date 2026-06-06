class Solution:
    def calPoints(self, operations: list[str]) -> int:
        from collections import deque

        dq = deque()

        for operation in operations:
            if operation == '+':
                dq.append(dq[-1] + dq[-2])
                print(dq)
            elif operation == 'C':
                dq.pop()
                print(dq)
            elif operation == 'D':
                dq.append(dq[-1] * 2)
                print(dq)
            else:
                dq.append(int(operation))

        return sum(dq)