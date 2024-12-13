import requests
from matplotlib import pyplot as plt
from PIL import Image

url = 'https://yandex.ru/pogoda'
params = {'lat': 54.3282, 'lon': 48.3866}
response = requests.get(url, params)
print(response.status_code)
print(response.encoding)
print(response.url)

url_pict = ('https://rgo.ru/upload/content_block/images/fb0a50cf56489987132ab488c36e37cb/'
            '6410ca87dad3c1ceeef45741a4388f4f9.jpg')
response = requests.get(url_pict)
with open('tiger.jpg', 'wb') as picture:
    picture.write(response.content)


x = [0, 10, 20, 30, 40]
y = [0, 32, 15, 25, 20]
y2 = [0, 28, 22, 27, 35]
plt.plot(x, y, color='#DA70D6', marker='.', markersize=7)
plt.plot( x, y2, color='#ADD8E6', marker='.', markersize=7)
plt.grid()
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('График')
plt.show()


image = Image.open('tiger.jpg')
image_new = image.save('tiger.png')
image_new = Image.open('tiger.png')
image_crop = image_new.crop((950, 100, 1900, image_new.height))
image_crop.show()
