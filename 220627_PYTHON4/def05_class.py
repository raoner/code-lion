class Car:
    count = 0 # 
    def __init__( # 생성자 함수
        self,
        name,
        color,
        fuel=100,
        efficiency=13,
        mileage=0
    ):
        self.name = name # 멤버 변수
        self.color = color
        self.fuel = fuel
        self.efficiency = efficiency
        self.mileage = mileage
        Car.count += 1

    def drive(self): # 멤버 메소드
        print(f"Let's drive :{self.name}")
    def __str__(self):
        return f"This is {self.name}"

my_car = Car("911 Turbo S", "Skyblue", "Gasoline")
print(my_car.name, my_car.color, my_car.fuel, my_car.count)

# list(), dict(), tuple() 파이썬 기본 지원 
# .append() list가 가지고 있는 함수 메소드
# .remove() list      "
# keys() 모든 키들을 반환해주는 메소드
# vlues() 모든 값들을 반환해주는 메소드

my_car.drive()
print(my_car)

k5 = Car("K5","silver","Gasoline")
print(Car.count)



