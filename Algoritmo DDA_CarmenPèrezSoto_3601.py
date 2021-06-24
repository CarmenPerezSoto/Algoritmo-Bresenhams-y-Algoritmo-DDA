#importamos la libreria para poder graficar 
import matplotlib.pyplot as plt

#Declaramos las variables que recibiran los valores
x1 = int( input("Introduce el valor de X1 ") )
y1 = int( input("Introduce el valor de Y1 ") )
x2 = int( input("Introduce el valor de X2 ") )
y2 = int( input("Introduce el valor de Y2 ") )
#calculamos la diferencia de x Y de y
dx = x2-x1
dy = y2-y1
#calculamos la pendiente
m = dy / dx
#calculamos el valor de steps
if(dx > dy):
    steps = dx
else:
    steps = dy
#Calculamos el incremento de X y de Y
xinc = dx / steps
yinc = dy / steps
#Mando a imprimir los valores iniciales 
print(x1,y1)
plt.scatter(x1,y1)
#calculamos los nuevos valores de x y y
i=1
while(i<=steps):
    x1 = x1 + xinc
    y1 = y1 + yinc
    #Redondeamos los valores con el metodo round 
    x=round(x1)
    y=round(y1)
    i+=1
    print(x,y)
    plt.scatter(x,y)
plt.show()