# split data into training and testing set
import os, random, shutil

os.mkdir('chess-detection/train')
os.mkdir('chess-detection/test')

image_paths = os.listdir('chess-detection/images')
random.shuffle(image_paths)

for i, image_path in enumerate(image_paths):
  if i < int(len(image_paths) * 0.8):
    shutil.copy(f'chess-detection/images/{image_path}', 'chess-detection/train')
    shutil.copy(f'chess-detection/annotations/{image_path.replace("JPG", "xml")}', 'chess-detection/train')
  else:
    shutil.copy(f'chess-detection/images/{image_path}', 'chess-detection/test')
    shutil.copy(f'chess-detection/annotations/{image_path.replace("JPG", "xml")}', 'chess-detection/test')