function = (input("enter the funcion that you want  "))
list = {
    "omar" : "01091970044",
    "zaid" : "01124544664",
    "fares" : "01017833613",
    "ahmed" : "01226103349"}
def add():
    name = input("Whats the name of the contact youll add  ")
    number = input("Whats their number  ")
    list[name] = (number)
def remove():
    rContact = input("whats the contact you would like to remove  ")
    del list[rContact]
def search():
    searchContact = str(input("Whats the contact you would like to search for  "))
    return searchContact
def view_all():
    print(list)

def update():
    uupdatedname = input("Whats the contact you would like to edit  ")
    updatednumber = input("Whats the edited numb  ")
    list.update({uupdatedname:updatednumber})
           
if function == "add":
    add()
    print(list)

elif function == "remove" :
    remove()
    print(list)

elif function == "search":
    searchContact=search()      
    print(list[searchContact])
elif function =="update":
    uupdatedname=update()
    print(list)
else:
    view_all()
    print(list)