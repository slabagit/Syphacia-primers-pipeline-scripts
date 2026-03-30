import os

def download_and_split_sra(sra_list, output_dir):
    """
    Downloads and splits paired-end SRA data using fastq-dump.
    Requires SRA Toolkit to be installed and accessible in the system PATH.
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Download each SRA file and split into reverse and forward reads fastq files
    for sra in sra_list:
        print(f"Downloading and splitting SRA: {sra}")
        
        # Call fastq-dump to download and split the SRA file
        # The --split-files option will create separate files for forward and reverse reads
        # The -O option specifies the output directory for the downloaded files
        os.system(f"fastq-dump {sra} --split-files -O {output_dir}")

    print("Trimming completed for all samples.")

# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    # List of SRA accession numbers to download
    my_sra_list = [
        "ERR1468425",
        "ERR1468426",
        "ERR1468428",
        "ERR1468597",
        "ERR1468598",
        "ERR1468599",
        "ERR1468600",
    ]

    # Define output directory in the current working directory
    my_output_dir = "./raw_data"

    # Run the download and split function
    download_and_split_sra(sra_list=my_sra_list, output_dir=my_output_dir)
