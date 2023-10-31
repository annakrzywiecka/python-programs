
def statystyka_slowa(portion):
    '''Program, który wyświetli liczbę zdań, liczbę słów, najdłuższe słowo, najczęściej występujące słowo o długości co najmniej 5 znaków.'''
    number_of_sentences = portion.count('.')    
    table_of_words = portion.split()
    table_of_words = [word.strip('.,:;(){}[]') for word in table_of_words]
    number_of_words = len(table_of_words)
    max_word = max(table_of_words, key=len)
    table_of_counts = [table_of_words.count(word) for word in table_of_words if table_of_words.count(word) if len(word) >= 5]
    popular_word = [word for word in table_of_words if max(table_of_counts) == table_of_words.count(word) and len(word) >= 5]
    popular_wordt = set(popular_word)
    answer = "W danym tekście jest " + str(number_of_sentences) + " zdan, " + str(number_of_words) + " slow. Najczesciej wystepujace slowo to " + ', '. join(popular_wordt) + ". Najdluzsze slowo to " + max_word + '.'
    return answer



def separate_text(abstr):
    """Program, który wyświetli zawartość abstract w taki sposób, że każdy wiersz będzie zawierał dokładnie 55 znaków, poszczególne słowa nie będą dzielone, każdy wiersz będzie wyrównany do prawej strony"""
    output_text = ""
    table_of_words = abstr.split()
    while(len(table_of_words) > 0):
        sum_of_signs = 0
        ind = 0
        while sum_of_signs <= 56 and len(table_of_words) > ind:           #dlatego 56, bo dodaję w pętli jeden jako spację rozdzielającą, która na końcu linijka nie jest potrzebna
            sum_of_signs = sum_of_signs + len(table_of_words[ind]) + 1
            ind = ind + 1
               
        if sum_of_signs <= 56:
            new_line = [table_of_words[i] for i in range(ind) ]
            table_of_words = table_of_words[ind:]
        else:
            new_line = [table_of_words[i] for i in range(ind-1)]
            table_of_words = table_of_words[ind-1:]

        new_line = (' ').join(new_line)
        difference_in_length = 55 - len(new_line)
        new_line = difference_in_length*(" ") + new_line + '\n'
        output_text = output_text + new_line

    return output_text





def reversing_words(abstract):
    """Program, który wyświetli abstract w taki sposób, że każde słowo w kolejnych zdaniach będzie zapisane wspak"""
    text = abstract[:]
    i = 0
    while i < len(text):
        if text[i] in [",",".",":",";","/","(",")"]:
            text = text[:i] + " " + text[i] + " " + text[i+1:]
            i += 1
        i += 1

    output_text = " ".join([word[::-1] for word in text.split()])

    i = 0
    while i < len(output_text):                                    #usuwanie spacji
        if output_text[i] in [",",".",":",";","/","(",")"]:
            output_text = output_text[:i-1] + output_text[i:]
            i -= 1
        i += 1


    output_text = separate_text(output_text)

    return output_text

def statistics_of_text(abstract):
    """Program, który dla każdego zdania w abstract wygeneruje sekwencje długości kolejnych słów, wyświetli ją w jednym wierszu a na koniec policzy średnią długość słowa w analizowanym zdaniu."""
    text = abstract[:]
    i=0
    output_stat=""
    while i < len(text):
        if text[i] in [",",":",";","/","(",")"]:
            text = text[:i] + text[i+1:]
            i += 1
        i += 1
    list_of_words = [sentence.split() for sentence in text.split(".")]
    for i in range (len(list_of_words)):
        list_of_lengths = [len(word) for word in list_of_words[i]]
        if len(list_of_lengths)>0:
            mean_of_lengths = round(sum(list_of_lengths)/len(list_of_lengths),4)
            list_of_lengths = [str(length) for length in list_of_lengths]
            output_stat = output_stat + ", ".join(list_of_lengths) + " srednia: " + str(mean_of_lengths)+ '\n'
    return output_stat













abstract = "Phospholipid membranes support essential biochemical processes, yet remain difficult to characterize due to their compositional and structural heterogeneity. The two most common phospholipid headgroup structures in biological membranes are phosphatidylcholine (PC) and phosphatidylethanolamine (PE), but interactions between PC and PE lipids remain underexplored. In this study, we apply ultrafast two-dimensional infrared (2D IR) spectroscopy to quantify the headgroup effects on interfacial dynamics in PC/PE lipid mixtures. Experiments are interpreted through molecular dynamics simulations using the molecular dynamics with alchemical step (MDAS) algorithm for enhanced sampling. Experimental results indicate that the PE content decreases H-bond formation at the ester carbonyl positions near the lipid membrane's hydrophobic core as a result of increased packing density. The observed dehydration is linked to faster molecular dynamics within the interfacial region."
print(statystyka_slowa(abstract))
print(separate_text(abstract))
print(reversing_words(abstract))
print(statistics_of_text(abstract))
