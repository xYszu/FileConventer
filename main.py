import SaveFile


def main():
    file1 = input("Plik do konwersji: ")
    file2 = input("Plik docelowy: ")
    SaveFile.convert_file(file1, file2)


if __name__ == '__main__':
    main()
