AF-DEAnalysis
=====
This is a Python script that takes an input directory of raw RNA read sample files froma dataset of two populations of S. cerevisiae, WT and snf2 knock-down, mapping them by aligning them to an annotated genome. 

Programs
=====
* FastQC
* CutAdapt
* Fastq Quality Trimmer
* STAR aligner
  
Function 
=====
By giving the script an input directory with the sample FASTQ files to be aligned, this script will perform the following actions on each sample file: 
1. Print out the name of the sample file that it is currently working on. 
2. Run FastQC to check the intial quality of the file, and give an output of an intial FastQC report html. 
3. Run CutAdapt to cut the given adapter sequence "AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT" from each read in the sample, giving an output file of "filename_cao.fastq" 
4. Run Fastq Quality Trimmer on the CutAdapt output file to trim poor quality reads, giving an output of output file of "filename_fqto.fastq"
5. Run FastQC on the Fastq Quality Trimmer output file to check the cleaned file's quality, giving an ouput of a final FastQC report html.

Once all samples files in the directory have undergone trimming, they will be mapped to the given annotated genome using STAR and give an output BAM file.

Future Implementations
======================
In the future, this script will be added on to be able to:
* Seperate the reads by type, WT and snf2, using a manifest
* Quantify reads by performing gene based counting
* Normalize reads
* Do a DE expression test

 
