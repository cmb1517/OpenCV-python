import os
import numpy as np
import cv2
from glob import glob


def create_dir(path):
  try:
    if not os.path.exists(path):
      os.makedirs(path)
  except OSError:
    print(f'ERROR: creating dir with name {path}')

def save_frame(video_path, save_dir):
  name = video_path.split("/")[-1].split(".")[0]
  save_path = os.path.join(save_dir, name)
  create_dir(save_path)

video_paths = glob("Videos/*")
save_dir = "save"

for path in video_paths:
  save_frame(path, save_dir)


video = cv2.VideoCapture("TestVideo.mp4")

idx = 0

gap = 1

while True:
  ret, frame = video.read()

  if ret == False:
    video.release()
    break

  if idx == 0:
    cv2.imwrite("./Images/frame"+str(idx)+".jpeg", frame)
  else:
    if idx % gap == 0:
      cv2.imwrite("./Images/frame"+str(idx)+".jpeg", frame)

  idx += 1
