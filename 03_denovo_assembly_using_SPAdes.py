import os

def run_spades_assembly(id_list,input_dir, output_dir, threads, memory):
    """
    Performs de novo genome assembly using SPAdes in --only-assembler mode.
    Requires SPAdes (spades.py) to be installed and accessible in the system PATH.
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Loop through each dataset and run SPAdes assembly
    for id in id_list:
        print(f"Processing sample: {id}")

        # Define input file paths
        r1 = f"{input_dir}/{id}_1_paired.fastq"
        r2 = f"{input_dir}/{id}_2_paired.fastq"

        # Define output directory for SPAdes assemblies
        output_SPAdes = f"{output_dir}/{id}_spades"

        # Construct and run SPAdes assembly command in only-assembler mode
        SPAdes_cmd = (
            f"spades.py --only-assembler --phred-offset 33 "
            f"-1 {r1} -2 {r2} -o {output_SPAdes} "
            f"-t {threads} -m {memory}"
            )
        os.system(SPAdes_cmd)

    print("\nSPAdes assembly completed for all datasets.")
    
# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    
    # List of Run IDs to assemble
    my_id_list = [
        "ERR1468425",
        "ERR1468426",
        "ERR1468428",
        "ERR1468597",
        "ERR1468598",
        "ERR1468599",
        "ERR1468600",
    ]

    # Define input and output directories
    # Update these paths to where your trimmed fastq files are located and where you want the SPAdes assemblies to be saved
    my_input_dir = "./trimmed_data"
    my_output_dir = "./assembled_data"

    # Hardware settings for SPAdes assembly
    my_threads = 8
    my_memory = 20 # in GB
    
    # Run the SPAdes assembly function
    run_spades_assembly(id_list=my_id_list, input_dir=my_input_dir, output_dir=my_output_dir, threads=my_threads, memory=my_memory)
