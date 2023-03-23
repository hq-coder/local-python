def max_num(num1, num2, num3):
    return max(num1, num2, num3)



def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


def rev_string(s):
    return s[::-1]



def num_within(num, start, end):
    return start <= num <= end


def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    for row in triangle:
        print(row)


# Testing max_num()
print(max_num(5, 9, 3))  # prints 9

# Testing mult_list()
print(mult_list([2, 4, 6]))  # prints 48

# Testing rev_string()
print(rev_string("hello"))  # prints "olleh"

# Testing num_within()
print(num_within(3, 2, 4))  # prints True
print(num_within(3, 1, 3))  # prints True
print(num_within(10, 2, 5))  # prints False

# Testing pascal()
pascal(5)  # prints first 5 rows of Pascal's triangle
