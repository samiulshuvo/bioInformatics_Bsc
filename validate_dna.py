## my first bioinformatics program
def validate_DNA(seq):
    useq=seq.upper()
    lenSeq=len(seq)
    validLen=useq.count("A")+useq.count("C")+useq.count("G")+useq.count("T")
    if lenSeq==validLen:
        print("the DNA is valid")
    else:
        print("It is not a valid DNA sequence")
DNA=input('please provide the sequence:')
validate_DNA(DNA)
