if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=arr
    max_num=-100
    second_max=-100
    for i in arr1:
        if i>max_num:
            max_num=i

    print(max_num)