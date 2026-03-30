import os

def run_quast(id_list, input_dir, output_dir, threads, min_contig_len):
    
    """
    Runs QUAST (Quality Assessment Tool for Genome Assemblies) on SPAdes output.
    Requires QUAST to be installed and accessible in the system PATH.
    """
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Loop through each assembly and run QUAST on the SPAdes contigs
    for id in id_list:
        print(f"Running QUAST for sample: {id}")
        
        # Define input and output paths for QUAST (assuming SPAdes contigs structure: {sample}_spades/contigs.fasta)
        input_path = f"{input_dir}/{id}_spades/contigs.fasta"
        output_path = f"{output_dir}/{id}_quast"

        quast_cmd = (
            f"quast.py {input_path} -o {output_path} -t {threads} -m {min_contig_len}"
        )
        
        os.system(quast_cmd)
    
    print("\nQUAST analysis completed for all assemblies.")
    
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
    
    # Define input and output directories
    # Input directory should be the output directory from the SPAdes assembly step
    my_input_dir = "./assembled_data"
    my_output_dir = "./quast_results"
    
    # Hardware settings for QUAST analysis
    my_threads = 8
    my_min_contig_len = 500 # in bp
    
    # Run the QUAST analysis function
    run_quast(id_list=my_id_list, input_dir=my_input_dir, output_dir=my_output_dir,
              threads=my_threads, min_contig_len=my_min_contig_len)
