import sys

if __name__ == "__main__":
    try:
        name=sys,argv[1]
    except:
        name=input("what's your name?\n")
    from getpass import getpass
    pw=("what's your password?\n")
    print(name,pw)
    
