import os
import cv2 as cv
import numpy as np

videos_path = 'VideosParaConverter'
images_main_path = 'ImagensConvertidas'


if __name__ == '__main__':
    videos = [f for f in os.listdir(videos_path) if f.endswith('.avi')]
    for video in videos:
        images_dir, _ = os.path.splitext(video)
        image_name = images_dir.split('/')[-1]
        images_path = os.path.join(images_main_path, images_dir)
        os.makedirs(images_path, exist_ok=True)
        cap = cv.VideoCapture(os.path.join(videos_path, video))
        frame_id = 0
        while True:
            grabbed, frame = cap.read()
            if not grabbed:
                break
            cv.imwrite(os.path.join(images_path, '%s%09d.jpg' % (image_name, frame_id)), frame)
            frame_id += 1
