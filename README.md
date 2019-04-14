# Image Segmentation

The repository demonstrates the use of the _K_-Means Algorithm to segment images into related color components. This has the practical application of allowing images to be compressed further than otherwise possible, so long as one is satisfied with an image containing only _K_ colors. Images are passes as input to the algorithm by treating each pixel as a unique 3-dimensional data point **<R,G,B>** where each dimension can take on values ranging from 0 - 255.

`k_means_clustering.py` contains the core implementation of the _K_-Means Algorithm and related objective functions that are useful for studying algorithm performance. It also contains functions that generate a random data set from _K_ Gaussian Distributions with varying means and equal covariance. To see an example of the algorithm running, execute this file, varying the parameter, _k_ in the main if you so desire. The program will display the data set, cluster assignments, and objective function performance.

`image_segmenter.py` contains the functions used to convert an image to a data set of **<R,G,B>** vectors, classify the points, and replace the pixels with associated means for segmentation. To try this on other images apart from the examples in this repository, simply path to the input image and output destination (as demonstrated in the main) and execute this file.

## Segmentation Examples

### K = 2 Means
![alt text](./Images/bugatti_segmented_2.jpg?raw=true)
### K = 3 Means
![alt text](./Images/bugatti_segmented_3.jpg?raw=true)

<img align="left"  src="./Images/bugatti_segmented_2.jpg">

### K = 4 Means
![alt text](./Images/bugatti_segmented_4.jpg?raw=true)
### K = 7 Means
![alt text](./Images/bugatti_segmented_7.jpg?raw=true)

### K = 10 Means
![alt text](./Images/bugatti_segmented_10.jpg?raw=true)
### Original Image
![alt text](./Images/bugatti.jpg?raw=true)
