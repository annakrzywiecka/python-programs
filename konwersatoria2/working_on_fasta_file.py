def fasta_file_analysys(filename):
    ''' Napisać program, który wczyta zawartość tego pliku i zachowa go w postaci słownika, gdzie kluczem będzie nazwa sekwencji (pierwszy ciąg znaków bez spacji po znaku >) a wartością sama sekwencja aminokwasowa reprezentowana przez jednoliterowe wielkie litery (zachowując sekwencje użytkownik powinien mieć możliwość wyboru czy zachowuje sekwencje ze znakami przerw czy te znaki powinny być usuwane). Następnie dla jednej z wczytanych sekwencji (tj. sekwencja bez przerw) zostanie wyznaczony średni skład aminokwasowy (tj. względny odsetek reszt aminokwasowych jednego typu). Wyniki obliczeń powinny być wydrukowane dla wszystkich 20 rodzajów aminokwasów tworzących białka syntetyzowane rybosomalnie.'''
    decision = input("If you want to keep the hyphens standing for the breaks, write T, if you want to omit them, write F: ")
    if decision not in ['F', 'T']:
        return fasta_file_analysys(filename)
    chosenind = input("Enter the sequence for which you want to obtain the percentage distribution of individual aminoacids: ")
    with open(filename, 'r') as file:
        indexes = []
        sequences = []
        seq = ''
        for fasta_line in file:
            if fasta_line.startswith('>'):
                indexes.append(fasta_line[1:].strip('\n '))
                if seq != '':
                    sequences.append(seq)
                    seq = ''   
            else:
                fasta_line = fasta_line.replace('\n','')
                if decision == 'F':
                    fasta_line = fasta_line.replace('-','')
                seq = seq + fasta_line
    if seq != '':
        sequences.append(seq)
        seq =''
    my_dict = {ind: s for ind, s in zip(indexes, sequences)}
    while chosenind not in list(my_dict.keys()):
        chosenind = input("Enter the sequence for which you want to obtain the percentage distribution of individual aminoacids: ")
    chosenseq = my_dict[chosenind]
    if decision == 'T':
        chosenseq = chosenseq.replace('-','') 
    dict_of_perc = {ind: 0 for ind in 'ACDEFGHIKLMNPQRSTVWY'}
    dict_of_perc.update({ind: s for ind, s in zip(set(chosenseq), [(chosenseq.count(letter)/len(chosenseq))*100 for letter in set(chosenseq)])})
    
    return dict_of_perc

   
filename =  r'c:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\PF00061-seed.fasta'
dicc = fasta_file_analysys(filename)
   
    
print(dicc)

