import os

print(os.getcwd())
os.listdir()

os.chdir("C:/Users/marketa.sokolova/Desktop/Maky test/raw_data")
print("new location", os.getcwd())

import gzip
import glob

# Search for the files
my_list = sorted(glob.glob("*.fastq.gz"))

if len(my_list) == 0:
    print("Zero files found! Are you in the right folder?")
else:
    print("--- SUCCESS: FILES FOUND ---")
    
    # Let's peek at the first file in your list
    first_filename = my_list[0]
    
    with gzip.open(first_filename, 'rt') as f:
        first_line = f.readline().strip()
        print(f"File Name: {first_filename}")
        print(f"Header:    {first_line}")
    
    print(f"Total number of files: {len(my_list)}")

import gzip
import glob

# This finds all your files
files = glob.glob("*.fastq.gz") 

print("--- HEADER INSPECTION ---")

for f in files:
    try:
        with gzip.open(f, 'rt') as temp:
            header = temp.readline().strip()
            # This prints the filename and just the first line
            print(f"FILE: {f}")
            print(f"HEAD: {header}")
            print("-" * 20)
    except Exception as e:
        print(f"Could not read {f}: {e}")

print("--- END OF LIST ---")


import os
import shutil

# 1. Create folders
os.makedirs("Illumina_Data", exist_ok=True)
os.makedirs("PacBio_Data", exist_ok=True)

# 2. Find files 
files = glob.glob("*.fastq.gz") 

for f in files:
    with gzip.open(f, 'rt') as temp:
        header = temp.readline()
    
    # 3. Logic based on your example headers
    if "/ccs/" in header:
        print(f"Moving {f} to PacBio_Data")
        # Extract just the filename if it was already in a subfolder
        base_name = os.path.basename(f)
        shutil.move(f, os.path.join("PacBio_Data", base_name))
    elif "M03" in header or "length=251" in header:
        print(f"Moving {f} to Illumina_Data")
        base_name = os.path.basename(f)
        shutil.move(f, os.path.join("Illumina_Data", base_name))

print("Done.")

def get_stats(folder_path):
    print(f"\nStats for {folder_path}:")
    print(f"{'File Name':<30} | {'Reads':<10} | {'Avg Length':<10}")
    print("-" * 55)
    
    for f in glob.glob(f"{folder_path}/*.fastq.gz"):
        count = 0
        total_len = 0
        with gzip.open(f, 'rt') as temp:
            for i, line in enumerate(temp):
                if i % 4 == 1: # This is the sequence line
                    count += 1
                    total_len += len(line.strip())
        
        avg_len = total_len / count if count > 0 else 0
        print(f"{os.path.basename(f):<30} | {count:<10} | {avg_len:<10.1f}")

get_stats("Illumina_Data")
get_stats("PacBio_Data")



