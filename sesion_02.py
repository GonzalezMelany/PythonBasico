#Tuplas
mi_tupla = (2, 4)
print ("Mi tupla: ", mi_tupla)

#Lista
mi_lista = [1, 3.1416, "Melany", mi_tupla]
print ("El primer elemento de mi lista", mi_lista[0])
print ("El cuartp elemento de mi lista", mi_lista[3])
print ("El tercer elemento de mi lista", mi_lista[2])

#diccionario 
mi_dic = {
    "mi_lista": mi_lista,
    "nombre": "pablo",
    "Pi": 3.1416,
    "tel": "7444701792"
}
print("llave para accesar a mi diccionario mi_lista", mi_dic["mi_lista"])
print("llave para accesar a mi diccionario Pi", mi_dic["Pi"])
print("llave para accesar a mi diccionario tel", mi_dic["tel"])
