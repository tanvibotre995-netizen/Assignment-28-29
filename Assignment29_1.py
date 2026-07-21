import os

def file(filename):
    if os.path.isfile(filename):
        print("file exists")
    else:
        print("file is not exists")

def main():
    filename=input("enter file name :")
    file(filename)

if __name__ == "__main__":
    main()
