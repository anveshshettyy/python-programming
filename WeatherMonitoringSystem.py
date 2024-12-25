from abc import ABC,abstractmethod

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humididty = 0
        self.wind_speed = 0

    def register_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature,self.humididty,self.wind_speed)

    def set_measurement(self,temperature,humidity,wind_speed):
        self.temperature = temperature
        self.humididty = humidity
        self.wind_speed = wind_speed
        self.notify_observer()

class DisplayWeather(ABC):
    def update(self,temperature,humidity,wind_speed):
        pass

class TemperatureDisplay(DisplayWeather):
    def update(self,temperature,humidity,wind_speed):
        print(f"Temperature : {temperature}")

class Humidity(DisplayWeather):
    def update(self,temperature,humidity,wind_speed):
        print(f"Humidity : {humidity}")

class WindSpeed(DisplayWeather):
    def update(self,temperature,humidity,wind_speed):
        print(f"Wind Speed : {wind_speed}")

if __name__ == "__main__":
    weatherStation = WeatherStation()

    temperature_display = TemperatureDisplay()
    humidity_display = Humidity()
    wind_speed = WindSpeed()

    weatherStation.register_observer(temperature_display)
    weatherStation.register_observer(humidity_display)
    weatherStation.register_observer(wind_speed)

    weatherStation.set_measurement(20, 50, 100)
    print()

