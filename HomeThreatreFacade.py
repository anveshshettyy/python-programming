from abc import ABC, abstractmethod

class Amplifier:
    def on(self):
        print("Amplifier On")

    def off(self):
        print("Amplifier Off")

    def set_volume(self,volume):
        print(f"Volume set to {volume}")

class CdPlayer:
    def on(self):
        print("CD Player On")

    def off(self):
        print("CD Player Off")

    def play(self):
        print("CD Player playing...")

class DvdPlayer:
    def on(self):
        print("DVD Player On")

    def off(self):
        print("DVD Player Off")

    def play(self):
        print("DVD Player playing...")

class Projector:
    def on(self):
        print("Projector On")

    def off(self):
        print("Projector Off")

class Screen:
    def down(self):
        print("Screen Rolling Down")

    def up(self):
        print("Screen Rolling Up")


class ThreatreLights:
    def dim(self):
        print("Threatre Lights dimmed ")

    def bright(self):
        print("Threatre Lights brightned")

class HomeThreatreFacade:
    def __init__(self):
        self.amplifier = Amplifier()
        self.cdPlayer = CdPlayer()
        self.DvdPlayer = DvdPlayer()
        self.projector = Projector()
        self.screen = Screen()
        self.threatreLights = ThreatreLights()

    def watch_movie(self,movie):
        print("Watching a Movie!")
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.cdPlayer.on()
        self.cdPlayer.play()
        self.DvdPlayer.on()
        self.DvdPlayer.play()
        self.projector.on()
        self.screen.down()
        self.threatreLights.dim()

    def end_movie(self):
        self.amplifier.off()
        self.amplifier.set_volume(0)
        self.cdPlayer.off()
        self.DvdPlayer.off()
        self.projector.off()
        self.screen.up()
        self.threatreLights.bright()

if __name__ == "__main__":
    home_threatre = HomeThreatreFacade()
    home_threatre.watch_movie("Intersellar")
    home_threatre.end_movie()
    