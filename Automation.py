import os
import shutil

# Define the source directory
source_dir = "path/to/source/directory"

# Define the target directories for different file types
target_dirs = {
    "images": "path/to/target/directory/images",
    "documents": "path/to/target/directory/documents",
    "music": "path/to/target/directory/music",
}

# Define file extensions for each category
file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".doc", ".docx", ".txt"],
    "music": [".mp3", ".wav", ".flac"],
}

def organize_files():
    for filename in os.listdir(source_dir):
        file_extension = os.path.splitext(filename)[1]
        moved = False

        for category, extensions in file_types.items():
            if file_extension in extensions:
                target_path = target_dirs[category]
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                shutil.move(os.path.join(source_dir, filename), target_path)
                print(f"Moved: {filename} to {target_path}")
                moved = True
                break
        
        if not moved:
            print(f"File {filename} did not match any category.")

if __name__ == "__main__":
    organize_files()
