# Joint Learning
We have used joint learning model for learning word vector representations from both large text corpora and the knowledge base that was created in the previous step.
- We have used the JointReps model (https://github.com/suhaibani/JointReps) for this purpose.
- The coocurance matrix have been made using https://github.com/stanfordnlp/GloVe.

# File Description
- **convert.c** is used to convert the binary coocurance file obtained from https://github.com/stanfordnlp/GloVe. 
- **coocurance.txt** is the coocurance matrix obtained after the conversion.
- **vocab.txt** is the vocaulary of our corpus
- **mapped_cooccurence.txt** is our final coocurance file otained after mapping with the help of vocab.txt. This will be the input to JoinReps Model as the edge parameter.
