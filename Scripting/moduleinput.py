class modelInputs:
    def __init__(self,sysSize,modType,sysLosses,arrayType,tiltAngle,azimuthAngle):
        self.sysSize = sysSize #kW
        self.modType = modType 
        self.sysLosses = sysLosses #%loss
        self.arrayType = arrayType 
        self.tiltAngle = tiltAngle
        self.azimuthAngle = azimuthAngle #180 northern hem, 0 southern hem

#gonna skip 2-axis
moduleTypes = ['Standard','Premium','Thin film']
arrayType = ['Fixed open rack','Fixed roof mount','1-Axis','Backtracked 1-Axis']
    
modelTest1 = modelInputs(4,moduleTypes[0],10,arrayType[1],25,180)
#A 4kW Standard PV system with 10% system losses. The system is installed on a roof at 25% in the northern hemisphere