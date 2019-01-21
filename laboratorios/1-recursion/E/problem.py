import json

def super1(p,s):
    if len(p)== 1:
        s+=int(p[0])
        p=s
        return super2(str(p),s)
    else:
        s+=int(p[0])
        
        return super1(p[1:],s)
def super2(p,s):
    if len(p)==1:
        return int(p[0])
    else:
        s=0
        
        return super1(p,s)
    
# TODO Complete!
def super_digit(n, k):
    p=n*k
    s=0
    return super1(p,s)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')
