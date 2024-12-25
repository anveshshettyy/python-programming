class MusicPlayer():
    def play(self):
        pass

class Mp3Player(MusicPlayer):
    def play_mp3(self):
        print (f"Playing MP3 Music")

class CdPlayer(MusicPlayer):
    def play_cd(self):
        print (f"Playing CD Player")

class MusicPlayerAdapter(MusicPlayer):
    def __init__(self, player):
        self.adapter = player

    def play(self):
        if isinstance(self.adapter,Mp3Player):
            self.adapter.play_mp3()
        elif isinstance(self.adapter,CdPlayer):
            self.adapter.play_cd()
        
def main():
    mp3_player = Mp3Player()
    cd_player = CdPlayer()

    mp3_adapter = MusicPlayerAdapter(mp3_player)
    cd_adapter = MusicPlayerAdapter(cd_player)

    mp3_adapter.play()
    cd_adapter.play()

if __name__ == "__main__":
    main()
        