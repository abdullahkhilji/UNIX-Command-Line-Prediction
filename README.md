# UNIX-Command-Line-Prediction
This repository provides an insight into ventures of framing an intelligent Command line interface (CLI) for UNIX Based Systems.


# **Data Scraping**

The database of linux documentation can be obtained by Web Scraping the domain https://linux.die.net/ by depoying the python library Beautiful Soup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/). The script yields two comma seperated values files
named 'cmd-names.csv' and 'data.csv' containing name of the UNIX command and it's particulars' links and Complete database of the command respectivey. 
This data can be pre-processed and utilized for the construction of knowedge base.

# Joint Learning
We have used joint learning model for learning word vector representations from both large text corpora and the knowledge base that was created in the previous step.
- We have used the JointReps model (https://github.com/suhaibani/JointReps) for this purpose.
- The coocurance matrix have been made using https://github.com/stanfordnlp/GloVe.

# File Description
- **convert.c** is used to convert the binary coocurance file obtained from https://github.com/stanfordnlp/GloVe. 
- **coocurance.txt** is the coocurance matrix obtained after the conversion.
- **vocab.txt** is the vocaulary of our corpus
- **mapped_cooccurence.txt** is our final coocurance file otained after mapping with the help of vocab.txt. This will be the input to JoinReps Model as the edge parameter.

# **Knowledge Base Creation**

The data obtained after scraping from the website is passed through an extensive process of pre-processing. The various columns obtained are concatenated, all special characters are removed and the resulting data is stemmed to obtain a uniform data for all the commands. For further removing bias due to large data present in some of the commands, common words 3 characters or less are removed to finally obtain a data ready for synonym pair extraction.
The data is then feeded as input to kb.py and an output knowledge base can be obtained.



