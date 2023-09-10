import pandas as pd
import numpy as np
from sklearn import utils
import random

def generate_question(data):
    df = pd.read_csv(f"src/data/{data}")

    vocabulary = utils.shuffle(df.values)
    vocabulary_list = []

    question = np.array([[0, 0, 0]])
    question = np.delete(question, 0, axis=0)

    options_list = []
    
    for i in range(len(df)):
        
        question = np.row_stack((question, vocabulary[i]))

        while len(question) < 4:
            random_vocabulary_num = random.randint(0, len(df))
            random_vocabulary = np.array(
                vocabulary[random_vocabulary_num-1])

            if np.isin(random_vocabulary, question, invert=True).any():
                question = np.row_stack((question, random_vocabulary))

        question = utils.shuffle(question)
        options_list.append([j[2] for j in question])
        question = np.delete(
            question, [0, 1, 2, 3], axis=0)
        
    for i in range(len(df)):
        vocabulary_list.append(' '.join(str(i)
            for i in vocabulary[i][0:3]))

    return vocabulary_list,options_list

if __name__=="__main__":
    a = generate_question("day3.csv")
    print(a[1])