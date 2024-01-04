from PIL import Image
import numpy
import  random
import os
colors = [[{"name":"Raisin Black","hex":"242331","rgb":[36,35,49],"cmyk":[27,29,0,81],"hsb":[244,29,19],"hsl":[244,17,16],"lab":[14,4,-9]},{"name":"Cafe Noir","hex":"533e2d","rgb":[83,62,45],"cmyk":[0,25,46,67],"hsb":[27,46,33],"hsl":[27,30,25],"lab":[28,7,14]},{"name":"Golden Brown","hex":"a27035","rgb":[162,112,53],"cmyk":[0,31,67,36],"hsb":[32,67,64],"hsl":[32,51,42],"lab":[51,14,40]},{"name":"Camel","hex":"b88b4a","rgb":[184,139,74],"cmyk":[0,24,60,28],"hsb":[35,60,72],"hsl":[35,44,51],"lab":[61,10,41]},{"name":"Flax","hex":"ddca7d","rgb":[221,202,125],"cmyk":[0,9,43,13],"hsb":[48,43,87],"hsl":[48,59,68],"lab":[81,-4,41]}],
[{"name":"Carnation Pink","hex":"ff99c9","rgb":[255,153,201],"cmyk":[0,40,21,0],"hsb":[332,40,100],"hsl":[332,100,80],"lab":[75,44,-8]},{"name":"Languid Lavender","hex":"c1bddb","rgb":[193,189,219],"cmyk":[12,14,0,14],"hsb":[248,14,86],"hsl":[248,29,80],"lab":[78,7,-14]},{"name":"Pale Cerulean","hex":"a2c7e5","rgb":[162,199,229],"cmyk":[29,13,0,10],"hsb":[207,29,90],"hsl":[207,56,77],"lab":[79,-5,-19]},{"name":"Turquoise Blue","hex":"58fcec","rgb":[88,252,236],"cmyk":[65,0,6,1],"hsb":[174,65,99],"hsl":[174,96,67],"lab":[91,-46,-5]},{"name":"Kombu Green","hex":"303a2b","rgb":[48,58,43],"cmyk":[17,0,26,77],"hsb":[100,26,23],"hsl":[100,15,20],"lab":[23,-8,8]}],
 [{"name":"Dark Sienna","hex":"482728","rgb":[72,39,40],"cmyk":[0,46,44,72],"hsb":[358,46,28],"hsl":[358,30,22],"lab":[20,16,6]},{"name":"Twilight Lavender","hex":"7e4e60","rgb":[126,78,96],"cmyk":[0,38,24,51],"hsb":[338,38,49],"hsl":[338,24,40],"lab":[39,23,-2]},{"name":"Opera Mauve","hex":"b287a3","rgb":[178,135,163],"cmyk":[0,24,8,30],"hsb":[321,24,70],"hsl":[321,22,61],"lab":[61,21,-8]},{"name":"Aero Blue","hex":"c0f8d1","rgb":[192,248,209],"cmyk":[23,0,16,3],"hsb":[138,23,97],"hsl":[138,80,86],"lab":[93,-25,13]},{"name":"Laurel Green","hex":"bdcfb5","rgb":[189,207,181],"cmyk":[9,0,13,19],"hsb":[102,13,81],"hsl":[102,21,76],"lab":[81,-11,11]}],[{"name":"Dark Liver Horses","hex":"503d3f","rgb":[80,61,63],"cmyk":[0,24,21,69],"hsb":[354,24,31],"hsl":[354,13,28],"lab":[28,9,2]},{"name":"Dark Liver","hex":"615756","rgb":[97,87,86],"cmyk":[0,10,11,62],"hsb":[5,11,38],"hsl":[5,6,36],"lab":[38,4,2]},{"name":"Polished Pine","hex":"539987","rgb":[83,153,135],"cmyk":[46,0,12,40],"hsb":[165,46,60],"hsl":[165,30,46],"lab":[58,-27,3]},{"name":"Medium Spring Green","hex":"52ffb8","rgb":[82,255,184],"cmyk":[68,0,28,0],"hsb":[155,68,100],"hsl":[155,100,66],"lab":[90,-60,21]},{"name":"Turquoise Blue","hex":"4dfff3","rgb":[77,255,243],"cmyk":[70,0,5,0],"hsb":[176,70,100],"hsl":[176,100,65],"lab":[91,-47,-7]}],
 [{"name":"Umber","hex":"695958","rgb":[105,89,88],"cmyk":[0,15,16,59],"hsb":[4,16,41],"hsl":[4,9,38],"lab":[39,6,3]},{"name":"Laurel Green","hex":"b6c8a9","rgb":[182,200,169],"cmyk":[9,0,16,22],"hsb":[95,16,78],"hsl":[95,22,72],"lab":[79,-12,13]},{"name":"Aero Blue","hex":"c8ead3","rgb":[200,234,211],"cmyk":[15,0,10,8],"hsb":[139,15,92],"hsl":[139,45,85],"lab":[90,-15,7]},{"name":"Aero Blue","hex":"cfffe5","rgb":[207,255,229],"cmyk":[19,0,10,0],"hsb":[148,19,100],"hsl":[148,100,91],"lab":[96,-20,7]},{"name":"Gainsboro","hex":"cedada","rgb":[206,218,218],"cmyk":[6,0,0,15],"hsb":[180,6,85],"hsl":[180,14,83],"lab":[86,-4,-1]}]]
def random_palette(size):
    palette = []
    for i in range(size):
        palette.append({"rgb":[random.randint(0,255),random.randint(0,255),random.randint(0,255)]})
    return palette
def image_to_pixelart(file,final,round):
    img = Image.open(file)
    img = numpy.asarray(img)

    for x in range(len(img)):
        for y in range(len(img[0])):
            img[x][y] =  (img[x][y][0]-divmod(img[x][y][0],round)[1],img[x][y][1]-divmod(img[x][y][1],round)[1],img[x][y][2]-divmod(img[x][y][2],round)[1])
    img = Image.fromarray(img)
    img.save(final)
def image_to_pixelart_using_palette(file,final,palette,size = -1):
    if size == -1:
        img = Image.open(file)
    else:
        img = resize_image(file,size)
    img = numpy.asarray(img)
    def getcolor(color):
        min = 99999999
        minind = 0

        for i in range(len(palette)):
            temp = sum(color-palette[i]["rgb"])
            if abs(temp)<min:
                min = abs(temp)
                minind = i
        return palette[minind]["rgb"]
    it = 0
    for x in range(len(img)):
        for y in range(len(img[0])):
            printProgressBar(it,len(img)*len(img[0]))
            it+=1
            img[x][y] = getcolor(img[x][y])
    img = Image.fromarray(img)
    img.save(final)
def resize_image(name,size):
    img = Image.open(name)
    d = [size,int(size*len(numpy.asarray(img)[0])/len(numpy.asarray(img)))]
    print(d)
    img = img.resize((int(size*(len(numpy.asarray(img)[0])/len(numpy.asarray(img)))), size ), Image.ANTIALIAS)
    return img
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    import sys
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print()
def image_to_all_palette(file,foldername,palettes,size = -1):
    os.makedirs(foldername,exist_ok=True)
    for i in range(len(palettes)):
        image_to_pixelart_using_palette(file, f"{foldername}/{i}.png", palettes[i],size)

#image_to_pixelart("jesus-name-powerful-1.jpg","mashala.jpg",50)
image_to_pixelart_using_palette("mac.jpg","random.png",random_palette(10),200)
