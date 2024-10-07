class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        bs = []
        for c in s:
            try:
                if c in brackets.keys():
                    bs.append(c)
                else:
                    close_br = bs.pop()
                    if c != brackets[close_br]:
                        return False
            except Exception:
                return False
        
        return len(bs) == 0

        