## Graphs for survey data collected on North Stradbroke Island 7 September 2019
import matplotlib.pyplot as plot

## Input elevation and distance values as y, x respectively
## Input all survey data values as y, x as point number
x_1 = [0,70,155,230,420,440,480,480,500,540,600,640,720,740,900,1040,1060,1110,1220,1260,1300,1390,1500,1670,1830,1870,1970,2090,2140]
y_1 =[-29.4,-26.9,-21.9,-23.3,-17.35,-5.25,-5.75,0,8.7,9,16.8,16.8,15.7,16.3,14.5,16.2,16.98,10.58,15.35,4.75,11.15,22.55,26.25,9.55,9.55,34.65,47.65,8.65,22.15]

plot.title("Elevation on A3/B3 Transect")
plot.scatter(x_1, y_1, color = 'blue', marker = 'o', label = "Ocean to Crest")

plot.xlabel("Distance(m)")
plot.ylabel("Elevation(m)")

plot.plot(x_1, y_1, color = 'blue') ## connect the dots
## Finalize things
plot.grid(True)
plot.legend()
plot.show()
