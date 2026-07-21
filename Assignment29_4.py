import os

def CompareFiles(FileName1, FileName2):
    fobj1 = open(FileName1, "r")
    fobj2 = open(FileName2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

    fobj1.close()
    fobj2.close()

def main():
    print(os.getcwd())
    CompareFiles("demo.txt", "hello.txt")

if __name__ == "__main__":
    main()
