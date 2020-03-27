# RestaurantXCenterInMadrid
Calcula la distancia de cada Centro Educativo de la Comunidad de Madrid a un VIPs o un Rodilla

Consta de 2 aplicaciones:
   - **MainRestaurantLocator**: Obtiene la información de los restaurantes de las páginas de Rodilla y VIPs
   - **MainDistanceCalculator**: Calcula la distancia de cada centro al restaurante más cercano (VIPs o Rodilla)

```
El directorio resources\output contiene un CSV con la distancia de cada centro al restaurante más cercano.
```
   
##  MainRestaurantLocator
Obtiene la información de los restaurantes de las páginas de Rodilla y VIPs

Parámetros aceptados:
   - **[-h | --help]** Imprime la ayuda por pantalla     
   - **[-o | --output]** Ruta del directorio en el que generar el fichero de salida 

Ejemplo de invocación:

```
python.exe MainRestaurantLocator.py -o C:\Users\joaquin\PycharmProjects\RestaurantXCenterInMadrid\resources
```

## MainDistanceCalculator
Calcula la distancia de cada centro al restaurante más cercano (VIPs o Rodilla)

Parámetros aceptados:
   - **[-h | --help]** Imprime la ayuda por pantalla     
   - **[-v | --vips]** Fichero CSV con la ubicación de los restaurantes Rodilla     
   - **[-r | --rodilla]** Fichero CSV con la ubicación de los restaurantes VIPS 
   - **[-c | --center]**  Fichero CSV con la ubicación de los centros educativos en la Comunidad de Madrid
   - **[-o | --output]** Fichero en el que se generará la información de salida 
         
Ejemplo de invocación:

```
python.exe MainDistanceCalculator.py -c C:\Users\joaquin\PycharmProjects\RestaurantXCenterInMadrid\resources\19-01-2020-(178)-utf8-extended-gps-owner.csv -v C:\Users\joaquin\PycharmProjects\RestaurantXCenterInMadrid\resources\vips.csv -r C:\Users\joaquin\PycharmProjects\RestaurantXCenterInMadrid\resources\rodilla.csv -o C:\Users\jgarzonpena\PycharmProjects\RestaurantXCenterInMadrid\resources\output\centers2restaurants.csv
```
