#################################
# Import libraries (biblioteka)
#################################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Naslov stranice
######################

image = Image.open('DNA.jpg')

st.image(image, use_column_width=True)

st.write("""
# Ova aplikacija broji nukleotidni sastav DNK upita!
                APP by Josip Požega
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Unesite DNK sekvencu ')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Unos sekvence ", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Preskače naziv sekvence (prvi redak)
sequence = ''.join(sequence) # Povezuje popis u niz

st.write("""
***
""")

## Ispisuje ulaznu sekvencu DNK
st.header('INPUT (DNA upit)')
sequence

## Broj DNK nukleotida
st.header('OUTPUT (Broj nukleotida DNK )')

### 1. Ispis rječnika
st.subheader('1. Ispis rječnika ')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 2. Print text
st.subheader('2. Print text')
st.write('Tamo su  ' + str(X['A']) + ' adenina (A)\nspoj koji je jedna od četiri sastavne baze nukleinskih kiselina.\n Derivat purina, uparen je s timinom u dvolančanoj DNK. ')
st.write('Tamo su  ' + str(X['T']) + ' timina (T)\nspoj koji je jedna od četiri sastavne baze nukleinskih kiselina.\n Derivat pirimidina, uparen je s adeninom u dvolančanoj DNK.')
st.write('Tamo su  ' + str(X['G']) + ' gvanina (G)\nspoj koji se javlja u guanu i ribljim ljuskama, a jedan je od četiri sastavne baze nukleinskih kiselina.\n Derivat purina, uparen je s citozinom u dvolančanoj DNK.')
st.write('Tamo su ' + str(X['C']) + ' citozina\nspoj koji se nalazi u živom tkivu kao sastavna baza nukleinskih kiselina.\n Uparen je s gvaninom u dvolančanoj DNK. (C)')

### 3. Display DataFrame
st.subheader('3. Prikaz okvira podataka ')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nukleotida'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Prikaz trakastog grafikona ')
p = alt.Chart(df).mark_bar().encode(
    x='nukleotida',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
