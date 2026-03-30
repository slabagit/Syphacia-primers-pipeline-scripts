import os

def run_megahit_assembly(input_dir, output_dir, id_list, threads, min_contig_len):
    """
    Performs de novo genome assembly using MEGAHIT via Docker container.
    Requires Docker to be installed and running on the system.
    """

    # Docker requires absolute paths for volume mounting, so we convert the input and output directories to absolute paths
    abs_input_dir = os.path.abspath(input_dir)
    abs_output_dir = os.path.abspath(output_dir)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(abs_output_dir):
        os.makedirs(abs_output_dir)
        print(f"Created output directory: {abs_output_dir}")

    # Loop through each dataset and run the MEGAHIT assembly using Docker
    for id in id_list:
        print(f"Processing sample: {id}")

        # Construct the Docker command to run MEGAHIT
        # -v option is used to mount the input and output directories into the Docker container
        megahit_docker_cmd = (
            f"docker run --rm -v {abs_input_dir}:/data_in -v {abs_output_dir}:/data_out "
            f"biocontainers/megahit:1.2.9_cv1 "
            f"/opt/conda/bin/megahit "
            f"-1 /data_in/{id}_1_paired.fastq "
            f"-2 /data_in/{id}_2_paired.fastq "
            f"-o /data_out/{id}_megahit_output "
            f"--min-contig-len {min_contig_len} --num-cpu-threads {threads}"
        )

        os.system(megahit_docker_cmd)
    
    print("\nMEGAHIT assembly completed for all datasets.")
    
# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    
    # List of ids to process
    my_id_list = [
        "ERR1468425",
        "ERR1468426",
        "ERR1468428",
        "ERR1468597",
        "ERR1468598",
        "ERR1468599",
        "ERR1468600",  
    ]
    # Define input and output directories (relative paths will be converted to absolute paths in the function)
    my_input_dir = "./trimmed_data"
    my_output_dir = "./assembled_data"

    # Hardware settings for MEGAHIT assembly
    my_threads = 8
    my_min_contig_len = 200 # in bp
    
    # Run the MEGAHIT assembly function
    run_megahit_assembly(input_dir=my_input_dir, output_dir=my_output_dir, id_list=my_id_list,
                         threads=my_threads, min_contig_len=my_min_contig_len)
