from image_processing_class import Image_data
from os import listdir
from os.path import isfile, join

images_path = '../sample_images/'
people_path = images_path + 'people/'

files_to_analyze = [f for f in listdir(people_path) if isfile(join(people_path, f))]


if __name__ == "__main__":

    image_objects_list = [Image_data(join(people_path, f)) for f in files_to_analyze]
    for image_object in image_objects_list:

        threshold = sum(image_object.hue_img)/len(image_object.hue_img)

        threshold = sum(threshold)/len(threshold)

        print(threshold)

        image_object.process(hue_threshold=threshold)
