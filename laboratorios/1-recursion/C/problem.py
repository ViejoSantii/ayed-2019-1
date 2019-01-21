import json


# TODO Complete!
def cont(s,V,C):
    if len(s)==0:
        return result(V,C)
    else:
        if s[0]==("A"or"a"):
            V=V+1
            return cont(s[1:],V,C)
        elif s[0]==("E"or"e"):
            V=V+1
            return cont(s[1:],V,C)
        elif s[0]==("I"or"i"):
            V=V+1
            return cont(s[1:],V,C)
        elif s[0]==("O"or"o"):
            V=V+1
            return cont(s[1:],V,C)
        elif s[0]==("U"or"u"):
            V=V+1
            return cont(s[1:],V,C)
        else:
            C=C+1
            return cont(s[1:],V,C)
def result(V,C):
    print(V,C)
    if V>C:
        return True
    elif V<C:
        return False
    
def has_more_vowels(s):
    V=0
    C=0
    print(s)
    return cont(s,V,C)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
