def main():
    file = open("demo.txt", "r")

    count = 0
    for words in file:
        count = count + len(words)

    file.close()

    print("Number of words is:", count)


if __name__ == "__main__":
    main()
