import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PredeterminedMeeting = False;
PredeterminedMeetingCode = "null";

print('''BEFORE USING:
         You must first install SELENIUM.
         Please add your webdriver(Preferably Chrome) to PATH, or else this will NOT WORK.
         Also, Please change the "progr" in /Users/progr/AppData/Local/Google/Chrome/User Data in the code to the name of your user folder.
         You must be the only profile in Chrome, if not, please contact me.''')
options = webdriver.ChromeOptions()
options.add_argument(
    '--user-data-dir=/Users/progr/AppData/Local/Google/Chrome/User Data')
options.add_argument(
    '--profile--directory=Default')





browser = webdriver.Chrome(options=options
                           )




def NewMeet(FirstTime):
    if(FirstTime == False):
        browser.switch_to.window(browser.window_handles[0])
        browser.get("https://meet.google.com")
    else:
        browser.get("https://meet.google.com")
    time.sleep(5)
    ##email = browser.find_element(By.ID, 'identifierId')
    ##email.send_keys("hackerscode09@gmail.com")
    NewMeeting = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button')
    browser.execute_script("arguments[0].click();", NewMeeting)
    time.sleep(1)
    RequestCode = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[1]/span[3]')
    browser.execute_script("arguments[0].click();", RequestCode)
    time.sleep(3)
    Copy = browser.find_element(By.CLASS_NAME, 'Hayy8b')
    MeetCode = Copy.text
    print(MeetCode)
    return MeetCode

def JoinMeet(MeetCode, FirstTime):
        if(FirstTime == True):            
           browser.execute_script("window.open('');")
            
        browser.switch_to.window(browser.window_handles[1])            
        if "https://" not in MeetCode:
            MeetCode = "https://" + MeetCode
        browser.get(MeetCode)
        time.sleep(7)
##        Camera = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[6]/div[2]/div')
##        browser.execute_script("arguments[0].click();", Camera)
##        Mic = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[6]/div[1]/div')
##        browser.execute_script("arguments[0].click();", Mic)
        ActionChains(browser).send_keys(Keys.CONTROL, "e").perform()
        ActionChains(browser).send_keys(Keys.CONTROL, "d").perform()
        time.sleep(1)
        JoinMeetButton = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button')
        browser.execute_script("arguments[0].click();", JoinMeetButton)
        time.sleep(0.5)
        ActionChains(browser)\
            .key_down(Keys.CONTROL)\
            .send_keys("e")\
            .perform()
        time.sleep(1)
        ActionChains(browser)\
            .key_down(Keys.CONTROL)\
            .send_keys("d")\
            .perform()


def PasteInChat(MeetCode):

        browser.switch_to.window(browser.window_handles[1])
        ChatButton = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[14]/div[3]/div[11]/div/div/div[3]/div/div[3]/div/div/span/button')
        browser.execute_script("arguments[0].click();", ChatButton)
        time.sleep(4)
        ChatBox = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[14]/div[3]/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/label/textarea')
        ChatBox.send_keys("--AUTOMATIC MEETING RESTART--")
        time.sleep(0.5)

        SendButton = browser.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div[1]/div/div[14]/div[3]/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/span/button')
        browser.execute_script("arguments[0].click();", SendButton)
        ChatBox.send_keys("--AUTOMATIC MEETING RESTART--")
        time.sleep(2)
        ChatBox.send_keys(MeetCode)
        time.sleep(2)
        browser.execute_script("arguments[0].click();", SendButton)


def MainLoop():
##    MeetingCode = input("What is the meeting URL?")
##    JoinMeet(MeetingCode)
    AskInput = input("Do you want ReMeet to start a new meeting now?")
    if (AskInput.lower()[0] == "y"):
        PredeterminedMeeting == False
        print("Doin' that now.")
    else:
        PredeterminedMeeting == True
        print("Ok, ReMeet will just need the meeting code.")

    if(PredeterminedMeeting == True):
        MeetingCode = input("What is the meeting code?")
    else:
        MeetingCode = NewMeet(FirstTime = True)

    JoinMeet(MeetingCode, FirstTime = True)
    while True:
        print("Timer starting/restarting")
        time.sleep(2700)
        MeetingCode = NewMeet(FirstTime = False)
        PasteInChat(MeetingCode)
        JoinMeet(MeetingCode, FirstTime = False)


MainLoop()

    
