import os

def run_local_blastn(id_list, query_dir, ref_fasta, db_output,  output_dir, perc_identity = 90):
    
    """
    Creates a local BLAST database from the best reference assembly 
    and runs BLASTn for each query FASTA file against the created database.
    Requires NCBI BLAST+ command line tools to be installed and accessible in the system PATH.
    """

    # Create output directory for database and results if they don't exist
    db_dir = os.path.dirname(db_output)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print(f"Created output directory: {db_dir}")
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
        
    # =====================
    # Create BLAST database
    # =====================

    print(f"\nCreating BLAST database from: {ref_fasta}...")
    cmd_ref_db = f"makeblastdb -in {ref_fasta} -dbtype nucl -out    {db_output}"
    os.system(cmd_ref_db)

    # ==================================================
    # Run BLASTn for each assembly against the reference 
    # ==================================================
    
    for id in id_list:
        print(f"\nRunning BLASTn for: {id}...")
        
        # Define the path to the query FASTA file.
        # NOTE: I renamed the query contigs from {id}_megahit_output/final.contigs.fa 
        # and {id}_spades/contigs.fasta to {id}_contigs.fasta for simplicity.
        query_path = f"{query_dir}/{id}_contigs.fasta"

        # Define the output path for the BLAST results.
        output_path = f"{output_dir}/{id}_blast.tsv"

        cmd_blast = (
            f"blastn -query {query_path} -db {db_output} "
            f"-out {output_path} -outfmt 6 -perc_identity {perc_identity}"
        )
        
        os.system(cmd_blast)

    print("\nBLASTn analysis completed.")

# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    
    # List of queries to process (without the one that was used as the reference (ERR1468425))
    my_id_list = [
        "ERR1468426",
        "ERR1468428",
        "ERR1468597",
        "ERR1468598",
        "ERR1468599",
        "ERR1468600",
    ]

    # Define paths
    my_ref_fasta = "./BLAST/reference.fasta"
    my_db_output = "./BLAST/blast_db/ref_db"
    my_query_dir = "./BLAST/queries"
    my_output_dir = "./BLAST/blast_results"
    
    my_perc_identity = 90 # minimum percentage identity for BLASTn hits
    
    # Run the local BLASTn function
    run_local_blastn(id_list=my_id_list, query_dir=my_query_dir, ref_fasta=my_ref_fasta, db_output=my_db_output,
                     output_dir=my_output_dir, perc_identity=my_perc_identity)
