#range(stop) takes one argument.
#range(start, stop) takes two arguments.
#range(start, stop, step) takes three arguments.


print("----------RUS------------")
#from https://python-scripts.com/range
# цикл for позволяет вам выполнять определенные части кода, столько раз, сколько вам угодно

numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f"{num} делится на 3, результат {int(quotient)}.")

print("----------RANGE() - RUS------------")
# 1 argument
for i in range(3):
    print(i)
# 2 arguments >> range(старт, стоп)
for i in range(1, 8):
    print(i)
# 3 arguments >> range(старт, стоп, шаг) >>шаг = на сколько велика будет разница между одним числом и следующим
for i in range(1, 8, 2):
    print(i)

#----------------CODEWARs-------------

#Build a function that returns an array of integers from n to 1 where n>0
def createList(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return(lst)

print(createList(3))

#better solution
def reverseseq(n):
    return list(range(n, 0, -1))
print(reverseseq(5))
#3rd option
def reverseseq(n):
    return [x for x in range(n,0,-1)]
print(reverseseq(6))