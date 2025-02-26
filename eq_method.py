class Clock:
    __DAY = 86400 # seconds in one day

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be integer number")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data (cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Operand in right must be integer or Clock")
        
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, value):
        sc = self.__verify_data(value)
        return self.seconds == sc
    
    def __lt__ (self,value):
        sc = self.__verify_data(value)
        return self.seconds < sc
    
    def __le__ (self,value):
        sc = self.__verify_data(value)
        return self.seconds <= sc

c1 = Clock(1000)
c2 = Clock(1900)
print(c2 >= c1)