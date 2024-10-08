import xml.dom.minidom

domtree = xml.dom.minidom.parse('people.xml')

group = domtree.documentElement

people = group.getElementsByTagName('person')

for person in people:
    print(f"-- Person {person.getAttribute('id')} --")

    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
    height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")

people[0].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Peter Warm"
people[0].setAttribute("id", "200")
people[0].setAttribute("newAttr", "Hello")

new_person = domtree.createElement("person")
new_person.setAttribute("id", "89")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Florian Dedov"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("22"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("84"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("189"))

new_person.appendChild(name)
new_person.appendChild(age)
new_person.appendChild(weight)
new_person.appendChild(height)

group.appendChild(new_person)

domtree.writexml(open('people.xml', 'w'))