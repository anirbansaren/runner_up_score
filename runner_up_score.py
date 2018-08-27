if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_num=-100
    second_max=-100
    for i in arr:
        if i>max_num:
            second_max=max_num
            max_num=i
        elif i<max_num:
            second_max
        else:
            second_max=i
    print(second_max)