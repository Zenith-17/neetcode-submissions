class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        sn=[]

        for token in tokens:
            if token not in ("+","-","*","/"):
                sn.append(token)
            else:
                e1=int(sn.pop())
                e2=int(sn.pop())
                res=0
                if token == "+":
                    res=e1+e2
                elif token == "-":
                    res=e2-e1
                elif token == "*":
                    res=e2*e1
                else:
                    res=int(e2/e1)
                sn.append(res)
        return sn.pop()



        