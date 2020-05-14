from hummingbird import Hummingbird
from time import sleep
from playsound import playsound
import random

bird = Hummingbird()

audioFiles = [r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\03.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\04.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\05.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\07.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\09.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\10.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\11.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\12.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\13.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\14.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\15.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\16.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\17.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\18.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\19.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\21.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\22.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\23.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\24.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\25.mp3',
              r'C:\Users\robin\Desktop\Seinfeld\SeinfeldAudioSamples\Seinfeld Samples\26.mp3']

# run until manually exit program
while(1):
    while(bird.get_knob_value(1) > 22):
        # when light threshold is less than 6, play random Seinfeld bass riff
        randRiffToPlay = random.choice(audioFiles)
        playsound(randRiffToPlay)

        # sleep for 6 seconds
        sleep(6)


