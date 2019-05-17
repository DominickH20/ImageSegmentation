import numpy as np
from PIL import Image
from k_means_clustering import k_means

#Given an image, return the pixel RGB data as a 1D vector
def read_image_pixels(filename):
    im = Image.open(filename)
    pixels = im.load()
    RGB_vectors = []
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            RGB_vectors.append(pixels[i,j])
    return np.asarray(RGB_vectors)

#Take an image, segment it, and output the segmented image
def write_clustered_image(infile,outfile, k):
    print("Importing Data...")
    data = read_image_pixels(infile)

    print("Clustering...")
    means, indicators = k_means(data,k,True)

    print("Segmenting...")
    segment(data,means,indicators)

    size = Image.open(infile).size
    img_array = reshape(data,size)

    out = Image.fromarray(img_array.astype('uint8'))
    out.save(outfile)

#Replace pixels in data with the means to which they are assigned
def segment(data,means,indicators):
    for n in range(len(data)):
        tmp = means[np.argmax(indicators[n])]
        data[n] = np.asarray([int(x) for x in tmp])

#Convert 1D vector to a 2D matrix that can be written to an image
def reshape(data, size):
    img_array = np.zeros((size[1],size[0],len(data[0])))
    for i in range(size[1]):
        for j in range(size[0]):
            img_array[i][j] = data[(i + j*size[1])]
    return img_array


#MAIN
if __name__ == '__main__':
    k=4
    #write_clustered_image("Images/ferrari.jpg","Images/ferrari_segmented_" + str(k)+ ".jpg",k)
    #write_clustered_image("Images/bugatti.jpg","Images/bugatti_segmented_" + str(k)+ ".jpg",k)
    #write_clustered_image("Images/tree.jpg","Images/tree_segmented_" + str(k)+ ".jpg",k)
    #write_clustered_image("Images/penguin.jpg","Images/penguin_segmented_" + str(k)+".jpg",k)
    #write_clustered_image("Images/droplets.jpg","Images/droplets_segmented_" + str(k)+".jpg",k)
    for k in range(2,8):
        write_clustered_image("Images/highland_park_flowers.jpeg","Images/highland_park_flowers_segmented_" + str(k) +".jpeg",k)
