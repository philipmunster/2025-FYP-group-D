import random
import os 
import cv2


def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False

class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform

        # get a sorted list of all files in the directory
        self.file_list = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of samples
        self.num_samples = len(self.file_list)

    def __len__(self):
        return self.num_samples

    def __iter__(self):
        # fill in with your own code below
        for file_name in self.file_list:
            file_path = os.path.join(self.directory, file_name)

            # read the image
            img_rgb, img_gray = readImageFile(file_path)

            # apply transformation 
            if self.transform:
                img_rgb = self.transform(img_rgb)
                img_gray = self.transform(img_gray)

            yield img_rgb, img_gray, file_name  


image_loader = ImageDataLoader(directory="data", shuffle=True)

for img_rgb, img_gray, filename in image_loader:
    print(f"Loaded image: {filename}, Shape: {img_rgb.shape}")
