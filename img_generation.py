from PIL import Image 

pose = ""
face = ""
hairstyle = ""
collor = ""
color_r, color_g, color_b = 0,0,0

def getFace(i):
    face = "" 
    if i % 8 == 1:
        face = "pensive" 
    if i % 8 == 2:
        face = "amazed" 
    if i % 8 == 3:
        face = "blush" 
    if i % 8 == 4:
        face = "happy" 
    if i % 8 == 5:
        face = "lmao" 
    if i % 8 == 6:
        face = "angry" 
    if i % 8 == 7:
        face = "surprized" 
    if i % 8 == 0:
        face = "smile" 
    return face

def getPose(i):
    pose = ""
    if int((i - 1)/ 24) == 0: # 0 0
        pose = "epic"
    if int((i - 1)/ 24) == 1: # 1 1
        pose = "rare"
    if int((i - 1)/ 24) == 2: # 2 3
        pose = "uncommon"
    if int((i - 1)/ 24) == 3: # 3 2
        pose = "common"
    return pose 

def getHairstyle(i):
    hairstyle = ""
    if i - int(i / 24)*24 >= 1 and i - int(i / 24)*24 <= 8:
        hairstyle = "rare"
    if i - int(i / 24)*24 >= 9 and i - int(i / 24)*24 <= 16:
        hairstyle = "uncommon"
    if i - int(i / 24)*24 >= 17 and i - int(i / 24)*24 <= 24:
        hairstyle = "epic"
    if i % 24 == 0:
        hairstyle = "epic"
    return hairstyle

def getColor(j):
    if j == 0:
        return "cloud-shadow", 105, 61, 61
    if j == 1:
        return "red-clay", 164, 56, 32
    if j == 2:
        return "honey", 235, 138, 62 
    if j == 3:
        return "fog", 185, 196, 201 
    if j == 4:
        return "thundercloud", 80, 81, 86
    if j == 5:
        return "asphalt", 50, 56, 77 
    if j == 6:
        return "pollen", 255, 214, 77
    if j == 7:
        return "coffe", 179, 136, 103
    if j == 8:
        return "sandstone", 125, 86, 66 
    if j == 9:
        return "smog", 244, 235, 219 

def createImg(i, age, pose, hairstyle, face, color, color_r, color_g, color_b):
    image = Image.open("./3_dogs/3_"+str(i)+".png").convert('RGBA')

    image.load()
    r, g, b, a = image.split()
    result_r, result_g, result_b, result_a = [], [], [], []
    # Обрабатывать каждый пиксель по очереди
    for pixel_r, pixel_g, pixel_b, pixel_a in zip(r.getdata(), g.getdata(), b.getdata(), a.getdata()):
        if pixel_r == 239 and pixel_g == 220 and pixel_b == 211: 
            pixel_r, pixel_g, pixel_b = color_r, color_g, color_b

        result_r.append(pixel_r)
        result_g.append(pixel_g)
        result_b.append(pixel_b)
        result_a.append(pixel_a)

    r.putdata(result_r)
    g.putdata(result_g)
    b.putdata(result_b)
    a.putdata(result_a)

    image = Image.merge('RGBA', (r, g, b, a))
    # Вывод картинки
    image.save("./child/"+age+"_"+pose+"_"+hairstyle+"_"+face+"_"+color+".png", quality=100)



for i in range(1, 97):
    pose = getPose(i)
    face = getFace(i)
    hairstyle = getHairstyle(i)
    for j in range(10):
        color, color_r, color_g, color_b = getColor(j)

        createImg(i, "child", pose, hairstyle, face, color, color_r, color_g, color_b)

