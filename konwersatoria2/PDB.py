
import re, os.path


class PDBFile():

    def __init__(self):
        self.data = None

    def read(self, filename):
        with open (filename, 'r') as pdbfiletoread:
            self.data = pdbfiletoread.read()
        return self.data
    
    def getSequence(self, chain='A'):
        pattern = re.compile('^SEQRES([ \d]+) ([A-Z])([ \d]+)(.+)$',re.M)
        matches = pattern.findall(self.data)
        seq = ''
        for match in matches:
            seq += match[-1].rstrip()
       
        return seq

    def getAtoms(self, chain='A'):
        pattern = re.compile(r'^ATOM\s+(\d+)\s+(\w{1,4})\s+(\w{1,3})\s+(\w)\s.+$')
        # pattern = re.compile(f'^ATOM([ \d]+).+({chain}).+$',re.M)
        matches = pattern.findall(self.data)
        atoms = ''
        for match in matches:
            atoms += match
        print(matches)
        return matches

if __name__ == '__main__':
    pfh = PDBFile()
    pfh.read(r'c:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\4boe.pdb')
    seq = pfh.getSequence()
    print(seq[:5], seq[:5], len(seq))
    pfh.getAtoms()




#filename = r'c:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\4boe.pdb'
#MOJEPDB = PDBParser(filename)