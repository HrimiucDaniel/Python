s = "ThisIsUpperCamelCase"
a = ""

for c in s:
    if c.isupper():
        a = a + "_" + c.lower()
    else:
        a = a + c


a = a.replace("_", "", 1)

print(a)
