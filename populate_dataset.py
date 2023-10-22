import os
import random
import shutil

# Define the source directory where your original image folders are located
source_directory = "../complete_dataset"

# Define the destination directory where you want to create the dataset structure
destination_directory = "../partitioned_dataset"

# Create the dataset structure
test_percentage = 0.3  # 30% for testing
train_percentage = 0.7  # 70% for training

# Create subdirectories under the destination directory
subdirectories = ["Other_(Music,Bell,Speech,Silence,Sneeze)",
                  "Emergency_Vehicle",
                  "Explosion",
                  "Gunshot",
                  "Power_Tool"]

for folder in subdirectories:
    os.makedirs(os.path.join(destination_directory, "test_30", folder), exist_ok=False)
    os.makedirs(os.path.join(destination_directory, "train_70", folder), exist_ok=False)

def getOutputDirectory(class_name):
    others = ['speech', 'sneeze', 'silence', 'music', 'bell']
    if class_name in others:
        return subdirectories[0]
    elif class_name == 'vehicle':
        return subdirectories[1]
    elif class_name == 'explosion':
        return subdirectories[2]
    elif class_name == 'gunfire':
        return subdirectories[3]
    elif class_name == 'tool':
        return subdirectories[4]
    else:
        raise Exception('Invalid class_name, aborting.')

# Copy the images to the dataset structure
for folder_name in os.listdir(source_directory):
    if os.path.isdir(os.path.join(source_directory, folder_name)):
        total_images = int(folder_name.split('_')[-1])
        test_count = int(total_images * test_percentage)
        train_count = int(total_images * train_percentage)

        files = os.listdir(os.path.join(source_directory, folder_name))
        random.shuffle(files)

        test_files = files[:test_count]
        train_files = files[test_count:(test_count + train_count)]

        class_name = folder_name.split('_')[-2]

        for file in test_files:
            source_path = os.path.join(source_directory, folder_name, file)
            destination_path = os.path.join(destination_directory, "test_30", getOutputDirectory(class_name), class_name + '_' + file)
            shutil.copy(source_path, destination_path)
        
        print(f'Finished copying the test files for {class_name}.')

        for file in train_files:
            source_path = os.path.join(source_directory, folder_name, file)
            destination_path = os.path.join(destination_directory, "train_70", getOutputDirectory(class_name), class_name + '_' + file)
            shutil.copy(source_path, destination_path)

        print(f'Finished copying the train files for {class_name}.')
    
    print(f'Finished copying files for the directory {folder_name}')

print("Dataset creation complete.")
