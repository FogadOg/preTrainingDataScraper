from bs4 import BeautifulSoup
from selenium import webdriver
import keyboard 
import requests
import time
import re
import csv


urls=[
    "https://en.wikipedia.org/wiki/United_States",
    "https://en.wikipedia.org/wiki/Reddit",
    "https://en.wikipedia.org/wiki/Internet_culture",
    "https://en.wikipedia.org/wiki/Debugging",
    "https://en.wikipedia.org/wiki/Meme",
    "https://en.wikipedia.org/wiki/Humour",
    "https://en.wikipedia.org/wiki/Comedy",
    "https://en.wikipedia.org/wiki/Stand-up_comedy",
    "https://en.wikipedia.org/wiki/Programming_language",
    "https://en.wikipedia.org/wiki/Language",
    "https://en.wikipedia.org/wiki/Psychology",
    "https://en.wikipedia.org/wiki/21st_century",
    "https://en.wikipedia.org/wiki/School",
    "https://en.wikipedia.org/wiki/Education",
    "https://en.wikipedia.org/wiki/Economy",
    "https://en.wikipedia.org/wiki/Physics",
    "https://en.wikipedia.org/wiki/Physicist",
    "https://en.wikipedia.org/wiki/Evolution",
    "https://en.wikipedia.org/wiki/Big_Bang",
    "https://en.wikipedia.org/wiki/Leonardo_da_Vinci",
    "https://en.wikipedia.org/wiki/Roman_Empire",
    "https://en.wikipedia.org/wiki/History_of_the_Roman_Empire",
    "https://en.wikipedia.org/wiki/Ancient_Egypt",
    "https://en.wikipedia.org/wiki/Ancient_Greece",
    "https://en.wikipedia.org/wiki/Classical_Athens",
    "https://en.wikipedia.org/wiki/Ancient_history",
    "https://en.wikipedia.org/wiki/17th_century",
    "https://en.wikipedia.org/wiki/GitHub",
    "https://en.wikipedia.org/wiki/Cmd.exe",
    "https://en.wikipedia.org/wiki/PowerShell",
    "https://en.wikipedia.org/wiki/Git",
    "https://en.wikipedia.org/wiki/API",
    "https://en.wikipedia.org/wiki/Nature",
    "https://en.wikipedia.org/wiki/Geology",
    "https://en.wikipedia.org/wiki/Africa",
    "https://en.wikipedia.org/wiki/Asia",
    "https://en.wikipedia.org/wiki/Europe",
    "https://en.wikipedia.org/wiki/North_America",
    "https://en.wikipedia.org/wiki/South_America",
    "https://en.wikipedia.org/wiki/Antarctica",
    "https://en.wikipedia.org/wiki/Oceania",
    "https://en.wikipedia.org/wiki/Minecraft",
    "https://en.wikipedia.org/wiki/Counter-Strike:_Global_Offensive",
]


class WaitForKeyPress():
    def _waitForKeyPress(self):
        keyboard.wait('esc')


class Scrape(WaitForKeyPress):
    def __init__(self, url) -> None:        
        self.url=url

    def startScrapingWebsite(self):
        page=self._sendRequestToMainPage(self.url)
        text=self._getTextDataFromWebsite(page)
        saveData=CreateCsvData(20,text)
        saveData.CreateTextSequancesWithWindow()

    def _sendRequestToMainPage(self,url):
        response=requests.get(url)
        # dr = webdriver.Chrome()
        # dr.get(url)
        # self._waitForKeyPress()
        page = BeautifulSoup(response.content,"html.parser")
        return page

    def _getTextDataFromWebsite(self,page)->list:
        textDataset=[]
        textData=page.find_all("div","mw-parser-output")

        for sentance in textData:
            for paragraph in sentance.find_all("p"):
                textDataset.append(paragraph.text)
        return "".join(textDataset)


class CreateCsvData():
    def __init__(self, windowSize, textSequance):
        self.windowSize=windowSize
        self.textSequance=textSequance

    def cleanText(self,sen):
        # Remove punctuations and numbers
        sentence = re.sub('[^a-zA-Z]', ' ', sen)

        # Single character removal
        sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

        # Removing multiple spaces
        sentence = re.sub(r'\s+', ' ', sentence)

        return sentence.lower()[1:-2]

    def CreateTextSequancesWithWindow(self):
        cleanedText=self.cleanText(self.textSequance)
        textSplitBySpace=cleanedText.split(" ")
        sequanceLength=len(textSplitBySpace)
        
        preiviusSentance=None
        with open(f'preTrainingData.csv', 'a', encoding='UTF8') as f:                
            #write header for columns in csv file
            dw = csv.DictWriter(f, delimiter=',', 
                fieldnames=["input","target"])
            dw.writeheader()
        for i in range(sequanceLength-self.windowSize):
        
            textSequance=textSplitBySpace[i:i+self.windowSize]

            if preiviusSentance!=None:


                with open(f'preTrainingData.csv', 'a', encoding='UTF8') as f:

                    writer = csv.writer(f)
                    writer.writerow([preiviusSentance," ".join(textSequance)])

            #remove the first word so the sentances are alignet proprety
            preiviusSentance=" ".join(textSequance[1:])


for url in urls:
    Scrape(url).startScrapingWebsite()




