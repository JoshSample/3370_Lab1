"""
Josh Sample
CSCI3370
Lab 1
"""
from xml.etree.ElementTree import Element, SubElement, ElementTree

SYMBOLS = ['(', ')', '[', ']', '{', '}', ',', ';', '=', '.', '+', '-', '*', '/', '&', '|', '~', '<', '>']
KEYWORDS = ['class', 'constructor', 'method', 'function', 'int', 'boolean', 'char', 'void', 'var',
            'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true', 'false', 'null', 'this']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    symbol = "symbol"
    reserved_word = "keyword"
    identifier = "identifier"
    root = Element("tokens")

    # This is the file reading process
    with open('Square.jack', 'r') as f:
        for line in f:
            # Removes single line comments
            line = line.partition('//')[0]
            # Removes multi line comments
            if line.__contains__('/**'):
                while not line.__contains__('*/'):
                    line = f.__next__()
                line = f.__next__()
            # Tokenize keywords
            count = 0
            for word in line:
                if any(word in KEYWORDS for word in line.split()):
                    keyw = SubElement(root, reserved_word)
                    keyw.text = line.split()[count]
                    line = line.replace(line.split()[count], '')
                    count += count
                for character in line:
                    if any(x in SYMBOLS for x in character):
                        char = SubElement(root, symbol)
                        char.text = character
                        line = line.replace(character, '')
                    if any(x in DIGITS for x in character):
                        line = line.replace(character, '')
            for word in line.split():
                if not word:
                    continue
                else:
                    iden = SubElement(root, identifier)
                    iden.text = word
                    line = line.replace(line, '')
            print(line.split())
    # Close file
    f.close()
    # Write xml file
    tree = ElementTree(root)
    tree.write("filename.xml")


if __name__ == "__main__":
    main()
