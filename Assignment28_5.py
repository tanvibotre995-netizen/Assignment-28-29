def main():
    file = open("XYZ.txt", "r")

    word = input("Enter word to search: ")

    data = file.read()

    if word in data:
        print("Word found")
    else:
        print("Word not found")

    file.close()


if __name__ == "__main__":
    main()
