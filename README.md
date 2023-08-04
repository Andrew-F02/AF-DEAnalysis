AF-FastQAligner
===========================================
Function 

This is a script that takes an input directory of raw RNA read sample files, 
in the form of FASTA or FASTQ, and aligns them to an annotated genome. 
Give it an input Directory with the FASTQ files you want to be aligned, it will first print out the name of the read file that it is currently working on. 
Then, it will run FastQC to check the intial quality of the file. 
Next, it will run CutAdapt to trim a given adapter sequence from each read and Fastq Quality Trimmer to trim poor quality reads.
FastQC is run again to check the cleaned file's quality.
Once all files in the directory have undergone this, they will be mapped to the given annotated genome using STAR aligner.

=======================================================================================================

Programs:
   FasQC
   CutAdapt
   Fastq Quality Trimmer
   STAR aligner
 
