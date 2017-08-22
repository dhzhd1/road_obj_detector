import cv2
import numpy as np
import os
import io

class Data:
    def __init__(self, notation_file, training_folder, wild_testing_folder, split_ratio=0.8):
        self.notation_file = notation_file
        self.training_folder = training_folder
        self.wild_testing_folder = wild_testing_folder
        self.split_ratio = split_ratio
        self.notation_list = []

    def load_notations(self):
        with io.open(self.notation_file,'r') as n:
            notation_content = n.readlines()
        image_list = np.array(notation_content)
        print(image_list[0])

    def image_transform_mirror(self, image_path):
        """
        This method will generate a new image with mirrored from the original image from the image_path
        :param image_path: String of image_path
        :return: image in numpy array as well as a new bounding box coordinates notation
        """
        pass

    def image_transform_contrast(self, image_path, new_image_num=1):
        """
        This method will generate image with random contrast
        :param image_path:
        :param new_image_num: number of new images
        :return: list of images which in numpy array format
        """
        pass

    def image_transform_brightness(self, image_path, new_image_num=1):
        """
        This method will generate image with random brightness
        :param image_path:
        :new_image_num: number of new images
        :return: list of images which in numpy array format
        """
        pass

    def image_transform_blur(self, image_path, num_image_num=1, blur_method='all', **blur_param):
        """
        generate several blur images for training set
        :param image_path:
        :param num_image_num: number of new images
        :param blur_method:  'Gaussian', 'Median','all'
        :param blur_param: blur parameters;
                            Gaussian [(kernel_size), sigma = sigmaX = sigmaY]
                            Median [(kernel_size)]
                            all of the kernel size should be positive and odd number
        :return:
        """
        pass

    def screen_bad_label(self):
        """
        drop the labels which doesn't include any object notation
        :return: new label list without empty labels
        """
        pass


if __name__ == '__main__':
    new_train_dataset = '../dataset/new_train/'
    train_folder = '../dataset/training/'
    test_folder = '../dataset/testing/'
    notation_file_path = os.path.join(train_folder,'label.idl')
    data = Data(notation_file_path, train_folder, test_folder)
    data.load_notations()


