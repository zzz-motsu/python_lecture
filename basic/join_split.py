# join
text = "".join(["Hi", "My", "name", "is", "John"])
print(text)

text = " ".join(["Hi", "My", "name", "is", "John"])
print(text)

text = "**".join(["Hi", "My", "name", "is", "John"])
print(text)

# split
print("Hi My name is John".split())
print("Hi/My/name/is/John".split("/"))

filename= "sample.py"
print(filename.split(".")[0])
print(filename.split(".")[1])
print(filename.split(".")[-1])