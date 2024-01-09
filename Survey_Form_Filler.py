import time
from selenium import webdriver
import pyautogui
import sys
import keyboard

# This opens up a chrome tab that will open to the page of the survey

web = webdriver.Chrome()
web.get('Link to Survey')
time.sleep(0.3)

# This is the function that will input the text and select the option that we want to be submitted
def Surveyform():
# This is the path for the questions within the Survey
    student = web.find_element('xpath', '/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/div[1]/div[1]')
    student.click()

    age = web.find_element('xpath', '/html/body/main/article/section/form/div[1]/div[2]/div/div/fieldset/div/div/div[2]')
    age.click()

    Emotions = web.find_element('xpath', '/html/body/main/article/section/form/div[1]/div[6]/div/div/fieldset/div/div[1]/div[2]')
    Emotions.click()

    possibility1 = web.find_element('xpath' , '/html/body/main/article/section/form/div[1]/div[8]/div/div/div/div/table/tbody/tr[4]/td[3]/div/label/span[1]')
    possibility1.click()
    possibility2 = web.find_element('xpath' , '/html/body/main/article/section/form/div[1]/div[8]/div/div/div/div/table/tbody/tr[7]/td[2]/div/label/span[1]')                               
    possibility2.click()
    possibility3 = web.find_element('xpath' , '/html/body/main/article/section/form/div[1]/div[8]/div/div/div/div/table/tbody/tr[8]/td[4]/div/label/span[2]')
    possibility3.click()
#This is the Xpath to a(n) textbox within the survey form that inputs a preselected response.
    Related = 'Example phrase to input into the text field'
    Ideas = web.find_element('xpath', '/html/body/main/article/section/form/div[1]/div[9]/div/div/div/div/div/textarea')
    Ideas.send_keys(Related)

    racoon_name = 'Bandit'
    name_sug = web.find_element('xpath' , '/html/body/main/article/section/form/div[1]/div[10]/div/div/fieldset/div/div[2]/input')
    name_sug.send_keys(racoon_name)
    
submit_counter = 1

def submit():
    global submit_counter  # Declaring the global variable inside the function
    submit_counter += 1  # Increment the counter

    # Your existing code
    Submit = web.find_element('xpath', '/html/body/main/article/section/form/div[2]/button')
    Submit.click()
    print("Submission", submit_counter)

Surveyform()

while True:
    submit()
    time.sleep(0.1)
    pyautogui.hotkey('F5')
    if keyboard.is_pressed("q"):
        print("Q pressed, Script has finished")
        break


    
