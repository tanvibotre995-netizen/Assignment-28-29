def main():
    file1 = open("ABC.txt", "r")
    file2 = open("demo.txt", "w")

    data = file1.read()
    file2.write(data)

    file1.close()
    file2.close()

    print("File copied successfully")


if __name__ == "__main__":
    main()
