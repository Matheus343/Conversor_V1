import os
import cv2 as cv

image_folder = './ImagensParaConverter'
video_name = 'weg_video.avi'

# Converte todas as imagens .bmp para .jpg
for img in os.listdir(image_folder):
    if img.endswith(".bmp"):
        img_path = os.path.join(image_folder, img)
        image = cv.imread(img_path)
        new_img_path = img_path.replace(".bmp", ".jpg")
        cv.imwrite(new_img_path, image)

# Após a conversão, carrega as imagens .jpg
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
if not images:
    print("Nenhuma imagem .jpg encontrada no diretório especificado.")
    exit()

print(f"{len(images)} imagens .jpg encontradas.")
frame = cv.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv.VideoWriter(video_name, cv.VideoWriter_fourcc(*'XVID'), 10, (width, height))

for image in images:
    video.write(cv.imread(os.path.join(image_folder, image)))

cv.destroyAllWindows()
video.release()
