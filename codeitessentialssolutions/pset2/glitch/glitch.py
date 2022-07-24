'''
    Pixels
'''

from PIL import Image
import sort
from sys import argv

'''
    loadImage:
        - loadImage is a function that we have implemented for you
        - It takes in a filename from the command line argument and returns 3 values: image, width, height
        - image: a 2D list representation of the image file passed into loadImage
        - width: width of the image (number of columns in 2D list)
        - height: height of the image (number of rows in 2D list)
'''
def loadImage(filename):
    # open image
    img = Image.open(filename)

    # retrieve pixels in a 2d array
    width, height = img.size
    img = img.load()
    image = [[0] * width for i in range(height)]
    
    for y in range(height):
        for x in range(width):
            image[y][x] = list(img[x, y])
        
    return image, width, height
'''
    saveImage
        - saveImage is a function that we have implemented for you
        - It takes in the processed image (which you will implement), and outputs a new file with a new name that you input
        - The new name that you input must end with '.jpg'
'''
def saveImage(flattened_pixels, width, height, newFilename):
    for i in range(len(flattened_pixels)):
        flattened_pixels[i] = tuple(flattened_pixels[i])
    new_img = Image.new('RGB',(width, height))
    new_img.putdata(flattened_pixels)
    new_img.save(newFilename)

def sortRow(row):
    # FIND POSITION OF DARKEST PIXEL
    min = 255 + 255 + 255
    minIndex = 0
    
    for i in range(len(row)):
        current = row[i][0] + row[i][1] + row[i][2]
        if current < min:
            min = current
            minIndex = i

    # SORT FROM 0 TO POSITION FOUND
    for i in range(1, minIndex):
        j = i
        while (j != 0 and sum(row[j - 1]) > sum(row[j])):
            row[j - 1], row[j] = row[j], row[j - 1]
            j -= 1

    # ALTERNATIVELY USE SORT FUNCTIONS
    # sort.insertionSort(row, minIndex - 1)
    # sort.mergeSort(row, 0, minIndex - 1)
    return

'''
    flattenImage
    - You are to implement this function by yourself
    - This function takes in image as a 2D list of RGB values, and returns that list flattened to a 1D list of RGB values. 
'''
def flattenImage(image, width, height):
    flattened_image = [0] * (width * height)
    for y in range(height):
        for x in range(width):
            flattened_image[y * width + x] = image[y][x]
    return flattened_image

def main():
    '''
        width: width of image in px
        height: height of image in px
        image: 2D list of images, each element a tuple of RGB values
        e.g. image[0][0] is the RGB values of the first element
    '''

    # STEP 1: LOAD TO GET INITIAL PIXELS, WIDTH AND HEIGHT
    image, width, height = loadImage(argv[1])

    # STEP 2: SORT EACH ROW OF PIXELS
    for i in range(height):
        sortRow(image[i])

    # STEP 3: FLATTEN PIXELS INTO 1D LIST
    flattened_pixels = flattenImage(image, width, height)

    # STEP 4: SAVE NEW PIXELS INTO FILE
    newName = input("new file name: ")
    saveImage(flattened_pixels, width, height, newName)

if __name__ == '__main__':
    main()