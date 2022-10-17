#nested loops = The "Inner loop" will finish all of it's iterations (повторение) before
#               finishing one iteration of the "outer loop"
def bro_code():
    rows = int(input("How many rows?: "))
    columns = int(input("How many columns?: "))
    symbol = input("Enter a symbol to use: ")

    for i in range(rows):
        for j in range(columns):
            print(symbol, end="")
#after we use the print statment we will enter a new line charecter and move down the next line.
#to prevend it put (, end="")
        print()
#bro_code()

def next_one():
    #next_one = input("Are u ready for the next one?: ")
    print("----------From W3------------")
next_one()

# From W3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


