# UpdateGit

import os
import random

messages = ["totally a bug fix", "error", "id say my sanity is ookay", "whatsapp messages added", "git randoms", ":)", "i dunno", "maybe a bug fix", "possibly if I'm lucky enough I could actually reach my true typing speed, all i gotta do is believe in myself, just do it me! Duel of the fates is pretty good at keeping my speed, although my fingers want to match the speed of the song and it's at the slow bit aaaaaaaaaaaaaaaaaaaaaaaaa please help me im trying so hard to reach my true typing speed ive reached before and i shall now breach you idiot i shall do it! i can, ican, ican, i can, i can, i can! i did it! i am the best i can finally reach my true potential i can finally do it again ive unlocked it once more, the typing is unbearable im legit sweating."]

def init():
    rand = random.randint(0, len(messages) - 1)
    os.system("git add .")
    os.system("git commit -m %s" % str(messages[rand]))
    os.system("git push")

init()