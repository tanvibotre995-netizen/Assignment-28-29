def Frequency(FileName):
    fobj = open(FileName, "r")

    Data = fobj.read()

    Frequency = {}

    for ch in Data:
        if ch in Frequency:
            Frequency[ch] = Frequency[ch] + 1
        else:
            Frequency[ch] = 1

    print(Frequency)

    fobj.close()


def main():
    Frequency("demo.txt")


if __name__ == "__main__":
    main()
