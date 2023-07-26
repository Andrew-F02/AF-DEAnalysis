import sys, getopt, os, subprocess

options = "hm:"
long_options = ["Help", "My_file"]

argumentList = sys.argv[1:]

try:

     for argument in argumentList:
        if argument in ("-h", "--Help"):
            print("Displaying Help")

        elif argument in ("-m", "--My_file"):
            print("Displaying file_name:", sys.argv[2])

except getopt.error as err:
    print(str(err))

SampleData = sys.argv[1]
for read in os.listdir(SampleData):
    SampleName = read.split(".fastq.gz")
    print(SampleName)

fastqc = "fastqc " + SampleData + "/" + read + " -o " + "/space/s2/andrew/scripts/script_output"
os.system(fastqc)

cutadapt_output_file = SampleName + list("_ca.fastq.gz")
cutadapt = "cutadapt -a AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT -o " + cutadapt_output_file + SampleData

fastq_qualitytrimmer_output = SampleName + "fqto.fastq"
fastq_quality_trimmer = "/home/lenore//bin/fastq_quality_trimmer -v" + " -t " + "20" + " -l " + "20" + " -i " + " -z " + cutadapt_output_file + " -o " + fastq_qualitytrimmer_output

fastqc_quality_trimmer = "fastqc /space/s2/andrew/scripts/" + fastq_qualitytrimmer_output  + " -o " + "/space/s2/andrew/scripts/script_output"

runSTAR = "/space/s2/andrew/software/STAR-2.7.10b/bin/Linux_x86_64_static/STAR"
REF_SEQ = "/space/s2/andrew/yeast_genome"

FILES = "ls -m /space/s2/andrew/scripts/fastq_qualitytrimmer_output/*fastq | sed 's/ //g'"
FILE = " echo " + FILES + " | sed 's/ //g'"
runSTARprocess = runSTAR + " --genomeDir " + REF_SEQ + "/STARindex/ --readFilesIn " + FILES + " --outFileNamePrefix aligned_sample --outFilterMultimapNmax 1 --outReadsUnmapped Fastx --outSAMtype BAM SortedByCoordinate --twopassMode Basic --runThreadN 1"
os.system(runSTARprocess)

