name = input("What is Your Name: ")
with open("file.txt","w") as data:
    data.write(f"\n{name}")


