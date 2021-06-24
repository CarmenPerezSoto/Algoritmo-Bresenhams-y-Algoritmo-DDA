#importamos la libreria para poder graficar
import matplotlib.pyplot as plt
#Declaramos las variables que recibiran los valores
x1 = int( input("Introduce el valor de X1 ") )
y1 = int( input("Introduce el valor de Y1 ") )
x2 = int( input("Introduce el valor de X2 ") )
y2 = int( input("Introduce el valor de Y2 ") )
#calculamos la diferencia
dx = x2-x1
dy = y2-y1
#calculamos a p
p = 2*dy - x1
#Mando a imprimer los valores iniciales
print(x1,y1)
plt.scatter(x1,y1)
#calculamos los nuevos valores de x y y
while(x1<x2):
        plt.scatter(x1,y1)
        x1=x1+1
        if dy<0:
            if p<0:
                p=p+2*dy
                y1=y1-1
            else:
                p=p + (2*dy)-(2*dx)
        else:
            if p<0:
                p=p+2*dy
            else:
                p = p + (2*dy)-(2*dx)
                y1=y1+1
        #Mando a imprimir los puntos
        print(x1,y1)    
plt.show()
