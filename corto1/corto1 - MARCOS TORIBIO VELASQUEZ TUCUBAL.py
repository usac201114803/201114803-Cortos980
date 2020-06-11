callatz = []

def secCallatz(b):
    while b != 1:
        if b % 2 == 0:
            print("%d," % (b), end = "")
            callatz.append(b)
            b = b // 2
        else:
            print("%d," % (b), end = "")
            callatz.append(b)
            b = (b * 3) + 1

        if b == 1:
            callatz.append(b)
            callatz.append(',')
            print("1")
# no se limpia la lista, por lo tanto contiene todas las secuencias acumuladas, en vez de ser una lista por secuencia

digitos = 803

for i in range(2,digitos+1):
    secCallatz(i)

print(callatz)

#Funcionamiento:        20/40 No guarda en un archivo, no genera una secuencia por lista
#Uso de Funciones       20/20
#Manejo de archivos     0/10
#Manejo de Listas       10/10
#Uso de git             0/20 No subio corto a repositorio en github
#*****************************
#Total                  50/100

