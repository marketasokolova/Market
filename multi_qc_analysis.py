#Moving the files from subfolder (raw data) to the "upper fodler"
import shutil
import glob
import os
print(os.getcwd())
os.listdir()


# 1. Define where files are and where they should go
source_folder = "raw_data/QC_Results"
destination_folder = "QC_Results"

# 2. Create the "upper" destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created: {destination_folder}")

# 3. Find all QC files (.html and .zip)
files_to_move = glob.glob(os.path.join(source_folder, "*_fastqc*")) + \
                glob.glob(os.path.join(source_folder, "multiqc*"))

if not files_to_move:
    print("No files found to move. Check if 'raw-data/QC_Results' has files in it.")
else:
    print(f"Moving {len(files_to_move)} files to {destination_folder}...")
    for file_path in files_to_move:
        # Get just the filename
        file_name = os.path.basename(file_path)
        # Move it to the new upper folder
        shutil.move(file_path, os.path.join(destination_folder, file_name))
    
    print("Move complete!")

# 4. Optional: Remove the now-empty subfolder
if os.path.exists(source_folder) and not os.listdir(source_folder):
    os.rmdir(source_folder)
    print(f"Removed empty folder: {source_folder}")
    