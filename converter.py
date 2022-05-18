from os import path
import pathlib
import sys

def checkFile(inpFile):
    if str(path.exists(inpFile)) == 'False':
        print(inpFile + " does not exist.")
        exit(0)

inputFile = sys.argv[1]
checkFile(inputFile)

input = open(inputFile, "r")

yamlSuffix1 = ".yaml"
yamlSuffix2 = ".yml"

jsonSuffix1 = ".json"
jsonSuffix2 = ".jsn"

outputFile = sys.argv[2]


if pathlib.Path(inputFile).suffix == yamlSuffix1 or pathlib.Path(inputFile).suffix == yamlSuffix2:
    output = open(outputFile, "w")
    for line in input:
        output.write(line)
    print("File <" + outputFile + "> successfully created.\nHave a nice day!")

elif pathlib.Path(inputFile).suffix == jsonSuffix1 or pathlib.Path(inputFile).suffix == jsonSuffix2:
    output = open(outputFile, "w")
    for line in input:
        output.write(line)
    print("File <" + outputFile + "> successfully created.\nHave a nice day!")
else:
    print("Error. Files are not supporting.")