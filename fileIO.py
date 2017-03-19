
fw = open("New File.txt", 'w')
fw.write("This is a new file \n")
fw.write("It's made by python \n")
fw.close()

fr = open("New File.txt", 'r')
text = fr.read()

print(text)
fr.close()

# If you want to open a file that already exists then use 'a' rather than 'w' or 'r'
# 'w' = write
# 'r' = read
# 'a' = append

