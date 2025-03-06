def address_line_split(address_line):
    # Split the address line into words
    words = address_line.split(',')
    return words

if __name__ == '__main__':
    address_line = '123 Main St, Springfield, IL 62701'
    words = address_line_split(address_line)
    print(words)