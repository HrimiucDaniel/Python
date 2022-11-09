def build_xml_element(tag, content, **kwargs):
    string = ""
    string += "<"
    string += tag
    key_value = dict()
    for key in kwargs.keys():
        key_value[key] = kwargs[key]

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


print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
