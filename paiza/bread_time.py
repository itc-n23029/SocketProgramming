def f(s, dic):
    key = [time for time in dic.keys() if int(s) < int(time)][0]
    return dic.get(key)


if __name__ == '__main__':
    dic = {
    '6': 0,
    '8': 45,
    '24': 60
}

s = input()
print(f(10, dic))
