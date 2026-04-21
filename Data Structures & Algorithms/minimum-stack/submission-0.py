from collections import deque

class MinStack:

    def __init__(self):
        self._minstack = deque()
        self._prefixmin = deque()

    def push(self, val: int) -> None:
         self._minstack.append(val)
         # grab previous min for comparision
         if len(self._prefixmin) == 0:
            self._prefixmin.append(val)
         elif val < self._prefixmin[-1]:
            self._prefixmin.append(val)
         else:
            self._prefixmin.append(self._prefixmin[-1])

    def pop(self) -> None:
        self._prefixmin.pop()
        return self._minstack.pop()


    def top(self) -> int:
        return self._minstack[-1]

    def getMin(self) -> int:
        return self._prefixmin[-1]
