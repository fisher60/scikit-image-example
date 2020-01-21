from image_processing_class import image_data

if __name__ == "__main__":
    rgb_img = image_data('dog1.png')

    rgb_img.process(hue_threshold=0.08)
