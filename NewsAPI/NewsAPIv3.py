import requests
# import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    print("Welcome to our News Portal")
    speak("Welcome to our News Portal")
    while True:
        print("What type of News Topic you want to Listen ?")
        speak("What type of News Topic you want to Listen ?")
        print("1. General\n"
            "2. Entertainment\n"
            "3. Business\n"
            "4. Health\n"
            "5. Science\n"
            "6. Sports\n"
            "7. Technology")
        category = int(input("Type Here : "))
        
        if category == 1:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            print(web)
            print(data)
            result = data['articles']
            print(result)
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 2:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 3:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 4:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 5:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 6:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        elif category == 7:
            web = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5d8feb879aa24e73ae22c310b77fa9a4")
            data = web.json()
            result = data['articles']
            for i in range(15):
                news = result[i]['description']
                print(f"{i+1}. {news}")
                speak(f"{news}")
                if i >= 14:
                    break
                if i == 13:
                    speak("Moving to our Today's Last News.")
                else:
                    speak("Moving to our Next News.")
                    
        else :
            print("You Entered Invalid Input. Please Enter a Valid Input !!!")
            speak("You Entered Invalid Input. Please Enter a Valid Input !!!")