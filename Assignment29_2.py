def main():
    file=open("demo.txt", "r")

    Data=file.read()
    print(Data)

    file.close()
    
if __name__ == "__main__":
    main()
