class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for b in s:
            if b == "(" or b == "{" or b == "[":
                st.append(b)
            else:
                if len(st) == 0:
                    return False
                ch = st.pop()
                if (
                    (b == ")" and ch == "(")
                    or (b == "}" and ch == "{")
                    or (b == "]" and ch == "[")):
                    continue
                else:
                    return False
        return len(st) == 0
