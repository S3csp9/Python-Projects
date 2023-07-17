from newsapi import NewsApiClient
from win32com.client import Dispatch

newsapi = NewsApiClient(api_key='e5ef7ecc652240929e5711e4c24b6f67')

def speaks(line):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(line)


def news(categ):
    top_headlines = newsapi.get_top_headlines(category= categ,
                                            language= "en",
                                            country= "in")
    headlines = top_headlines["articles"]
    for i in range(10):
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
    print("Welcome to our News Portal!")
    speaks("Welcome to our News Portal!")
    while True:
        print("\nWhich type of News want to Listen and Read?\n"
                "1. General\n"
                "2. Entertainment\n"
                "3. Business\n"
                "4. Health\n"
                "5. Science\n"
                "6. Sports\n"
                "7. Technology\n"
                "8. Exit")
        speaks("Which type of News want to Listen and Read?")
        # speaks("Which type of News want to Listen and Read? \n1. General \n2. Entertainment \n3. Business \n4. Health \n5. Science \n6. Sports \n7. Technology \n8. Exit")
        
        try:
            op = int(input("Choose an Option : "))
            if op == 1:
                print("\nNow, We begin with Today's General News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's General News")
                news("general")
                
            elif op == 2:
                print("\nNow, We begin with Today's Entertainment News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Entertainment News")
                news("entertainment")
                
            elif op == 3:
                print("\nNow, We begin with Today's Business News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Business News")
                news("business")
                
            elif op == 4:
                print("\nNow, We begin with Today's Health News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Health News")
                news("health")
                
            elif op == 5:
                print("\nNow, We begin with Today's Science News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Science News")
                news("science")
                
            elif op == 6:
                print("\nNow, We begin with Today's Sports News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Sports News")
                news("sports")
                
            elif op == 7:
                print("\nNow, We begin with Today's Technology News\n------------------------------------------------------------------")
                speaks("Now, We begin with Today's Technology News")
                news("technology")
                
            elif op == 8:
                print("Thank you for using our Program. Have a Nice Day. ")
                speaks("Thank you for using our Program. Have a Nice Day. ")
                quit()
                
            else:
                print("Please Enter a Valid Option !!!")
                speaks("Please Enter a Valid Option !!!")
                
        except ValueError:
            print("Please Enter a Valid Option !!!")
            speaks("Please Enter a Valid Option !!!")