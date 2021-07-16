def teste(num: list):
    v1 = num[1]
    v2 = num[1]
    n = None
    for i in range(len(num)):
        num[i] = num[i]+2
        if num[i] < v1:
            v1 = v1 + num[i]
        elif num[i] > v2:
            v2 = v2 + num[i]
    print(v1, v2)

num = [1,2,3,4,5,6,7,8,9,10]
teste(num)