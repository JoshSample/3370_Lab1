"""
Josh Sample
CSCI3370
Lab 1
"""
import xml.etree.cElementTree as ET

SYMBOLS = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
KEYWORDS = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var',
            'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']


def main():
    symbol = "symbol"
    reserved_word = "keyword"
    identifier = "identifier"
    int_const = "integerConstant"
    str_const = "stringConstant"
    bool_const = "booleanConstant"
    root = ET.Element("tokens")

    # This is the file reading process
    with open('Square.jack', 'r') as f:
        for line in f:
            line = line.partition('//')[0]
            if line.__contains__('/**'):
                while not line.__contains__('*/'):
                    line = f.__next__()
                line = f.__next__()
            print(line)

    # ET.SubElement(root, "field1", name="blah").text = "some value1"
    # ET.SubElement(root, "field2", name="asdfasd").text = "some value2"
    f.close()
    # tree = ET.ElementTree(root)
    # tree.write("filename.xml")


if __name__ == "__main__":
    main()
