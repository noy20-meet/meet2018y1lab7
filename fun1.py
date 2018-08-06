
c = 0
for number in range(1, 100 + 1):
    print(number)
    c = c + number
print(c)
'''
this code iis prunting all the numbers from 1-101 and combinnig them togeder
'''
def add_numbers(c):
    for number in range(1, 100+1):
        print(number)
        c=c+number
    return(c)   



answer = add_numbers(0)
print(answer)
'''
function for the code
'''
def add_number2(start, end):
    for number in range(start, end):
        print(number)
        end=start+number
    return(end)

answer2 = add_number2(333, 778)
print(answer2)

def add_number3(start, end):
    c=0
    for number in range(start, end+1):
        c=c+number
    return(c)

answer3 = add_number3(1, 2)
print(answer3)


answer4=add_number3(1, 100)
print(answer4)

answer5= add_number3(1000, 5000)
print(answer5)

