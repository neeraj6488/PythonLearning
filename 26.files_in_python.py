file = open("D:\\data.txt", 'w')
file.write("My Name is Neeraj")
file.close

file = open("D:\\data.txt")
content = file.read()
print(content)

binary_file = open("D:\\data.bin", 'wb')
binary_data = b'\x00'
binary_file.write(binary_data)
binary_file.close

binary_file = open("D:\\data.bin", 'rb')
binary_content = binary_file.read()
print(binary_content)

unicode_file = open("D:\\unicode.txt", 'w', encoding='utf-8')
unicode_file.write('Hello, 世界\n')
unicode_file.close

unicode_file = open("D:\\unicode.txt", 'r', encoding='utf-8')
unicode_content = unicode_file.read()
print(unicode_content)