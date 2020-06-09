# get distance between two points on Earth
import math as m
lat1 = float(input('Enter latitude in decimal degrees for first point '))
long1 = float(input('Enter longitude in decimal degrees for first point '))
lat2 = float(input('Enter latitude in decimal degrees for second point '))
long2 = float(input('Enter longitude in decimal degrees for second point '))

# converting lat/ long to spherical coordinates
rho = 6378 # radius of Earth, value in kilometres
phi = (90 - lat1) * (m.pi/ 180)
theta = (360 - long1) * (m.pi/ 180) # conversion to radians

# convert spherical coordinates to rectangular coordinates
x1 = rho * m.sin(phi) * m.cos(theta)
y1 = rho * m.sin(phi) * m.sin(theta)
z1 = rho * m.cos(phi)

# convert 2nd lat/ long value to spherical coordinates, rho won't change
phi = (90 - lat2) * (m.pi/ 180)
theta = (360 - long2) * (m.pi/ 180) # conversion to radians

# convert spherical coordinates to rectangular coordinates, 2nd set
x2 = rho * m.sin(phi) * m.cos(theta)
y2 = rho * m.sin(phi) * m.sin(theta)
z2 = rho * m.cos(phi)

# calculate dot product of rectangular coordinates
dot = ((x1 * x2) + (y1 * y2) + (z1 * z2))

# calculate distance of 2 vectors
dist1 = m.sqrt((x1**2) + (y1**2) + (z1**2)) 
dist2 = m.sqrt((x2**2) + (y2**2) + (z2**2))

# calculate distance along the great circle
# define gamma
gamma = m.acos(dot/ (dist1 * dist2))

# calculate distance
distance = (gamma * rho)

# print final distance to release results, rounded value
print(int(distance), 'km')
