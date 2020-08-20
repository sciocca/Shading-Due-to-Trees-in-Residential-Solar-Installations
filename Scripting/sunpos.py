import math
import matplotlib.pyplot as plt
#day => Feb1st = 32

class solarPosition:
    def __init__(self,year,day,hour,lat,long):
        self.year = year
        self.day = day
        self.hour = hour
        self.lat = lat
        self.long = long

    def julianDate(self):
        delta = self.year - 1949
        leap = int(delta/4)
        return 32916.5 + delta*365 + leap + self.day + self.hour/24
    
    #Ecliptic Coordinates
    def n(self):
        jd = self.julianDate()
        return jd - 51545.0

    def meanLong(self):
        n = self.n()
        meanlong = 280.46 + (0.9856474*n)
        meanlong = math.fmod(meanlong,360)
        if (meanlong < 0):
            meanlong += 360
        return meanlong

    def meanAnomaly(self):
        n = self.n()
        meananomaly = 357.528 + (0.9856003*n)
        meananomaly = math.fmod(meananomaly,360)
        if (meananomaly < 0):
            meananomaly += 360
        return math.radians(meananomaly)

    def eclipticLong(self):
        L = self.meanLong()
        g = self.meanAnomaly()
        eclipticlong = L + 1.915*math.sin(g) + .02*math.sin(2*g)
        eclipticlong = math.fmod(eclipticlong,360)
        if(eclipticlong < 0):
            eclipticlong += 360
        return math.radians(eclipticlong)

    def obliquityEliptic(self):
        n = self.n()
        obliquityeliptic = 23.439 - .0000004*n
        return math.radians(obliquityeliptic)
    
    #Celestial Coordinates
    def rightAscension(self):
        ep = self.obliquityEliptic()
        l = self.eclipticLong()
        num = math.cos(ep)*math.sin(l)
        den = math.cos(l)
        rightascension = math.atan2(num,den)

        if(den < 0):
            rightascension += math.pi
        elif(num < 0):
            rightascension += 2*math.pi
        return rightascension

    def declination(self):
        ep = self.obliquityEliptic()
        l = self.eclipticLong()
        return math.asin(math.sin(ep)*math.sin(l))

    #Local Coordinates
    def gmst(self):
        n = self.n()
        gmst = 6.697375 + 0.0657098242*n + self.hour
        gmst = math.fmod(gmst,24)
        if(gmst < 0):
            gmst += 24
        return gmst

    def lmst(self):
        gmst = self.gmst()
        eastLong = 360 - self.long
        lmst = gmst + eastLong/15
        lmst = math.fmod(lmst,24)
        if(lmst < 0):
            lmst += 24
        return math.radians(lmst*15)

    def hourAngle(self):
        lmst = self.lmst()
        ra = self.rightAscension()
        hourangle = lmst - ra
        if (hourangle < -math.pi):
            hourangle = hourangle + 2*math.pi
        if (hourangle > math.pi):
            hourangle = hourangle - 2*math.pi
        return hourangle

    def elevation(self):
        dec = self.declination()
        ha = self.hourAngle()
        return math.asin(math.sin(dec)*math.sin(math.radians(self.lat)) + math.cos(dec)*math.cos(math.radians(self.lat))*math.cos(ha))

    def azimuth(self):
        dec = self.declination()
        ha = self.hourAngle()
        el = self.elevation()
        azimuth = math.asin((-math.cos(dec)*math.sin(ha))/math.cos(el))
        if(math.sin(dec) - math.sin(el)*math.sin(math.radians(self.lat)) >= 0):
            if(math.sin(azimuth) < 0):
                azimuth += 2*math.pi
            else:
                azimuth = math.pi - azimuth
        return math.degrees(azimuth)

    def refractionCorrectedAzimuth(self):
        az = self.azimuth()
        l = self.eclipticLong()
        el = math.degrees(self.elevation())
        if(el >= 19.225):
            refraction = 0.00452*3.51823/math.tan(math.radians(el))
        elif(el > -0.766 and el < 19.255):
            refraction = 3.51823*(0.1594 + 0.0196*el + 0.00002*pow(el,2))/(l + 0.505*el + 0.0845*pow(el,2))
        elif(el <= -0.766):
            refraction = 0
        return math.degrees(az + refraction)
    
    def zenithAngle(self):
        el = self.elevation()
        return 90 - el

    #extras
    def soldst(self):
        g = self.meanAnomaly()
        return 1.00014 - 0.01671*math.cos(g) - 0.00014*math.cos(2*g)

    def soldia(self):
        soldst = self.soldst()
        return .5332/soldst

latNorthWaterbury = 41.5582
longWestWaterbury = 73.0515
yearWaterbury = 2018
dayWaterbury = 1
hourWaterbury = 0
hourWaterburyUT = hourWaterbury + 5 - 1

solarObject = solarPosition(yearWaterbury, dayWaterbury, hourWaterburyUT, latNorthWaterbury, longWestWaterbury)

azArray = []
zArray = []

#(We need to figure this out for half hour increments (a day is 47 increments?))
for i in range(90*90*2):
    if (hourWaterbury != 24):
        hourWaterbury += .5
    else:
        dayWaterbury += 1
        hourWaterbury = 0
    solarObject = solarPosition(yearWaterbury, dayWaterbury, hourWaterburyUT, latNorthWaterbury, longWestWaterbury)
    az = solarObject.azimuth()
    z = solarObject.zenithAngle()
    azArray.append(az)
    zArray.append(z)

"""
for i in range(360):
    solarObject = solarPosition(yearWaterbury, dayWaterbury, hourWaterburyUT, latNorthWaterbury, longWestWaterbury)
    dayWaterbury += 1
    az = solarObject.azimuth()
    z = solarObject.zenithAngle()
    azArray.append(az)
    zArray.append(z)
 """

plt.subplot(211)
plt.plot(azArray)
plt.title('Azimuth')
plt.subplot(212)
plt.plot(zArray)
plt.title('Zenith')
plt.show()

"""
show = []
#Visualize a certain val
for i in range(350):
    solarObject = solarPosition(yearWaterbury, dayWaterbury, hourWaterburyUT, latNorthWaterbury, longWestWaterbury)
    dayWaterbury += 1
    temp = solarObject.zenithAngle()
    show.append(temp)

plt.plot(show)
plt.title('zenith')
plt.show()
print(show)
"""