import os
import subprocess
import glob

print(os.getcwd())
os.chdir("C:/Users/marketa.sokolova/Desktop/Maky test/raw_data")


def run_fastqc():
    # 1. Define where the data is and where the results should go
    input_folder = "Illumina_Data"
    output_folder = "QC_Results"

    # 2. Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")

    # 3. Find all your fastq.gz files in the Illumina folder
    files = glob.glob(os.path.join(input_folder, "*.fastq.gz"))
    
    if not files:
        print(f"No files found in {input_folder}! Check your folder names.")
        return

    print(f"Found {len(files)} files. Starting QC...")

    # 4. Loop through each file and run the FastQC command
    for f in sorted(files):
        print(f"--- Analyzing: {os.path.basename(f)} ---")
        
        # This is the command that runs the software you installed
        # ['fastqc', 'input_file', '-o', 'output_folder']
        command = ["fastqc", f, "-o", output_folder]
        
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error analyzing {f}: {e}")

    print("\n" + "="*30)
    print("QC ANALYSIS COMPLETE!")
    print(f"All HTML reports are in the '{output_folder}' folder.")
    print("="*30)

if __name__ == "__main__":
    run_fastqc()


#Moving the files from subfolder (raw data) to the "upper fodler"
import shutil


# 1. Define where files are and where they should go
source_folder = "raw-data/QC_Results"
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
    