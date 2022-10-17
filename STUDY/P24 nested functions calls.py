# nested functions calls = function calls inside other function calls
#  (вложенная функция)      innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

#num = input("Enter a whole possitive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#less code
print((round(abs(float(input("Enter a whole possitive number: "))))))