import requests
import json
import time
import uiautomator2 as u2
import random

def get_balance():

    url = "http://rummynabob.4599vip.com:8080/user/api/refreshgold"
    data = {'userId': '1082024', 'token': '5FDCB0A9C9134BA3B7630C1F656FF802'}
    headers = {'Content-type': 'application/json', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; ASUS_X00PD Build/OPR1.170623.032)','Accept-Encoding':'identity'}
    r = requests.post(url, data=json.dumps(data), headers=headers,verify=False)
    json_data = json.loads(r.text)
    balance=json_data['data'][0]['Score']
    print(balance)
    return int(balance)

d = u2.connect()
cordinates = {"andar": [0.31, 0.562], "bahar": [0.728, 0.555]}
amount_cordinates={10:[0.292, 0.907],50:[0.384, 0.918],100:[0.48, 0.914],500:[0.572, 0.914],1000:[0.662, 0.918]}

def get_random_side():
    test_list = ['andar','bahar']
    random_side =random.choice(test_list)
    return random_side


def bet_10(side):
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_20(side):
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_40(side):
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_80(side):
    d.click(amount_cordinates[50][0], amount_cordinates[50][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_160(side):
    d.click(amount_cordinates[100][0], amount_cordinates[100][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[50][0],amount_cordinates[50][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])



def bet_320(side):
    d.click(amount_cordinates[100][0], amount_cordinates[100][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])



def bet_640(side):
    d.click(amount_cordinates[500][0], amount_cordinates[500][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[100][0], amount_cordinates[100][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[10][0], amount_cordinates[10][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])



def bet_50(side):
    d.click(0.382, 0.907)
    d.click(cordinates[side][0], cordinates[side][1])

def bet_100(side):
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])

def bet_200(side):
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_400(side):
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_800(side):
    d.click(0.574, 0.925)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_1600(side):
    d.click(0.666, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(0.574, 0.925)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])

def bet_3200(side):
    d.click(0.664, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(0.478, 0.921)
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_6400(side):
    d.click(amount_cordinates[1000][0], amount_cordinates[1000][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(amount_cordinates[100][0], amount_cordinates[100][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])




while True:
     balance=get_balance()
     time.sleep(5)
     print ("place bet 50")
     side=get_random_side()
     print(side)
     bet_50(side)
     time.sleep(10)

     while(get_balance() == balance):
         print("balance not updated")
         time.sleep(1)

     if(get_balance() < balance):
         balance=get_balance()
         time.sleep(5)
         print("place bet 20")
         side = get_random_side()
         print(side)
         bet_100(side)
         time.sleep(10)

         while (get_balance() == balance):
             print("balance not updated")
             time.sleep(1)

         if (get_balance() < balance):
            balance = get_balance()
            time.sleep(5)
            print("place bet 200")
            side = get_random_side()
            print(side)
            bet_200(side)
            time.sleep(10)

            while (get_balance() == balance):
                print("balance not updated")
                time.sleep(1)

            if (get_balance() < balance):
                balance = get_balance()
                time.sleep(5)
                print("place bet 400")
                side = get_random_side()
                print(side)
                bet_400(side)
                time.sleep(10)

                while (get_balance() == balance):
                 print("balance not updated")
                 time.sleep(1)

                if (get_balance() < balance):
                      balance = get_balance()
                      time.sleep(5)
                      print("place bet 800")
                      side = get_random_side()
                      print(side)
                      bet_800(side)
                      time.sleep(10)

                      while (get_balance() == balance):
                          print("balance not updated")
                          time.sleep(1)
                          time.sleep(1)

                      if (get_balance() < balance):
                        balance = get_balance()
                        time.sleep(5)
                        print("place bet 1600")
                        side = get_random_side()
                        print(side)
                        bet_1600(side)
                        time.sleep(10)

                        while (get_balance() == balance):
                            print("balance not updated")
                            time.sleep(1)

                        if (get_balance() < balance):
                            balance = get_balance()
                            time.sleep(5)
                            print("place bet 3200")
                            side = get_random_side()
                            print(side)
                            bet_3200(side)
                            time.sleep(10)

                      #       while (get_balance() == balance):
                      #           print("balance not updated")
                      #           time.sleep(1)
                      #
                      #       if (get_balance() < balance):
                      #           balance = get_balance()
                      #           time.sleep(5)
                      #           print("place bet 6400")
                      #           side = get_random_side()
                      #           print(side)
                      #           bet_6400(side)
                      #           time.sleep(10)



