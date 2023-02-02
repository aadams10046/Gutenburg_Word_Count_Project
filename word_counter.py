#Importing appropriate packages
import pandas as pd
import re
import matplotlib.pyplot as plot
import seaborn as sns
import numpy as np

#function to read book, giving you the choice to return the the text with or without all punctuation and spaces
def book_reader(file, return_orig = False):
    with open(file, 'r') as current_book:
        text = current_book.read()
        text = text.replace('\n', ' ').replace('\r',' ')
        orig = text
    text = text.lower()
    text = re.sub(r'[0-9]',' ',text)
    text = re.sub(r'[^\w\s]',' ', text)
    cleaned = text
    if return_orig == True:
        return orig
    else:
        return cleaned

#Function to find the word count of the text
def word_count(text):
    text_split = text.split(' ')
    while('' in text_split):
        text_split.remove('')
    return len(text_split)

#Function to count unique word in the text and also to create dictionary to store them all
def unique_count(text, return_list = False):
    uniques = {}
    for word in text.lower().split(' '):
        if word in uniques:
            uniques[word] += 1
        else:
            uniques.update({word: 1})
#Below removes remaining empty entries in the unique word dictionary  
    uniques.pop('')
    if return_list == True:
        return uniques
    else:
        return len(list(uniques.keys()))

#Connecting the book files to the code
alcott = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Alcott_Little_Women.txt'
eliot = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Eliot_Middlemarch.txt'
forster = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Forster_A_Room_with_a_View.txt'
gaskell = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Gaskell_Cranford.txt'
smollett_clinker = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Smollett_The_Expedition_of_Humphry_Clinker.txt'
fielding = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Fielding_The_History_of_Tom_Jones.txt'
melville = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Melville_Moby_Dick.txt'
montgomery = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Montgomery_The_Blue_Castle.txt'
smollett_fathom = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Smollett_The_Adventures_of_Ferdinand_Count_Fathom .txt'
von_arnim = '/Users/alexanderadams/Desktop/Word_Count_Project/Books/Von_Arnim_The_Enchanted_April.txt'

#Generating a dataframe for the whole library above
data = np.array([['Louisa May Alcott', 'Little Women', word_count(book_reader(alcott)), unique_count(book_reader(alcott))], 
['George Eliot', 'Middemarch', word_count(book_reader(eliot)), unique_count(book_reader(eliot))], 
['Henry Fielding', 'The History of Tom Jones', word_count(book_reader(fielding)), unique_count(book_reader(fielding))],
['E.M. Forster', 'A Room with a View', word_count(book_reader(forster)), unique_count(book_reader(forster))],
['Elizabeth Gaskell', 'Cranford', word_count(book_reader(gaskell)), unique_count(book_reader(gaskell))],
['Herman Melville', 'Moby Dick', word_count(book_reader(melville)), unique_count(book_reader(melville))],
['L.M. Montgomery', 'The Blue Castle', word_count(book_reader(montgomery)), unique_count(book_reader(montgomery))],
['Tobias Smollett', 'The Adventures of Ferdinand Count Fathom', word_count(book_reader(smollett_fathom)), unique_count(book_reader(smollett_fathom))],
['Tobias Smollett', 'The Expedition of Humphry Clinker', word_count(book_reader(smollett_clinker)), unique_count(book_reader(smollett_clinker))],
['Elizabeth von Armin', 'The Enchanted April', word_count(book_reader(von_arnim)), unique_count(book_reader(von_arnim))]])

statistics = pd.DataFrame(data, columns = ['Author', 'Title', 'Word Count', 'Unique Word Count'])

print(statistics)

#Create .csv file cataloguing the variable statistics
statistics.to_csv('Word_Count.csv')

#Creating .csv files for each book's unique word list and count for use in grapher.py
df_alcott = pd.DataFrame.from_dict(unique_count(book_reader(alcott), True), orient='index').to_csv('alcott_count.csv')
df_eliot = pd.DataFrame.from_dict(unique_count(book_reader(eliot), True), orient='index').to_csv('eliot_count.csv')
df_fielding = pd.DataFrame.from_dict(unique_count(book_reader(fielding), True), orient = 'index').to_csv('fielding_count.csv')
df_forster = pd.DataFrame.from_dict(unique_count(book_reader(forster), True), orient='index').to_csv('forster_count.csv')
df_gaskell = pd.DataFrame.from_dict(unique_count(book_reader(gaskell), True), orient='index').to_csv('gaskell_count.csv')
df_melville = pd.DataFrame.from_dict(unique_count(book_reader(melville), True), orient='index').to_csv('melville_count.csv')
df_montgomery = pd.DataFrame.from_dict(unique_count(book_reader(montgomery), True), orient='index').to_csv('montgomery_count.csv')
df_smollett_c = pd.DataFrame.from_dict(unique_count(book_reader(smollett_clinker), True), orient='index').to_csv('smollett_clinker_count.csv')
df_smollett_f = pd.DataFrame.from_dict(unique_count(book_reader(smollett_fathom), True), orient='index').to_csv('smollett_fathom_count.csv')
df_von_arnim = pd.DataFrame.from_dict(unique_count(book_reader(von_arnim), True), orient='index').to_csv('smollett_clinker_count.csv')
