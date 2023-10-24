def nn_to_aa(nucleotides):
    rna_codon_table = {
            "UUU": "Phe",
            "UUC": "Phe",
            "UUA": "Leu",
            "UUG": "Leu",
            "CUU": "Leu",
            "CUC": "Leu",
            "CUA": "Leu",
            "CUG": "Leu",
            "AUU": "Ile",
            "AUC": "Ile",
            "AUA": "Ile",
            "AUG": "Met",
            "GUU": "Val",
            "GUC": "Val",
            "GUA": "Val",
            "GUG": "Val",
            "UCU": "Ser",
            "UCC": "Ser",
            "UCA": "Ser",
            "UCG": "Ser",
            "CCU": "Pro",
            "CCC": "Pro",
            "CCA": "Pro",
            "CCG": "Pro",
            "ACU": "Thr",
            "ACC": "Thr",
            "ACA": "Thr",
            "ACG": "Thr",
            "GCU": "Ala",
            "GCC": "Ala",
            "GCA": "Ala",
            "GCG": "Ala",
            "UAU": "Tyr",
            "UAC": "Tyr",
            "UAA": "STOP",
            "UAG": "STOP",
            "CAU": "His",
            "CAC": "His",
            "CAA": "Gln",
            "CAG": "Gln",
            "AAU": "Asn",
            "AAC": "Asn",
            "AAA": "Lys",
            "AAG": "Lys",
            "GAU": "Asp",
            "GAC": "Asp",
            "GAA": "Glu",
            "GAG": "Glu",
            "UGU": "Cys",
            "UGC": "Cys",
            "UGA": "STOP",
            "UGG": "Trp",
            "CGU": "Arg",
            "CGC": "Arg",
            "CGA": "Arg",
            "CGG": "Arg",
            "AGU": "Ser",
            "AGC": "Ser",
            "AGA": "Arg",
            "AGG": "Arg",
            "GGU": "Gly",
            "GGC": "Gly",
            "GGA": "Gly",
            "GGG": "Gly"
        }
    
    tri = nucleotides[0:3]
    tri = tri.upper()
    return rna_codon_table[tri]



print(nn_to_aa('uUg'))


def rna_to_protein_dependent(nucleotides):
    protein = ""
    if (len(nucleotides)%3 != 0):
        protein = protein + "Podałeś niepodzielną przez 3 liczbę nukleotydów, nie wszystkie zostały wzięte pod uwagę przy zamianie na aminokwasy. Twoja sekwencja: \n"
    for i in range(0,len(nucleotides),3):
        tri = nukleotydy[i:(i+3)]
        protein = protein + nn_to_aa(tri) + " "
    return protein



def rna_to_protein(nucleotides):
    protein = ""
    rna_codon_table = {
            "UUU": "Phe",
            "UUC": "Phe",
            "UUA": "Leu",
            "UUG": "Leu",
            "CUU": "Leu",
            "CUC": "Leu",
            "CUA": "Leu",
            "CUG": "Leu",
            "AUU": "Ile",
            "AUC": "Ile",
            "AUA": "Ile",
            "AUG": "Met",
            "GUU": "Val",
            "GUC": "Val",
            "GUA": "Val",
            "GUG": "Val",
            "UCU": "Ser",
            "UCC": "Ser",
            "UCA": "Ser",
            "UCG": "Ser",
            "CCU": "Pro",
            "CCC": "Pro",
            "CCA": "Pro",
            "CCG": "Pro",
            "ACU": "Thr",
            "ACC": "Thr",
            "ACA": "Thr",
            "ACG": "Thr",
            "GCU": "Ala",
            "GCC": "Ala",
            "GCA": "Ala",
            "GCG": "Ala",
            "UAU": "Tyr",
            "UAC": "Tyr",
            "UAA": "STOP",
            "UAG": "STOP",
            "CAU": "His",
            "CAC": "His",
            "CAA": "Gln",
            "CAG": "Gln",
            "AAU": "Asn",
            "AAC": "Asn",
            "AAA": "Lys",
            "AAG": "Lys",
            "GAU": "Asp",
            "GAC": "Asp",
            "GAA": "Glu",
            "GAG": "Glu",
            "UGU": "Cys",
            "UGC": "Cys",
            "UGA": "STOP",
            "UGG": "Trp",
            "CGU": "Arg",
            "CGC": "Arg",
            "CGA": "Arg",
            "CGG": "Arg",
            "AGU": "Ser",
            "AGC": "Ser",
            "AGA": "Arg",
            "AGG": "Arg",
            "GGU": "Gly",
            "GGC": "Gly",
            "GGA": "Gly",
            "GGG": "Gly"
        }
    if (len(nucleotides)%3 != 0):
        protein = protein + "Podałeś niepodzielną przez 3 liczbę nukleotydów, nie wszystkie zostały wzięte pod uwagę przy zamianie na aminokwasy. Twoja sekwencja: \n"
    for i in range(0,len(nucleotides),3):
        tri = nukleotydy[i:(i+3)]
        protein = protein + rna_codon_table[tri] + " "
    return protein
        






