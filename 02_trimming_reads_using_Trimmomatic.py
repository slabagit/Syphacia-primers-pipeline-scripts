import os

def run_trimmomatic(id_list, input_dir, output_dir, trimmomatic_jar, adapter_file):
    """
    Runs Trimmomatic in paired-end (PE) mode to trim adapters and filter low-quality reads.
    Requires Java to be installed and accessible in the system PATH.
    """

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
	    os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")


    # Loop through each sample and run Trimmomatic
    for id in id_list:
        print(f"Trimming sample: {id}")
    
        # Define input file paths to downloaded fastq files
        R1 = f"{input_dir}/{id}_1.fastq"
        R2 = f"{input_dir}/{id}_2.fastq"

        # Define output file paths for paired and unpaired reads
        out_p1 = f"{output_dir}/{id}_1_paired.fastq"
        out_up1 = f"{output_dir}/{id}_1_unpaired.fastq"
        out_p2 = f"{output_dir}/{id}_2_paired.fastq"
        out_up2 = f"{output_dir}/{id}_2_unpaired.fastq"

        # Run Trimmomatic command
        trimmomatic_cmd = (
            f"java -jar {trimmomatic_jar} PE -phred33 {R1} {R2} "
            f"{out_p1} {out_up1} {out_p2} {out_up2} "
            f"ILLUMINACLIP:{adapter_file}:2:30:10 "
            f"LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
        )
        os.system(trimmomatic_cmd)
    
    print("Trimming completed for all samples.")

# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    
    # List of Run IDs to process
    id_list = [
        "ERR1468425",
        "ERR1468426",
        "ERR1468428",
        "ERR1468597",
        "ERR1468598",
        "ERR1468599",
        "ERR1468600",
    ]
    
    # Define input and output directories
    my_input_dir = "./raw_data"
    my_output_dir = "./trimmed_data"
    
    # Define paths to Trimmomatic jar and adapter file
    trimmomatic_jar = "./tools/trimmomatic-0.39.jar"
    adapter_file = "./tools/TruSeq3-PE.fa"

    # Run the trimming function
    run_trimmomatic(id_list=id_list, input_dir=my_input_dir, output_dir=my_output_dir, 
                    trimmomatic_jar=trimmomatic_jar, adapter_file=adapter_file)
