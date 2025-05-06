# class Termajamoa:
#     def __init__(self, name, age, *talant):
#         self.name = name 
#         self.age = age
#         self.talant = talant

#     def get(self):
#         return self.name, self.age, self.talant

#     def __len__(self):
#         return len(self.talant)
    
#     def __str__(self):
#         return self.name, self.age, self.talant
    
#     def __repr__(self):
#         return str(self.age)
    

# obj = Termajamoa('Sardor', 18, 'tez', 'hujimchi')
# obj2 = Termajamoa('Ali', 22, 'himoyachi')

# print(len(obj))

   
# class Time:
    
#     def __init__(self, son):
#         self.son = son 

#     def info(self):
#         return self.son
        
#     def __truediv__(self):
#         return self.son / 60
    
#     def __mul__(self):
#         return self.son * 60
    
# obj = Time(200)

# print(f"{obj.info()} minut, {obj.__truediv__()} soat bo'ladi")
# print(f"{obj.info()} minut, {obj.__mul__()} soniya bo'ladi")


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vectorlar({self.x}, {self.y})"

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)  # Vector uzunligi

    def __abs__(self):
        return int((self.x**2 + self.y**2)**0.5 ) # Mutlaq uzunlik

vector = Vector(3, -5)
print(vector)        # Vector(3, 4)
print(repr(vector))  # Vector(3, 4)
print(len(vector))   # 5 (3-4-5 uchburchagi)
print(abs(vector))   # 5.0





class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1 / 2)



# 
# class Time:
#     def __init__(self,minut):
#         self.minut=minut
# 
# 
#     def __add__(self, other):
#         if not isinstance(other,Time) and not isinstance(other,int):
#             raise TypeError("Siz son yoki time objsini yozishingiz mumkin")
#         son=other
#         if isinstance(other,int):
#             son=other
#         if isinstance(other,Time):
#             son=other.minut
# 
#             return self.minut+son
# 
#         return Time(self.minut+son.minut)
# 
# 
# t=Time(20)
# t2=Time(35)
# c=t+t2
# print(c)



from importlib.metadata import pass_none


class Time:
    DAY=86400

    def __init__(self,second):
        self.second=second


    def get_time(self):
        s=self.second%60
        m=(self.second//60)%60
        h=(self.second//3600)%24
        return f"{self.get_formated(h)}:{self.get_formated(m)}:{self.get_formated(s)}"

    @classmethod
    def get_formated(cls,x):
        return str(x).rjust(2,"0")


time=Time(86399)
print(time.get_time())
