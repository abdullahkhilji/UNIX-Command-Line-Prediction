# **Knowledge Base Creation**

The data obtained after scraping from the website is passed through an extensive process of pre-processing. The various columns obtained are concatenated, all special characters are removed and the resulting data is stemmed to obtain a uniform data for all the commands. For further removing bias due to large data present in some of the commands, common words 3 characters or less are removed to finally obtain a data ready for synonym pair extraction.
The data is then feeded as input to kb.py and an output knowledge base can be obtained.
