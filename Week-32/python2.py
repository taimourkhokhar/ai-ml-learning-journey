s ="aacc"

t ="ccac"

def checker(s,t):
    if len(s)!=len(t):
        return False
    s_list=list(s)
    for i in t:
        if i in s_list:
            s_list.remove(i)
            return True
        else:
            return False

print(checker(s,t))