def build_xml_element(tag, content, key_value):
    string = ""
    string += "<"
    string += tag
    for element in key_value.keys():
        string += " "
        string += element.__str__()
        string += "="
        string += "\""
        string += key_value[element].__str__()
        string += "\""
    string += ">"
    string += content
    string += "</"
    string += tag
    string += ">"
    return string



x = dict()
x["href"] = "http://python.org"
x["_class"] = " my link "
x["id"] = "some id"
print(build_xml_element("a", "Hello there", x))
