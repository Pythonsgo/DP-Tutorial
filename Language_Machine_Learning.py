# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015

##########################################################################
## Imports
##########################################################################

from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split as tts
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

import numpy as np


##########################################################################
## Module Constants
##########################################################################
##########################################################################
## Modules
##########################################################################
##########################################################################
## Program
##########################################################################

if __name__ == "__main__":

    corpus = load_files("Language_Folder")
 
    #print len(corpus.data)
 
    X_train, X_test, y_train, y_test = tts(corpus.data, corpus.target, test_size=0.20)
    
    
    text_clf = Pipeline([
        ('vec', CountVectorizer(analyzer='char_wb')),
        ('clf', MultinomialNB())
    ])
        
    text_clf = text_clf.fit(X_train, y_train)
    predicted = text_clf.predict(X_test)
    accuracy = np.mean(predicted==y_test)
    print accuracy
    
    random_test = ['el dia esta bello.', 'cuantos anos tienes?', 'hello there!', 'nein']
    
    predicted_random = text_clf.predict(random_test)
    print predicted_random
      
     
    
    