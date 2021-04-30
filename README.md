A Body Mass Index detection system from facial images the algorithm used is Random Forest Regressor. The images have been converted into face encodings to work well with Machine Learning algorithms. 

The following libraries have been used for the project -
1.	Numpy
2.	pandas
3.	re (for regex processing)
4.	matplotlib (displaying of image and plots)
5.	dlib (mandatory for face_recognition library to work)
6.	opencv
7.	glob (reading images from file folder)
8.	pathlib
9.	scikit-learn (Machine Learning)
10.	face_recognition (library for face detection)
11.	IPython
12.	seaborn 
13.	Flask (for app deployment)

Dataset -
The dataset consists of 288 images of 54 different individuals. These individuals are a mixture of celebrities and common persons. All the images considered in this dataset are frontal facing. In a CSV file the height, weight, BMI, name and gender of these individuals are stored. The images are stored in ‘jpg’ and ‘jpeg’ format.
The dataset was enriched from time to time whenever accuracy problems were encountered for some type of images. eg. Senior citizens pictures were not available initially. To overcome this situation, front facing images were collected from senior citizens and added in the training set. 
The data collection task was done carefully to include every height and weight group. 

The application architecture is as follows -

![image](https://user-images.githubusercontent.com/50106830/116661917-bde36000-a9b2-11eb-8b79-92ad1465f1e3.png)

Note - The dataset cannot be shared as it contains images and data of the subjects.
