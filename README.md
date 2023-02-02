# Gutenburg Word Count Project
This is a project that performs analyses on some of the top downloaded books from [The Gutenberg Project](https://www.gutenberg.org/) in Python with visualizations in Python and Tableau.

## Skills Demonstrated
* Python: including seaborn, matplotlib, pandas, regular expressions (RegEx) and defining functions
* Natural Language Processing (NLP) basics
* Tableau: visualizations [here](https://public.tableau.com/app/profile/alexander.adams3449/viz/MobyDickUniqueWordCountWordCloud/Sheet1).

## Process
I started by dowloading a few books from the "Top Downloads" list on The Gutenberg Project's website, linked above. 
After that, using Python's pandas library, I created functions that cleaned the text by removing all punctuation, counted the number of words, counted the number of unique words, and sent all of these counts to a aggregated .csv file [here](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/Word_Count.csv) as well as separate .csv files for each book, one of which is [here](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/melville_count.csv).
Once I had successfully implemented the functions and created the tables necessary, I then developed a Python file to make visualizations, which can be found below. ⬇⬇⬇

![Word Count by Book](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/Word_Count_by_Book.png?raw=true)

![Unique Word Count by Book](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/Unique_Word_Count_by_Bookpng.png)

![Word Count vs. Unique Word Count](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/Word_Count_v_Unique_Count.png)

After this, I removed some of the most common words from the melville_count.csv using a filter in order to create a Tableau visualization in the form of a word cloud, available [here](https://public.tableau.com/app/profile/alexander.adams3449/viz/MobyDickUniqueWordCountWordCloud/Sheet1).

## Full Python Code Below
Code used to process the raw .txt files into a useful format available [here](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/word_counter.py).

Code used to turn the processed files into visualizations in Python available [here](https://github.com/aadams10046/Gutenburg_Word_Count_Project/blob/main/grapher.py).
