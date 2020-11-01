import pygame


pygame.init()


class Audio:
    def __init__(self, game):

        self.game = game

        self.pause_tampon = None

        pygame.mixer.init()

        # Musics (only mp3)
        self.playlist = list()

        self.music_theme = '../assets/audio/ost/theme.mp3'
        self.music_theme2 = '../assets/audio/ost/theme2.mp3'
        self.pause = '../assets/audio/ost/pause.mp3'
        self.over = '../assets/audio/ost/over.mp3'

        # Sounds
        # Note Nath : seules les format .ogg sont accepté, et parfois les .wav
        self.sound_click = pygame.mixer.Sound('../assets/audio/sounds/click.wav')
        self.sound_laser = pygame.mixer.Sound('../assets/audio/sounds/laser.ogg')
        self.sound_heal = pygame.mixer.Sound('../assets/audio/sounds/heal.wav')
        self.sound_comet = pygame.mixer.Sound('../assets/audio/sounds/comet.wav')

    def start_music(self, song):
        if type(song) != list:

            pygame.mixer.music.load(getattr(self, song, 'the song entered isn\'t settled ;p'))
            #if self.pause_tampon != None and not(song=='pause'):
             #   pygame.mixer.music.set_pos(self.pause_tampon)
            pygame.mixer.music.play(-1, 0)

        else:
            self.playlist.clear()
            self.playlist.extend([s for s in song])
            pygame.mixer.music.load(self.playlist.pop())  # Get the first track from the playlist
            pygame.mixer.music.queue(self.playlist.pop())  # Queue the 2nd song,...
            pygame.mixer.music.play()  # Play the music

    @staticmethod
    def end_music():
        pygame.mixer.music.stop()


    def pause_music(self):
        self.pause_tampon = pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()

    @staticmethod
    def unpause_music():
        pygame.mixer.music.unpause()

    def make_sound(self, sound):
        t = getattr(self, sound, 'le song n\'est pas chargé')
        t.set_volume(2)
        t.play()
