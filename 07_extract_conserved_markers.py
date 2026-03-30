import os
from Bio import SeqIO

def extract_candidate_markers(ref_fasta, blast_dir, output_fasta):
    """
    Extracts candidate marker sequences from a reference FASTA file based on BLAST tabular results.
    Only sequences that have hits in all BLAST result files will be retained as candidates.
    Requires Biopython to be installed in the Python environment.
    """

    print("\nStarting candidate marker extraction...")

    # 1. Load reference sequences into a dictionary for easy access
    print(f"Loading reference FASTA:{ref_fasta}...")
    ref_records = SeqIO.to_dict(SeqIO.parse(ref_fasta, "fasta"))

    
    # 2. Initialize a set of candidate IDs with all reference IDs
    candidates = set(ref_records.keys())
    print(f"Total starting contigs: {len(candidates)}")

    # 3. Find all BLAST result files (both .txt and .tsv)
    blast_files = [f for f in os.listdir(blast_dir) if f.endswith((".txt", ".tsv"))]
    
    if not blast_files:
        print("No BLAST result files found in the specified directory. Exiting.")
        return
    
    print(f"Processing {len(blast_files)} BLAST result files...")
    
    # 4. For each BLAST result file, extract the IDs of the reference sequences that had hits and intersect them with our candidate set.
    for b in blast_files:
        path = os.path.join(blast_dir, b)
        print(f"Checking against {b} for candidate markers...")
        
        ids_in_sample = set()
        
        with open(path, "r") as f:
            for line in f:
                cols = line.strip().split("\t")
                if len(cols) > 1:
                    # Assuming the second column (index 1) contains the reference sequence ID that had a hit
                    ids_in_sample.add(cols[1])
        
        # Keep only those candidates that had hits in this sample (intersection)
        before_count = len(candidates)
        candidates.intersection_update(ids_in_sample)
        after_count = len(candidates)
        print(f"Candidates reduced from {before_count} to {after_count}")
        
    print("\n" + "=" * 40)
    print(f"RESULT: Found {len(candidates)} conservative markers across all assemblies.")
    print("\n" + "=" * 40 + "\n")
    
    # 5. Save the results to an output FASTA file
    if candidates:
        # Create output direcotry if it doesn't exist
        out_dit = os.path.dirname(output_fasta)
        if out_dit and not os.path.exists(out_dit):
            os.makedirs(out_dit)
            
        print(f"Saving candidate markers to {output_fasta}...")
        
        with open(output_fasta, "w") as out_f:
            count = 0
            for cid in candidates:
                SeqIO.write(ref_records[cid], out_f, "fasta")
                count += 1
                
        print(f"Saved {count} candidate marker sequences to {output_fasta}.")
    else:
        print("No candidate markers found that had hits in all samples. No output file created.")

# ==================
# USER CONFIGURATION
# ==================

if __name__ == "__main__":
    
    # Define the path to the reference FASTA file containing all contigs
    my_ref_fasta = ".BLAST/reference.fasta"
    
    # Define the directory containing the BLAST result files (either .txt and .tsv)
    my_blast_dir = ".BLAST/blast_results"
    
    # Define the output FASTA file to save the candidate marker sequences
    my_output_fasta = "./candidate_markers/candidate_markers.fasta"
    
    # Run the candidate marker extraction function
    extract_candidate_markers(ref_fasta=my_ref_fasta, blast_dir=my_blast_dir, output_fasta=my_output_fasta)
