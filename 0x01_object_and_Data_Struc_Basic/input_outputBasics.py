with open('myfile.txt', 'w') as file:
    file.write("""
    I am a boy of 20 years old
    I am aslo a programmer
    """)

with open('myfile.txt', 'r') as file:
    content= file.read()
    myCon= file.readlines()
    print(content)
    print(myCon)


with open('myfile12.txt', 'w') as file:
    file.write("""
    I am a boy of 20 years old
    I am asl a webdeveloper
    """)

with open('myfile12.txt', 'r') as file:
    content= file.read()
    print(content)

# Appending to the file
with open('myfile12.txt', 'a') as file:
    file.write("""I am a """)

# Reading the file
with open('myfile12.txt', 'r') as file:
    print(file.read())