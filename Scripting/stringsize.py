import math
#Find min and max string allowed for large PV systems
#Samuel Ciocca 


class StringSizer:
    def __init__(self,panelVoc,panelVmp,inverterMppLow,inverterMppHigh,inverterMaxDCInput,moduleWattage,moduleAmount,inverterWattage,inverterAmount,panelTempVoc,NTOC):
        self.panelVoc = panelVoc
        self.panelVmp = panelVmp
        self.inverterMppLow = inverterMppLow
        self.inverterMppHigh = inverterMppHigh
        self.inverterMaxDCInput = inverterMaxDCInput
        self.moduleWattage = moduleWattage
        self.moduleAmount = moduleAmount
        self.inverterWattage = inverterWattage
        self.inverterAmount = inverterAmount
        self.panelTempVoc = panelTempVoc
        self.NTOC = NTOC

        self.moduleTotal = self.moduleWattage * self.moduleAmount
        self.inverterTotal = self.inverterWattage * self.inverterAmount

        self.minStringSize = math.ceil(self.inverterMppLow / self.panelVmp)
        self.maxStringSize = math.floor(self.inverterMaxDCInput / self.panelVoc)

    def mpp_range_check(self):
        res = self.maxStringSize*self.panelVmp
        if res < self.inverterMppHigh:
            if res > self.inverterMppHigh - 20:
                return True
        else:
            return False
    
    def temp_dependent_max(self,worst_case_day):
        realMaxStringSize = self.maxStringSize
        tempDiff = self.NTOC - worst_case_day
        voltAboveRated = (self.panelVoc * (self.panelTempVoc/100)) * tempDiff
        truePanelVoltage = self.panelVoc + voltAboveRated

        while truePanelVoltage * realMaxStringSize > self.inverterMaxDCInput:
            realMaxStringSize -= 1
        return realMaxStringSize


#LG350N1C-V5
panelVoc = 41.3
panelVmp = 35.3
inverterMppLow = 155
inverterMppHigh = 480
inverterMaxDCInput = 600
moduleWattage = 350
moduleAmount = 12
inverterWattage = 4800
inverterAmount = 1
panelTempVoc = 0.260
NTOC = 45.95

worst_case_day = -30


solarPanelModel = StringSizer(panelVoc,panelVmp,inverterMppLow,inverterMppHigh,inverterMaxDCInput,moduleWattage,moduleAmount,inverterWattage,inverterAmount,panelTempVoc,NTOC)

if solarPanelModel.mpp_range_check() == True:
    print('min string',solarPanelModel.minStringSize,'max string',solarPanelModel.temp_dependent_max(worst_case_day))
else:
    print('failure')
