import json


# TODO Complete!
def impar(numbers,c,d):
    print("impar", d, c)
    if c == len(numbers):
        print(d)
        return d
    else:
        if numbers[c]%2 == 1:
            d.append(numbers[c])
        return impar(numbers,c+1,d)
def par(numbers,c,d):
    print("par", d)
    if c == len(numbers)-1:
        c=0
        return impar(numbers,c,d)
    else:
        if numbers[c]%2 == 0:
            d.append(numbers[c])
        return par(numbers,c+1,d)
        
    
def arrange(numbers):
    c = 0
    d = []
    return par(numbers,c,d)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
