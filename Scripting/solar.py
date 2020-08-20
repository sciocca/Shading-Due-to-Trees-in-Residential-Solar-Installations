import pandas as pd

df_2018 = pd.read_csv('C:/Users/samci/Desktop/WORK/Research/NREL_SOLAR_RAD/1276284_41.57_-73.02_2018.csv')
df_dhi,df_dni,df_temp,df_windspeed,df_albedo,df_relhum,df_pressure = df_2018['DHI'],df_2018['DNI'],df_2018['Temperature'],df_2018['Wind Speed'],df_2018['Surface Albedo'],df_2018['Relative Humidity'],df_2018['Pressure']
#df_dhi.array
#day is 47 indexes, our test will be for day 1
class SolarIncrement:
    def __init__(self,dhi,dni,temp,windspeed,albedo,relhum,pressure,begin,end):
        self.dhi = dhi
        self.dni = dni
        self.temp = temp
        self.windspeed = windspeed
        self.albedo = albedo
        self.relhum = relhum
        self.pressure = pressure
        self.begin = begin - 1
        self.end = end - 1

    def increments(self):
        return (self.end - self.begin) * 47




#init object
solarObject = SolarIncrement(0,0,0,0,0,0,0,1,31)
solarNum = solarObject.increments()
for index in range(solarNum):
    dhiTemp,dniTemp,tempTemp,windspeedTemp,albedoTemp,relhumTemp,pressureTemp = df_dhi[index],df_dni[index],df_temp[index],df_windspeed[index],df_albedo[index],df_relhum[index],df_pressure[index]
    solarObject = SolarIncrement(dhiTemp,dniTemp,tempTemp,windspeedTemp,albedoTemp,relhumTemp,pressureTemp,0,30)
