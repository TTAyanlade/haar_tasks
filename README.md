# EC1

Idea. used face detector to extract the 5 characters (data and code in chars). then i trained and saved pkl file.
for usage, i extract frame run detector from face recognition  then use my classifier (see recognize_faces function in detector.py) output is saved to outputs folder. I tried to truncate the file for the html but i had some issues for some weird reason that did not happen to other videos


## Steps.

This was done after EC2. So i used same environment

I took video from friends. created frames and using face xml. standard, I didnt have to train a new one. I just renamed it to friends because there were so many xml files in my working directory.

created the set of images for each character. I am attaching the images to this repo.

So i trained a classifier using:
python detector.py --train 

the model is saved as a pkl file in output.

So I can use the classifier to to classify frames of the video.
python detector.py --test -f path_to_image.mp4

See final video in output folder


Note:
cb - Chandler bing
mn - Monica
pb - Phoebe Buffay
rg - Ross Geller
rgr - Rachel Green



# EC2


## Haar Cascade Training for Sunflower Detection (Caltech101)

Just a rough log of what I did to train a Haar cascade for the sunflowwer

I used OpenCV 3.x.

## Steps

I used the Caltech101 sunflower class as my positive samples.

I randomly picked images from other classes in Caltech101 and used them as negatives.

I Used match.py to align .mat annotations with .jpg images. Manually renamed the output .txt to positive.dat

Set up a new conda env with OpenCV 3.x 

Downloaded OpenCV source. Built the tools using cmake and make (needed opencv_createsamples and opencv_traincascade binaries).

Generated vector file and train

I used the following 

python
import os

os.system("mkdir sf_detect")

os.system("opencv_createsamples -info positive.dat -vec positive.vec -w 30 -h 30")

os.system("opencv_traincascade -data sf_detect -vec positive.vec -bg negative.dat -numPos 85 -numNeg 166 -numStages 10 -w 30 -h 30")



Notes
The positive.dat file has lines like:
dataset/images/image_0001.jpg 1 60 16 230 228

same for negatives. but bounding box coordinates not neccesary