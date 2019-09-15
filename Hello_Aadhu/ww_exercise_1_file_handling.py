class fileDict:
    def __init__(self):
        pass

    def doesFileExist(self, path_name):
        try:
            rf = open(path_name, 'r')
        except FileNotFoundError:
            print("File does not exist in given path")
        except:
            print("Unexpected Error...!!")
        else:
            print("File exist in given path\n")
            with open(path_name, 'r') as rf:
                for line in rf.readlines():
                    start_pos = rf.seek(0)
                    match = ' '
                    end_index = line.find(match, start_pos)
                    end_pos = rf.seek(end_index)
                    word = line[start_pos:end_pos]
                    print(word)
                    meaning = line[end_pos + 3:]
                    if not meaning:
                        print("No meaning for this word..!!")
                    else:
                        if ',' in meaning:
                            meaning_s = meaning.split(', ')
                            for i in range(len(meaning_s)):
                                print(meaning_s[i])
                        else:
                            meaning1 = meaning
                            print(meaning1)


print("Please enter the valid path to access file \nNote: File format should be in as below -\n\nword1 - meaning1, meaning2\nword2 - meaning1, meaning2\n\n")
path = input("Enter the File path: ")
p1 = fileDict()
p1.doesFileExist(path)
