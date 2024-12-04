import pandas as pd
import streamlit as st


def checker(dna_sequence: str) -> bool:
    # Checks if the dna_sequence is a valid sequence, i.e. only contains adenine (A), cytosine (C), guanine (G), and thymine (T).
    dna = ''
    for i in dna_sequence:
        if i not in ['A', 'C', 'G', 'T']:
            dna += i
    return len(dna) == 0


def seq_to_dict(dna_sequence: str) -> dict:
    # Convert the dna_sequence into a dictionary
    dna_dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in dna_sequence:
        dna_dic[i] += 1
    return dna_dic


def main():
    # Renders the page heading and subheading for the web application
    st.write('''
    # DNA Nucleotide Analyzer
    Counts the nucleotide compotion of am inputted DNA query
    ''')


    # Input section for the web application
    temp_text = 'GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG'
    dna_sequence = st.text_area('Enter DNA Sequence', temp_text, height = 68)
    dna_sequence = dna_sequence.replace(' ', '').upper()

    
    # Input for the numbers of nucletoides to be used in the positional analysis
    n = st.slider('Group size of nucleotides for positional analysis', min_value = 2, max_value = 12)


    # Validates if the received sequence is a usuable DNA sequence and triggers the Output based on it
    flag = True

    if len(dna_sequence) == 0 or checker(dna_sequence) == False:
        st.markdown('**Error: Invalid Sequence Received (Issue with lenght or content)**')
        flag = False
    else:
        st.markdown('Recevied Sequence: ' + dna_sequence)

    
    # Renders the output chart
    if flag == True:
        st.markdown('***')
        st.markdown('### DNA Analysis')


        st.markdown('###### Nucleotide Count')
        dna_dic = seq_to_dict(dna_sequence)
        st.bar_chart(dna_dic, x_label = 'Nucleotides', y_label = 'Count')


        st.markdown('###### Nucleotide Positional %')
        st.markdown('_Note: In case the provide sequence cannot be bifurcated into equal parts the last part will be dropped_')
        positional_seq = [dna_sequence[i:i+n] for i in range(0, len(dna_sequence) - len(dna_sequence) % n, n)]
        df = pd.DataFrame({'Col': positional_seq})
        df = df.Col.str.split('', n = n, expand = True).drop(0, axis = 1)
        df = df.apply(pd.Series.value_counts)
        df = df.apply(lambda x: (x/x.sum())*100).round(2).fillna(0)
        st.write(df)


if __name__ == '__main__':
    main()
