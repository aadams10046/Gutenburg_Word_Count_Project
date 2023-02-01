#Importing the appropriate packages for later use
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Reading Word_Count.csv into a DataFrame for use in the graphing elements below
info = pd.read_csv('Word_Count.csv')

#Function for graphing Word Count vs. Unique Word Count in seaborn with tending line
def wc_v_uwc():
    sns.regplot(data = info, x = info['Unique Word Count'], y = info['Word Count'] , fit_reg = True)
    plt.xlabel('Word Count')
    plt.ylabel('Unique Word Count')
    plt.title('Total Word Count vs. Number of Unique Words per Book')
    plt.show()

#Function for graphing Word Count per book
def word_count_bar():
    sns.barplot(data = info, x = info['Title'], y = info['Word Count'], palette = 'pastel', width = 1)
    plt.xticks(rotation = 45, ha = 'right')
    plt.xlabel('Book Title')
    plt.ylabel('Word Count')
    plt.title('Word Count by Book')
    plt.show()

#Function for graphing Unique Count per book
def unique_word_count_bar():
    sns.barplot(data = info, x = info['Title'], y = info['Unique Word Count'], palette = 'pastel', width = 1)
    plt.xticks(rotation = 45, ha = 'right')
    plt.xlabel('Book Title')
    plt.ylabel('Unique Word Count')
    plt.title('Unique Word Count by Book')
    plt.show()