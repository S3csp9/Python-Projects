from newsapi import NewsApiClient
from win32com.client import Dispatch

newsapi = NewsApiClient(api_key='e5ef7ecc652240929e5711e4c24b6f67')

def speaks(line):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(line)

def news(categ):
    all_articles = newsapi.get_everything(q=categ,
                                    sources='bbc-news,the-verge',
                                    language='en',
                                    sort_by='popularity')
    headlines = all_articles["articles"]
    for i in range(10):
        # headline = headlines[i]['title']
        headline = headlines[i]['description']
        print(f"{i+1}. {headline}")
        speaks(headline)
        if i==9:
            break
        elif i == 8:
            speaks("Moving to our last news.")
        else:
            speaks("Moving to next news.")


if __name__ == '__main__':
    print("Welcome to our News Portal! v2")
    speaks("Welcome to our News Portal!")
    while True:
        print("\nWhat do you want?\n")
        speaks("What do you want?")
        print("1. Start\n"
                "2. Exit")        
        try:
            op = int(input("Choose an Option : "))
            if op == 1:
                print("Which type of News want to Listen and Read : ")
                speaks("Which type of News want to Listen and Read : ")
                query = input()
                news(query)
                
            elif op == 2:
                print("Thank you for using our Program. Have a Nice Day. ")
                speaks("Thank you for using our Program. Have a Nice Day. ")
                quit()
                
            else:
                print("Please Enter a Valid Option !!!")
                speaks("Please Enter a Valid Option !!!")
                
        except ValueError:
            print("Please Enter a Valid Option !!!")
            speaks("Please Enter a Valid Option !!!")