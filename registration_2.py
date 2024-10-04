import requests
import time
import datetime
import ast
Reg_Url_Time_dIct = {}

with open("NEW_URL_2.txt", 'r', encoding='utf-8') as dicti:
    data = dicti.read().strip()
    data = data.replace("\n", " ").strip(",")
    try:
        dict_data = ast.literal_eval("{" + data + "}")
        Reg_Url_Time_dIct.update(dict_data)
    except Exception as problem:
        print('Unabel to read data ')

inp_time_1scrim = int()
inp_time_2scrim = int()
inp_time_3scrim = int()
inp_time_4scrim = int()


inp_time_end = int()


def LinkUpdate():

    print('1. DELETE OLD URL DATA \n2. ENTER NEW URL DATA')
    user_choice = input('ENTER YOUR CHOICE (1/2) : ')
    if user_choice == '1':
        user_choice_confirmation = input('YOUR ALL OLD URL DATA WILL BE DELETED, DO YOU WANT TO CONTINUE (Y/N) : ')
        if user_choice_confirmation == 'Y' or 'y' :
            with open('NEW_URL_2.txt','w', encoding='utf-8') as delete:
                delete.write('')
            print('URL DATA IS SUCCESSFULLY DELETED :) ')
            time.sleep(3)
            LinkUpdate()
        elif user_choice_confirmation == 'N' or 'n':
            print('NOT DELETING YOUR DATA, RETURNING TO LINK UPDATE MENU ')
            time.sleep(3)
            LinkUpdate()
        else:
            print('ONLY RESPONSE WITH (Y/N), RETURNING TO LINK UPDATE MENU ')
            time.sleep(3)
            LinkUpdate
    if user_choice == '2':
        
        inp_Url = input('ENTER THE URL ')
        inp_time_url = input(f'ENTER THE TIME OF REGISTRATION OF URL {inp_Url} (IN HOUR:MINUTE:SECOND) : ')
        print('\n')
        print(f'Make sure to match the url, Your entered URL is {inp_Url}')
        dec = input('Do you want to update the url (Y/N) : ')
        if dec == 'Y':
            with open('NEW_URL_2.txt', 'a', encoding='utf-8') as link:
                link.write(f'"{inp_time_url}" : "{inp_Url}",\n')
            print('LINK UPDATED WAIT YOU ARE REDIRECTED TO MAIN SCREEN :)')
            time.sleep(3)
            LinkUpdate()
        
        with open("NEW_URL_2.txt", 'r', encoding='utf-8') as dicti:
            data = dicti.read().strip()
            data = data.replace("\n", " ").strip(",")
            try:
                dict_data = ast.literal_eval("{" + data + "}")
                Reg_Url_Time_dIct.update(dict_data)
            except Exception as problem:
                print(f'Error to update URL {inp_Url}: {problem}')
    
        print(Reg_Url_Time_dIct.keys())
    
        if dec == 'N':
            print('Returning to enter screen :)')
            time.sleep(4)
            LinkUpdate()
        



def welcome_screen():
    print('HELLO THERE, WELCOME TO OUR REGISTRATION SOFTWARE \n \n \n \n \n')
    print('1. : UPDATE REGISTRATION URL')
    print('2. : REGISTRATION DETAILS')
    print('3. : QUIT')
    print('\n \n ')
    Choice = int(input('ENTER YOUR CHOICE : '))
    if Choice == 1:
        LinkUpdate()
    elif Choice ==2:
        registration_data()
    elif Choice ==3:
        quit()

lis = []

with open('url.txt','r', encoding='utf-8') as sno:
    for line in sno:
        lis.append(line.strip())


def registration_data():

    print('AVAILABLE SCRIMS TO REGISTER ARE AS FOLLOW : \n')

    stored_data = list(Reg_Url_Time_dIct.keys())

    n=0
    for data in  stored_data:
        print(f'{n+1} --> {stored_data[n]}')
        n+=1

    

    while True:
        scrim = (input("ENTER SCRIMS NO YOU WANT TO REGISTER WITHOUT ANY SPACE EX(1234), IF YOU ARE DONE SELECTING SCRIMS TYPE DONE TO START REGISTRATION "))
        scrims = list(scrim)
        n =0
        for no in scrims:
            scrim_no = int(scrims[n])
            print(stored_data[scrim_no -1 ])
            scrim_to_register = stored_data[scrim_no -1]
            # register(Reg_Url_Time_dIct[f'{scrim_to_register}'])
            reg_URL = Reg_Url_Time_dIct[f'{scrim_to_register}']
            time_match(scrim_to_register,reg_URL)
            n+=1

def time_match(time_registration,scrim_url):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(0.1)
        if current_time == time_registration:
            register(scrim_url)
        # print(time_registration)
        if current_time> time_registration:
            print('returning')
            return



def register(sno):

    url = f"https://discord.com/api/v9/channels/{sno}/messages"
    
    headers = {
        "Authorization": "MTExNzgzMzkxODY5NjEyODUxMg.GvYaAS.WztT9Mv0ajNvgZHlnGNh2pzzHzZPRZmoBynSg0",    
        "Content-Type": "application/json"
    }
    
    msg = {
        'content': 'TEAM NAME : SUGARx <@1117833918696128512> <@896979044837511188> <@1216632380815573035> <@745564134103318539> '
    }
    
    response = requests.post(url, headers=headers, json=msg)
    
    print(response.status_code)
    print(response.json())
    a = str(response.status_code )
    with open('process.txt','a', encoding='utf-8') as file:
        file.write(a)
        file.write('\n')
    b = str(response.json())
    with open('json_Pro.txt','a', encoding='utf-8') as jsn:
        jsn.write(b)
        jsn.write('\n')
        


welcome_screen()






