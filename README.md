# Mathsage

__Mathsage__ (or Math-sage) is a semester-long project for Natural Language Processing (CS5624).

MathQA Dataset GitHub repo

- https://math-qa.github.io/math-QA/index.html

## Files

Our final code is contained in the directory, "final", containing the following files:

1. MathQA_Preprocessing: Preprocesses the MathQA dataset as outlined in our paper
2. MathQA_Preprocessing2: A continuation of the previous file
3. MathQA_Const_Classifier: Creates the multi label constant classifier portion of our model
4. MathQA_Op_Classifier: Creates the multi label operator classifier portion of our model
5. MathQA_Masked_Language_Modeling: Fine tunes a pretrained encoder model on MathQA
6. MathQA_Independent_Subexpressions: Contains the code for the outlined independent subexpression predictor
7. MathQA_Final_Training: Used for training the seq2seq model for flan-t5-base and flan-t5-large
8. MathQA_Flan_T5_Base_Evaluation - Evaluates the performance of the base model
9. MathQA_Flan_T5_Large_Evaluation - Evaluates the performance of the large model
