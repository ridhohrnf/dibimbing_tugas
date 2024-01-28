class Car:
    def __init__(self,make,model,year,color,speed):
        # attriibutes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, speed_increase):
        # increase the speed of the car by the given amount
        self.speed += speed_increase

    def brake(self, speed_decrease):
        # mengurangi kecepatan mobil dengan jumlah yang diberikan
        self.speed -= speed_decrease
        self.speed = max(self.speed,0)

    def honk(self):
        # print honking message
        print("honk! honk!")

    def display_info(self):
        # print the information about the car
        print(f"{self.year} {self.make} {self.model} {self.color}")
        print(f"Current Speed: {self.speed} mph")

def main():
    # call class
    my_car = Car(make="Toyota",model="Camry",year=2023,color="black",speed = 0)

    # accelerate the car
    my_car.accelerate(100)
    my_car.brake(150)

    my_car.display_info()
    my_car.honk()

if __name__ == "__main__":
    main()