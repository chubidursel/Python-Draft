# if __name__ == '__main__':
#
# 1. Module cn be run as a standalone program
# 2. Module can imported and used by other modules
# Python interpreter sets "special variables", one of which __name__
# Python will assign the __name__ variable a value of "__main__" if its the initial modul being run.

if __name__ == '__main__':
    print("Running this module directly")
else:
    print("running other module inderectly")

def hello():
    print("Hello!")