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

    # This reads the file one character at a time
    with open('Square.jack', 'r') as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of file")
                break
            print("Read a character:", c)
    # ET.SubElement(root, "field1", name="blah").text = "some value1"
    # ET.SubElement(root, "field2", name="asdfasd").text = "some vlaue2"
    f.close()
    # tree = ET.ElementTree(root)
    # tree.write("filename.xml")


if __name__ == "__main__":
    main()
