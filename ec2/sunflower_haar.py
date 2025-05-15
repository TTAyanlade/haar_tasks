import os

os.system("mkdir sf_detect")

os.system("opencv_createsamples -info positive.dat -vec positive.vec -w 30 -h 30")

os.system("opencv_traincascade -data sf_detect -vec positive.vec -bg negative.dat -numPos 85 -numNeg 166 -numStages 10 -w 30 -h 30")


import subprocess

# subprocess.run(["opencv_createsamples", "-info", "positive.dat", "-vec", "positive.vec", "-w", "30", "-h", "30"])
