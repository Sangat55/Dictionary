import urllib.parse
import urllib.request
import lxml
from bs4 import BeautifulSoup as bs4
def choice11():
    choice1 = input("Enter q to exit and n to search new item: ")
    if(choice1 == 'q'):
        return False
    elif (choice1 == 'n'):
        return True
    else:
        choice11()

def search(query):
        url  = "https://dictionary.cambridge.org/dictionary/english/%s"% (urllib.parse.quote_plus(query))
        url2 = "https://www.oxforddictionaries.com/definition/%s"% (urllib.parse.quote_plus(query))
        urlfile = urllib.request.urlopen(url)
        urlfile2= urllib.request.urlopen(url2)
        htmlResult = urlfile.read()
        htmlResult2 = urlfile2.read()
        urlfile.close()
        urlfile2.close()
        soup = bs4(htmlResult,'lxml')
        soup2= bs4(htmlResult2 , 'lxml')
        print("*************************CAMBRIDGE***************************")
        print("\n")
        findMeaning = soup.find_all('b', attrs={"class":"def"})
        i = 1
        for meaning in findMeaning:
                print(str(i) + ". " + meaning.text)
                i = i + 1
        print("\n\n")
        print("*************************OXFORD*****************************")
        print("\n")
        findMeaning2 = soup2.find_all('span' , attrs = {"class":"ind"})
        j=1
        for meaning2 in findMeaning2:
                print(str(j) + ". " + meaning2.text)
                j =j + 1
choice = True
while(choice):
    filename = input("Enter the english Word: ")
    search(filename)
    choice = choice11()

