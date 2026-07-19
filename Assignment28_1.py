def main():
    file = open("demo.txt", "r")

    count = 0
    for line in file:
        count = count + 1

    file.close()

    print("Number of lines is:", count)


if __name__ == "__main__":
    main()
