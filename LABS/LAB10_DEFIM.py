from time import sleep
import ast
import json


def readfile():
    path = "C:/Users/Benco/Documents/Hello.txt"
    file = open(path, "r+")
    mist = list(file.read().splitlines())
    file.close()
    return mist


def DNStoFile(UrlDict):
    path = "C:/Users/Benco/Documents/Hello2.txt"
    file = open(path, "r")
    line_count = 1
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    file = open(path, "a+")
    file.writelines("\n")
    file.write(str(line_count) + ":-----> " + str(UrlDict))
    file.close()


def readfile2():
    path = "C:/Users/Benco/Documents/Hello.txt"
    file = open(path, "r+")
    mist = list(file.read().splitlines())
    file.close()
    return print(mist)


def writetofile(x):
    path = "C:/Users/Benco/Documents/Hello.txt"
    file = open(path, "a")
    file.writelines("\n")
    file.write(x)
    file.close()
    return print("IP added ! ")


def CleanLines(path):
    fh = open(path, "r")
    lines = fh.readlines()
    fh.close()

    keep = []
    for line in lines:
        if not line.isspace():
            keep.append(line)

    fh = open(path, "w")
    fh.write("".join(keep))
    # should also work instead of joining the list:
    # fh.writelines(keep)
    fh.close()


def Deletetofile(x):
    path = "C:/Users/Benco/Documents/Hello.txt"
    with open(path, "r") as f:
        lines = f.read().splitlines()
    with open(path, "w") as f:
        for line in lines:
            if x != line.rstrip("\n"):
                f.write(line)
                f.writelines("\n")
    return print("IP deleted ! ")


def searchIp():
    var = readfile()
    x = bool(False)
    ko = 0
    ipchoose = input("-----------------------------------------\n\nEnter the ip you are searching : ")
    for i in range(len(var)):
        if ipchoose == var[i]:
            ko = i
            x = True
    if x:
        return print("-----------------------------------------\n\nIP FOUND ON THE LIST IN LINE - " + str(ko))
    else:
        return print("-----------------------------------------\n\nIP NOT FOUND")


def AddIP():
    path = "C:/Users/Benco/Documents/Hello.txt"
    counter = 0
    list122 = readfile()
    while True:
        sleep(1)
        count = 0
        ipnum = input("-------------------------------\nEnter the ip you want to enter : ")
        for i in range(len(ipnum)):
            if ipnum[i] == ".":
                count = count + 1
        if count == 3:
            writetofile(ipnum)
            CleanLines(path)
            list122 = readfile()
            print(list122)
            counter = counter + 1
            ans = input("you want to contintue ? yes/no :  ")
            if ans == "yes" or ans == "y":
                continue
            else:
                counter = 5
        else:
            print("Incorrect IP address Don't forger DOTS")
            counter = counter + 1
            ans = input("you want to contintue ? yes/no :  ")
            if ans == "yes" or ans == "y":
                continue
            else:
                counter = 5
        if counter > 4:
            print("End of Attempts")
            break
    return print(list122)


def DeleteIp():
    path = "C:/Users/Benco/Documents/Hello.txt"
    counter = 0
    var = readfile()
    while True:
        sleep(1)
        print(var)
        delip: str = input("--------------------------\nEnter IP address from the above TO DELETE : ")
        for i in range(len(var)):
            if i == len(var) - 1 and i > 1:
                print('Not an Exist IP address ! \n')
            if var[i] == delip:
                Deletetofile(delip)
                CleanLines(path)
                print("IP number: " + str(var[i]) + " DELETED from the list...\n")
                var = readfile()
                print(var)
                break
        counter = counter + 1
        ans = input("you want to contintue ? yes/no :  ")
        if ans == "yes" or ans == "y":
            continue
        else:
            counter = 5
        if counter > 4:
            print("End of the Attempts")
            break
    var = readfile()
    return print(var)


def createADict(count):
    URL_Dictionary = {}
    IPs = readfile()
    co = 0
    i = 0
    while i != count:
        for i in range(count):
            print(IPs)
            IP = input("Enter IP from the above to Enter the DICT: ")
            num = len(IPs)
            for x in range(num):
                if IPs[x] == IP:
                    URL_Dictionary.update({input("enter name of URL :"): IP})
                    IPs.remove(IPs[x])
                    co = co + 1
                    break
            if co < 1:
                print("\nIncorrect IP Write from the ABOVE ! ")
                i = 0
                continue
            else:
                co = 0
                i += 1
    print("You created New Dict  ")
    return URL_Dictionary


def SearchUrl(UrlDict):
    url = input("Enter URL to search ...")
    sleep(2)
    Temp = 0
    x = bool(False)
    for i in UrlDict:
        if url == i:
            x = True
            Temp = i
            break
    if not x:
        return print("The URL: " + url + " CAN NOT BE FOUND IN THE DICTIONARY..")
    else:
        return print("The URL:  " + str(Temp) + " you search FOUND in the Dict ")


def addUrlNIP(UrlDict):
    path = "C:/Users/Benco/Documents/Hello2.txt"
    print(UrlDict)
    countURL = int(input("how much URL:IPs you want to add ? "))
    IPs = readfile()
    for y in dict(UrlDict).values():
        for i in IPs:
            if i == y:
                IPs.remove(i)
    co = 0
    i = 0
    while i != countURL:
        for i in range(countURL):
            print(IPs)
            IP = input("Enter IP from the above to Enter the DICT: ")
            num = len(IPs)
            for x in range(num):
                if IPs[x] == IP:
                    UrlDict.update({input("enter name of URL :"): IP})
                    IPs.remove(IPs[x])
                    co = co + 1
                    break
            if co < 1:
                print("\nIncorrect IP Write from the ABOVE ! ")
                i = 0
                continue
            else:
                co = 0
                i += 1
    print("Your DICTIONARY updated !! ")
    CleanLines(path)
    return UrlDict


def DeleteUrl(UrlDict):
    path = "C:/Users/Benco/Documents/Hello2.txt"
    print(UrlDict)
    print("put (below or equal) --> " + str(len(UrlDict)) + " To Delete .")
    countURL = int(input("Enter How much to delete : "))
    i = 0
    Check = bool(False)
    Check2 = bool(False)
    while i != countURL and countURL <= len(UrlDict):
        Check2 = True
        print(dict(UrlDict).keys())
        ChosetoDel = input("Write a URL from the above to delete : ")
        for x in UrlDict:
            if x == ChosetoDel:
                print("Working...")
                del UrlDict[x]
                Check = True
                break
        sleep(1)
        if not Check:
            print("Incorrect URL Please write from the ABOVE ! ")
            i = 0
            continue
        else:
            print("Url dict Updated " + str(i + 1) + " time")
            i += 1
    if Check2:
        print("YOUR DICT UPDATED FULLY ! ")
    else:
        print("Try again ..")
        DeleteUrl(UrlDict)
    CleanLines(path)
    return UrlDict


def cleandict(line):
    Urldict = eval(line[9:])
    return Urldict


def ChoseAdict():
    UrlDict = {}
    print("Hello this is the menu , please choose a dict to change in -\n")
    path = "C:/Users/Benco/Documents/Hello2.txt"
    file = open(path, "r")
    with open(path, "r") as f:
        line_count = 0
        for _ in f:
            line_count += 1
    f.close()
    print(str(file.read()) + "\nFor new dict enter 'N' ")
    file.close()
    string: str = ("\nEnter between 1-{0}".format(str(line_count)))
    print(string)
    chose = input("Entry : ")
    check = bool(False)

    while chose <= str(line_count) or chose == "N":
        if chose == "N":
            print("\n------------------\nfirst of all create the DICT!\n")
            counter = int(input("How much URLs you want ? "))
            print("Working....")
            sleep(2)
            UrlDict = createADict(counter)
            print("The dic is : " + str(UrlDict))
            DNStoFile(UrlDict)
            print("Your file is Updated continuing to menu ...\n")
            CleanLines(path)
            return UrlDict
        else:

            with open(path, "r") as f:
                line2: str
                for line2 in f:
                    if str(line2[0:1]) == str(chose):
                        UrlDict = cleandict(line2)
                        check = True
                        break
                f.close()
            if not check:
                print("Failed try again..")
                ChoseAdict()
            else:
                CleanLines(path)
                return UrlDict


def Updatefile(stringOriginal, UrlDictCopy):
    sleep(3)
    path = "C:/Users/Benco/Documents/Hello2.txt"
    stringCopy = str(UrlDictCopy)
    with open(path, "r") as reading_file:
        new_file_content = ""
        line2: str
        for line2 in reading_file:
            stripped_line = line2.rstrip()
            if stripped_line[9:] == stringOriginal:
                new_line = stripped_line.replace(stripped_line[9:], stringCopy)
                new_file_content += new_line + "\n"
            else:
                new_file_content += stripped_line + "\n"
        reading_file.close()

    writing_file = open(path, "w")
    writing_file.write(new_file_content)
    writing_file.close()
    return print("Your file updated ")

#    def UpdateIPadd():
#    print(UrlDict)
#    Urlchoose = input("Enter the Url that you want to change the IP TOO")
#    path = "C:/Users/Benco/Documents/Hello2.txt"
#    file = open(path, "r")
#    line_count = 1
#    for line in file:

#        if line != "\n":
#           line_count += 1

#    file.close()
