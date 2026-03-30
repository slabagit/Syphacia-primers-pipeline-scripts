# Syphacia-primers-pipeline

This pipeline is designed for the automated identification of conserved genomic markers in parasitic nematode Syphacia obvelata. The goal is to find suitable target regions for specific PCR primer design.

# Workflow Overview

The pipeline consists of seven sequential Python scripts:

1. 01_download_sra_using_fastq-dump.py**: Fetches raw sequencing data from the NCBI SRA database.
2. 02_trimming_reads_using_Trimmomatic.py**: Performs quality control and removes adapters/low-quality bases.
3. 03_denovo_assembly_using_SPADes.py**: Performs *de novo* genome assembly (ideal for smaller datasets).
4. 04_denovo_assembly_using_megahit.py**: Alternative assembly using MEGAHIT (executed via Docker container).
5. 05a/b_assembly_qc_using_quast.py**: Evaluates the quality of assembled contigs (N50, total length, etc.).
6. 06_local_blastn_analysis.py**: Creates a local database from a reference assembly and maps other assemblies against it.
7. 07_extract_conserved_markers.py**: Identifies sequences present across all samples (consensus markers).

# Requirements

To run this pipeline, ensure the following tools are installed and accessible in your system PATH:
* Python 3.x (with `biopython` library)
* SRA Toolkit
* Trimmomatic
* SPAdes
* Docker (required for the MEGAHIT script)
* QUAST
* NCBI BLAST+

# Usage

Scripts are designed to be executed in numerical order. Hardware settings (threads, memory) and file paths can be adjusted within the `USER CONFIGURATION` section at the end of each script.
