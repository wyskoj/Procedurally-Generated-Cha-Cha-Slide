from pydub import AudioSegment
import os, random

outputPath = "output.wav"
outputData = AudioSegment.from_wav("clips/funky.wav") + AudioSegment.from_wav("clips/beat/beat_normal.wav")

for x in range(0, 1000):
    print(x)
    soundType = random.randint(0, 100)
    if soundType < 15:
        outputData += AudioSegment.from_wav("clips/cha_cha/" + random.SystemRandom().choice(os.listdir("clips/cha_cha")))
        outputData += AudioSegment.from_wav("clips/beat/cha_cha/" + random.SystemRandom().choice(os.listdir("clips/beat/cha_cha")))
        outputData += AudioSegment.from_wav("clips/beat/beat_normal.wav")
    elif soundType < 20:
        outputData += AudioSegment.from_wav("clips/freeze_everybody_clap_your_hands.wav")
        for y in range(0, (2 ** random.randint(1, 3)) - 1):
            outputData += AudioSegment.from_wav("clips/beat/clapping/beat_clapping_0.wav")
        outputData += AudioSegment.from_wav("clips/beat/clapping/beat_clapping_1.wav")
        outputData += AudioSegment.from_wav("clips/beat/beat_normal.wav")
    elif soundType < 25:
        outputData += AudioSegment.from_wav("clips/five_hops_this_time.wav")
        outputData += AudioSegment.from_wav("clips/beat/beat_synth.wav")
    elif soundType < 30:
        outputData += AudioSegment.from_wav("clips/charlie_brown.wav")
        outputData += AudioSegment.from_wav("clips/beat/beat_synth.wav")
    elif soundType < 40:
        outputData += AudioSegment.from_wav("clips/reverse/" + random.SystemRandom().choice(os.listdir("clips/reverse")))
        outputData += AudioSegment.from_wav("clips/beat/beat_reverse.wav")
    elif soundType < 70:
        outputData += AudioSegment.from_wav("clips/normal/" + random.SystemRandom().choice(os.listdir("clips/normal")))
        outputData += AudioSegment.from_wav("clips/beat/beat_normal.wav")
    else:
        outputData += AudioSegment.from_wav("clips/synth/" + random.SystemRandom().choice(os.listdir("clips/synth")))
        outputData += AudioSegment.from_wav("clips/beat/beat_synth.wav")

outputData.export(outputPath, format="wav")