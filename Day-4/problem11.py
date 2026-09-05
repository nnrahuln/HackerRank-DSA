n = int(input())

for i in range(n):
    grade = int(input())

    if grade < 38:
        print(grade)
    else:
        next_multiple = ((grade // 5) + 1) * 5

        if next_multiple - grade < 3:
            print(next_multiple)
        else:
            print(grade)