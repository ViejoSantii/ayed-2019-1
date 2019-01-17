import json


# TODO Complete!!

def rev(text,c,d):
    if c < 0:
        return d
    else:
        d += text[c]
        return rev(text,c-1,d)
def reverse(text):
    c = len(text)-1
    d = ""
    return rev(text,c,d)

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
    
