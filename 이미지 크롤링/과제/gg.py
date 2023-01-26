from PIL import Image

img=Image.open('image folder\lenna.png')
print(img.size)
print(img.format)

img.show()

# 이미지 부분 잘라내기
# crop(left, upper, right, lower)
area = (100, 100, 320, 320)
cropImage = img.crop(area)
img.show() # 원본 이미지 화면 출력
cropImage.show() # 잘려진 이미지(cropped image) 화면 출력

size = (64, 64)
img.thumbnail(size) # Thumbnail 이미지 생성
img.save('lenna-thumb.png') # Thumbnail을 저장함
img.show()


img2 = img.resize((300, 300)) # tuple 형태의 크기(가로 크기, 세로 크기)
img2.save('lenna_300.png')
img3 = img.rotate(90) # counter-clockwise (반시계방향)
img3.save('lenna_rotate.png')
img3.show()

mirrorImage = img.transpose(Image.FLIP_LEFT_RIGHT) # y축을 기준으로 x값 이동
mirrorImage.save('lenna-mirror.png')

