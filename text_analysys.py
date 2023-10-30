
def statystyka_slowa(portion):
    '''Program, który wyświetli liczbę zdań, liczbę słów, najdłuższe słowo, najczęściej występujące słowo o długości co najmniej 5 znaków.'''
    number_of_sentences = portion.count('.')    
    table_of_words = portion.split()
    table_of_words = [word.strip('.,:;(){}[]') for word in table_of_words ]
    #print(table_of_words)
    number_of_words = len(table_of_words)
    max_word = max(table_of_words, key=len)
    table_of_counts = [table_of_words.count(word) for word in table_of_words if table_of_words.count(word) if len(word) >= 5]
    popular_word = [word for word in table_of_words if max(table_of_counts) == table_of_words.count(word) and len(word) >= 5]
    popular_wordt = set(popular_word)

    print(popular_word)
    answer = "W danym tekście jest " + str(number_of_sentences) + " zdan, " + str(number_of_words) + " slow. Najczesciej wystepujace slowo to " + ', '. join(popular_wordt) + ". Najdluzsze slowo to " + max_word
    print(answer)
    return number_of_sentences














abstract = "Phospholipid membranes support essential biochemical processes, yet remain difficult to characterize due to their compositional and structural heterogeneity. The two most common phospholipid headgroup structures in biological membranes are phosphatidylcholine (PC) and phosphatidylethanolamine (PE), but interactions between PC and PE lipids remain underexplored. In this study, we apply ultrafast two-dimensional infrared (2D IR) spectroscopy to quantify the headgroup effects on interfacial dynamics in PC/PE lipid mixtures. Experiments are interpreted through molecular dynamics simulations using the molecular dynamics with alchemical step (MDAS) algorithm for enhanced sampling. Experimental results indicate that the PE content decreases H-bond formation at the ester carbonyl positions near the lipid membrane's hydrophobic core as a result of increased packing density. The observed dehydration is linked to faster molecular dynamics within the interfacial region."
print(statystyka_slowa(abstract))