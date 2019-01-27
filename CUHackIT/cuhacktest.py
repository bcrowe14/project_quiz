import requests
import flask
from bs4 import BeautifulSoup
from flask import Flask, request
from flask import Flask
from flask import make_response

response = requests.get('https://quizlet.com/74960844/cuhackit-quizlet-flash-cards/')
soup = BeautifulSoup(response.text, 'html.parser')

print("List Qs")
questions = soup.find_all(class_='SetPageTerm-wordText')
for Q in questions:
    print(Q.get_text())
    #print(notA.find('span', {'class': 'TermText notranslate lang-en'}).get_text())

print()



print("List As")
ans = soup.find_all(class_='SetPageTerm-definitionText')
for A in ans:
    print(A.get_text())
    #print(notA.find('span', {'class': 'TermText notranslate lang-en'}).get_text())

#for i in question: print(i.get_text())

class Question:

    def __init__(self):
        self.qs = questions
        #self.as = ans

