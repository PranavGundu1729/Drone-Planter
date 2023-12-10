""" This is the main drone class, which all codes will use to control and operate the drone. """

class Drone:
    def __init__(self):
        # Drone Variables
        self.mass = 0
        self.maxThrust = 0

        # Motors
        self.leftBackMotor =  0
        self.leftFrontMotor = 0
        self.rightBackMotor = 0
        self.rightFrontMotor = 0
        self.motors = [self.leftBackMotor, self.leftFrontMotor, self.rightBackMotor, self.rightFrontMotor]
        self.motorVelocities = []

        self.yaw = 0
        self.pitch = 0
        self.roll = 0
        self.altitude = 0
        self.GPSPosition = 0
        self.cartesianPosition = 0

    def selfCheck(self):
        fail = True

        if fail:
            self.emergencyShutdown()
        return fail
    
    def getMotorVelocities(self):
        currentMotorVelocities = []
        for motor in self.motors:
            motor.getVelocity()
            currentMotorVelocities.append(motor)
        
        currentMotorVelocities = currentMotorVelocities.reverse()
        self.motorVelocities = currentMotorVelocities
        
    
    def emergencyShutdown(self):
        pass

    def getAcceleration(self):
        pass

    def getGPSPosition(self):
        pass

    def getCartesianPosition(self):
        yawAcceleration = 0
        pitchAcceleration = 0
        rollAcceleration = 0


    def getYaw(self):
        pass

    def getPitch(self):
        pass

    def getRoll(self):
        pass

    def getAltitude(self):
        pass

    def moveForward(self, distance):
        pass

    def moveBackward(self, distance):
        pass

    def moveLeft(self, distance):
        pass

    def moveRight(self, distance):
        pass

    def rotate(self, radians):
        pass

    def followPath(self):
        pass

    def land(self):
        pass

    def takeOff(self):
        pass

    def streamVideo(self):
        pass

    def takePicture(self, quantity):
        pass

    def takeVideo(self, time):
        pass

    







    