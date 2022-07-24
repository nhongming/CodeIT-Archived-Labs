'''
    Pixels
'''

from PIL import Image
from sys import argv
from matplotlib.cbook import flatten

from sklearn.cluster import k_means

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

'''
    flattenImage
    - You are to implement this function by yourself
    - This function takes in image as a 2D list of RGB values, and returns that list flattened to a 1D list of RGB values. 
'''
def flattenImage(image, width, height):
    # TO IMPLEMENT
    flatten_pixels = []
    for pixel_row in range(height):
        for pixel_col in range(width):
            pixel = image[pixel_row][pixel_col]
            flatten_pixels.append(pixel)
    return flatten_pixels 

def main():
    '''
        width: width of image in px
        height: height of image in px
        image: 2D list of an image, each element a tuple of RGB values
        e.g. image[0][0] is the RGB values of the first element
    '''

    # STEP 1: LOAD TO GET INITIAL IMAGE, WIDTH AND HEIGHT
    image, width, height = loadImage(argv[1])
    # STEP 2: SORT EACH ROW OF PIXELS
    # TO IMPLEMENT
    def sort_row(row):
        darkest_color = 255*3
        darkest_color_index = 0
        #find the darkest pixel in the row
        #by using linear search
        for i in range(len(row)):
            # each pixel has an RPG value, for instance (255, 255, 255)
            temp = row[i][0] + row[i][1] + row[i][2]
            if temp < darkest_color:
                darkest_color = temp
                darkest_color_index = i
        # once index for the darkest pixel is extracted
        # perform insertion sort
        for j in range(1,(darkest_color_index+1)):
            k = j
            while ( k != 0 and sum(row[k - 1]) > sum(row[k]) ):
                temp = row[k]
                row[k] = row[k-1]
                row[k-1] = temp
                k -= 1
        return row
    # regrouping the sorted rows pixels into a new sorted image 2D array
    def sort_image(image):
        sorted_image = []
        for pixels_row in image:
            sorted_row = sort_row(pixels_row)
            sorted_image.append(sorted_row)
        return sorted_image
    
    sorted_image = sort_image(image)

    # STEP 3: FLATTEN PIXELS INTO 1D LIST
    flattened_pixels = flattenImage(sorted_image, width, height)

    # STEP 4: SAVE NEW PIXELS INTO FILE
    newName = input("new file name: ")
    saveImage(flattened_pixels, width, height, newName)

if __name__ == '__main__':
    main()