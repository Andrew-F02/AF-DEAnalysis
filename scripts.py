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
Output_Dir = "/space/s2/andrew/Output_Dir/"
for read in os.listdir(SampleData):
    SampleName = read.split(".fastq.gz")
    FullName = str(SampleName).replace("[","").replace("]","").replace(",","").replace(" ","")
    print(*SampleName)
    fastqc = "fastqc " + SampleData + "/" + read + " -o " + "/space/s2/andrew/Output_Dir"
    os.system(fastqc)
    cutadapt_output_file = FullName + "_cao.fastq"
    cutadapt = "cutadapt -a AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGATCT" + " -o " +  Output_Dir + cutadapt_output_file + " " + SampleData + "/" + read
    os.system(cutadapt)
    fastq_qualitytrimmer_output = FullName + "_fqto.fastq"
    fastq_quality_trimmer = "/home/lenore/bin/fastq_quality_trimmer -v" + " -t " + "20" + " -l " + "20"  + " -i " + Output_Dir +  cutadapt_output_file + " -o " + Output_Dir + fastq_qualitytrimmer_output
    os.system(fastq_quality_trimmer)
    fastqc_quality_trimmer = "fastqc " + Output_Dir  + fastq_qualitytrimmer_output  + " -o " + "/space/s2/andrew/Output_Dir/CleanedFastq"
    os.system(fastqc_quality_trimmer)
else:
     runSTAR = "/space/s2/andrew/software/STAR-2.7.10b/bin/Linux_x86_64_static/STAR"
     REF_SEQ = "/space/s2/andrew/yeast_genome"
     Output = Output_Dir + "ERR458815_fqto.fastq," + Output_Dir + "ERR458816_fqto.fastq," + Output_Dir + "ERR458817_fqto.fastq," + Output_Dir + "ERR458818_fqto.fastq" 
     runSTARprocess = runSTAR + " --genomeDir " + REF_SEQ + "/STARindex/ --readFilesIn " + Output + " --outFileNamePrefix /space/s2/andrew/Output_Dir/CleanedFastq/alignedreads/aligned_read --outFilterMultimapNmax 1 --outReadsUnmapped Fastx --outSAMtype BAM SortedByCoordinate --twopassMode Basic --runThreadN 1"
     os.system(runSTARprocess)

