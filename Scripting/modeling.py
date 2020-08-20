"""
so we will have three objects to enter into these models

class SolarIncrement:
    def __init__(self,dhi,dni,temp,windspeed,albedo,relhum,pressure,begin,end):

lass solarPosition:
    def __init__(self,year,day,hour,lat,long):
    also zenith and azimuth of sun

class modelInputs:
    def __init__(self,sysSize,modType,sysLosses,arrayType,tiltAngle,azimuthAngle):

We first will initialize these all for the entire year of 2018, making arrays for all needed values with the data point at increments of 30 minutes, so one year will be 17520 measured instances, using these inputs we will create the requried modeling functions. for testing we will create empty arrays and fill them up eventually. we will use np.save() eventually to remove the calculation requirement every time

AOI (angle of incidence) calculations for fixed, one-axis, or two-axis tracking systems
"""
import math
#defining variables, these are placeholders for now
dhi = [0] * 17519
dni = [0] * 17519
temp = [0] * 17519
windspeed = [0] * 17519
albedo = [0] * 17519
relhum = [0] * 17519
pressure = [0] * 17519
begin = 0
end = 0
year = 0
day = [0] * 17519
hour = [0] * 17519
lat = 0
long = 0
zenith = [0] * 17519
azimuth = [0] * 17519
sysSize = 0
modType = 0
sysLosses = 0
arrayType = 0
tiltAngle = 0
azimuthAngle = 0

def fixedAOI(zenith,azimuth,azimuthAngle,tiltAngle):
    AOI = []
    for index in range(0,17519):
        fixed1 = math.sin(zenith[index])*math.cos(azimuthAngle - azimuth[index])*math.sin(tiltAngle)
        fixed2 = math.cos(zenith[index])*math.cos(tiltAngle)
        aFixed = math.acos(fixed1 + fixed2)
        AOI.append(aFixed)
    return AOI

def horOneAxisTracking(zenith,azimuth,azimuthAngle,tiltAngle):
    AOI = []
    for index in range(0,17519):
        R = math.atan(math.tan(zenith[index])*math.sin(azimuth[index] - azimuthAngle))
        B = abs(R)
        Y = azimuthAngle + math.asin(math.sin(R)/math.sin(B))
        f1 = math.sin(zenith[index])*math.cos(Y - azimuth[index])*math.sin(B)
        f2 = math.cos(zenith[index])*math.cos(B)
        aFixed = math.acos(f1 + f2)
        AOI.append(aFixed)
    return AOI







for index in range(0,17519):
    pass