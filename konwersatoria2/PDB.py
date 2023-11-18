
import re, os.path


class PDBFile():

    def __init__(self):
        self.data = None
        self.chains = []
        self.number_of_atoms = None
        self.number_of_hetatm = None

    def read(self, filename):
        with open (filename, 'r') as pdbfiletoread:
            self.data = pdbfiletoread.read()
        return self.data
    
    def getSequence(self, lchain='A'):
        pattern = re.compile('^SEQRES[ \d{5}]+ ([A-Z ])[ \d]+(.+)$',re.M)
        matches = pattern.findall(self.data)
        seq = ''
        for match in matches:
            if lchain == 'ALL':
                seq += match[-1].rstrip()
                seq += ' '
            else:
                if match[0] == lchain:
                    seq += match[-1].rstrip()
            if match[0] not in self.chains:
                self.chains.append(lchain)
        return seq

    def getAtoms(self, chain='A'):
        pattern = re.compile(f'^ATOM[ \d]+\w+\s+\w+\s+{chain}[- \.\d]+([A-Z])+.*$',re.M)
        matches = pattern.findall(self.data)
        atoms = ''
        for match in matches:
            atoms += match[0]
        self.number_of_atoms = len(atoms)
        return atoms

def writefasta(pdbfile, fastapath):
        amino_acid_codes = {
    'ALA': 'A',
    'ARG': 'R',
    'ASN': 'N',
    'ASP': 'D',
    'CYS': 'C',
    'GLN': 'Q',
    'GLU': 'E',
    'GLY': 'G',
    'HIS': 'H',
    'ILE': 'I',
    'LEU': 'L',
    'LYS': 'K',
    'MET': 'M',
    'PHE': 'F',
    'PRO': 'P',
    'SER': 'S',
    'THR': 'T',
    'TRP': 'W',
    'TYR': 'Y',
    'VAL': 'V'
}
        seq = pdbfile.getSequence('ALL')
        with open (fastapath, 'w') as fastaf:
            fastaf.write(f'<{pdbfile} sequence\n')
            how_long = 0
            for aa in seq.split():
                fastaf.write(amino_acid_codes[aa])
                how_long += 1
                if how_long%60 == 0:
                    fastaf.write('\n')

def nonpolymeric_molecules(pdbfile):
    number_of_np = 0
    names_of_np = []
    formula_of_np = []
    pattern = re.compile('^HETATM[\d ]+[A-Z0-9]+[\s]+([A-Z]+).+$', re.M)
    matches = pattern.findall(pdbfile.data)
    for match in matches:
        names_of_np.append(match)
    pattern = re.compile('^FORMUL[\d ]+([A-Z]+)[\s\*]+(.*)$', re.M)
    matches = pattern.findall(pdbfile.data)
    for match in matches:
        match = list(match)
        match[1] = match[1].strip()
        formula_of_np.append(match)
    number_of_np = len(names_of_np)
    return f'Number of non-polymeric molecules:{number_of_np}.\n\nNames of non polymeric molecules:\n{names_of_np}\n\nFormulas of non-polymeric molecules:\n{formula_of_np}'

          




        





if __name__ == '__main__':
    pfh = PDBFile()
    folder = os.path.abspath(os.path.dirname(__file__))
    pdbfilename = "4boe.pdb"
    pathtopdb = os.path.join(folder, pdbfilename)
    fastafilename = "mojafasta.fasta"
    pathtofasta = os.path.join(folder, fastafilename)
    pfh.read(pathtopdb)
    writefasta(pfh, pathtofasta)
    seq = pfh.getSequence()
    pfh.getAtoms()
    print(f'Number of polypeptide chains: {len(pfh.chains)}')
    print(f'Number of atoms: {pfh.number_of_atoms}')
    #print(seq[:5], seq[:5], len(seq))
    print(nonpolymeric_molecules(pfh))




#filename = r'c:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\4boe.pdb'
#MOJEPDB = PDBParser(filename)

#^ATOM\s+\d+\s+\w+\s+\w+\s+A\s+\-?\d+\s+\d+\.\d+\s+\-?\d+\.\d+\s+\-?\d+\.\d+\s+\-?\d+\.\d+\s+\d+\.\d+\s+\w+\s*$
