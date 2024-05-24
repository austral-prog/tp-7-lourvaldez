def enumerate_list(lista):
    #nueva lista para no modificar la primera
    nueva_lis=[]
    indice = 0
    for elemento in lista:
        if elemento!= "":
            nueva_lis.append(f"{indice}. {elemento}")
            indice = indice + 1
    return nueva_lis

colors = ["Red", "Green", "", "White", "Black"]
enumerate_list(colors)





def enumerate_backwards(list):
    nueva_lis = []
    indice = 0
    for elemento in list:
        elemento= elemento[::-1]
        if elemento != "":
            nueva_lis.append(f"{indice}. {elemento}")
            indice = indice + 1
    return nueva_lis
