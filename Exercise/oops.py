# File: oops.py

class MyError(Exception):
    pass

def oops():
    raise MyError('Spam!')

def doomed():
    try:
        oops()
    except IndexError:
        print('Oops! We got an IndexError!')
    except MyError as data:
        print('Caught Error', MyError, data)
    else:
        print('No error found this time!')


if __name__ == '__main__':
    doomed()
