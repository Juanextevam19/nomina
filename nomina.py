


#US1/create_ register

users = []
def createUser():
    user = []
    id = int(input("Ingrese su Documento de identidad"))
    user.append(id)
    user_name= input("Ingrese su nombre")
    user.append(user_name)
    last_name=input("Ingrese su apellido")
    user.append(last_name)  
    phone = input("Ingrese su telefono")
    user.append(phone)
    email= input("Ingrese su correo electronico")
    user.append(email)
    password=input("Ingrese su contraseña")
    user.append(password)
    users.append(user)

createUser()
createUser()
createUser()

print(users)