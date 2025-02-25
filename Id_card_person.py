from string import ascii_letters

class Person:
    S_UKR = "абвгдежзійиклмнопрстуфхцчшщьєюя"
    S_UKR_UPPER = S_UKR.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
      
        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight
    
    @classmethod
    def verify_fio(cls,fio):
        if type(fio) != str:
            raise TypeError ("ПІБ повинно бути строкою")
        
        f = fio.split()
        if len(f) !=3:
            raise TypeError("Невірний формат")

        letters = ascii_letters + cls.S_UKR + cls.S_UKR_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("ПІБ Повинен містити хочаб один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("ПІБ повинен містити лише буквенні символи")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Вік у межах 14 -120 років, ціле число")
    
    @classmethod
    def verify_weight(cls, w):
        if type(w) !=int or w < 20:
            raise TypeError ("Вага не менше 20 кг")
    
    @classmethod
    def verify_ps (cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт повинен бути строкою у форматі Серія Номер")
        
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 6:
            raise TypeError("Невірний формат паспортних даних")
        
        for p in s[1]:
            if not p.isdigit():
                raise TypeError("")
        for p in s[0]:
            if p.isdigit():
                raise TypeError("")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self,x):
        self.verify_old(x)
        self.__old = x

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, wg):
        self.verify_weight(wg)
        self.__weight = wg

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

if __name__ == "__main__":
    p = Person ("Нестеренко Дмитро Валерійович", 120,"СМ 607853", 102)
    p.old = 100
    p.passport = "FR 098686"
    p.weight = 90
    print (p.__dict__)