#现在火焰是自由的了
import os
import codecs
import pandas as pd
import csv
from bs4 import BeautifulSoup
import re

path = "./data/labeledTrainData.tsv"


'''with open(path, "r",encoding='utf-8') as f:
    labeledTrain = [line.strip().split("\t") for line in f.readlines() if len(line.strip().split("\t")) == 3]
    #print(unlabeledTrain)
    unlabel = pd.DataFrame(labeledTrain[1:], columns=labeledTrain[0])
    print(unlabel.head(5))'''
train = pd.read_csv(path,sep='\t')
#print(train.head(5))
def cleanReview(subject):
    beau = BeautifulSoup(subject)

    re_tag = re.compile(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]')
    newsubject = beau.get_text()

    newsubject = newsubject.strip().split(" ")
    #newsubject.split(re_tag)
    newsubject = [word.lower()for word in newsubject]
    newsubject = " ".join(newsubject)
    return newsubject
train["review"] = train["review"].apply(cleanReview)
#print(train.head(5))
newLabel = train[["review","sentiment"]]
print(newLabel.head(5))
newLabel.to_csv("./data/testdata.csv",index=False)


