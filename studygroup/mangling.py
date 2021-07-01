class K:
    def __init__(self):
        self.num = 0
        self._num = 1
        self.__num = 2
        self._K__num = 3
    
    def show1(self):
        return self.__num

    def show2(self):
        return self._K__num
    
    def __show(self):
        return "show"
    
    def _K__show(self):
        return "_K__show"


k = K()
print(k.num, k._num)
print(k._K__num)
# print(k.__num)  ## private
print(k.show1())
print(k.show2())
# print(k.__show())  ## private
print(k._K__show())