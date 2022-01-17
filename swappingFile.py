def swapFileData():
    file1Name=input("enter file1 name:")
    file2Name=input("enter file2 name:")
    dataA=sample1.txt
    dataB=sample2.txt

    file=open(file1Name,'r'):
        file1Name.input=dataA

    file=open(file2Name,'r'):
        file2Name.input=dataB

    print("file1 name:")
    print(file1Name.input)

    print("file2 name:")
    print(file2Name.input)

swapFileData()