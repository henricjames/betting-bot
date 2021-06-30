import requests
import json
import time
import uiautomator2 as u2
import random

def get_balance():

    url = "http://rummynabob.4599vip.com:8080/user/api/refreshgold"
    data = {'userId': '1008354', 'token': 'E8FFBE549AF14D258F03E51C3F9EE114'}
    headers = {'Content-type': 'application/json', 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; ASUS_X00PD Build/OPR1.170623.032)','Accept-Encoding':'identity'}
    r = requests.post(url, data=json.dumps(data), headers=headers,verify=False)
    json_data = json.loads(r.text)
    balance=json_data['data'][0]['Score']
    print(balance)
    return int(balance)

d = u2.connect()
cordinates = {"andar": [0.256, 0.953], "bahar": [0.736, 0.953]}
plus_cordinates={"andar":[0.348, 0.953],"bahar":[0.838, 0.953]}

def get_random_side():
    test_list = ['andar','bahar']
    random_side =random.choice(test_list)
    return random_side


def bet_1(side):
    d.click(cordinates[side][0], cordinates[side][1])


def bet_2(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_4(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_8(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_16(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])



def bet_32(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])



def bet_64(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])


def bet_128(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_256(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])

def bet_512(side):
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(plus_cordinates[side][0], plus_cordinates[side][1])
    d.click(cordinates[side][0], cordinates[side][1])




while True:
     balance=get_balance()
     time.sleep(8)
     print ("place bet 1")
     side=get_random_side()
     print(side)
     bet_1(side)
     time.sleep(13)

     while(get_balance() == balance):
         print("balance not updated")
         time.sleep(1)

     if(get_balance() < balance):
         balance=get_balance()
         time.sleep(8)
         print("place bet 2")
         side = get_random_side()
         print(side)
         bet_2(side)
         time.sleep(13)

         while (get_balance() == balance):
             print("balance not updated")
             time.sleep(1)

         if (get_balance() < balance):
            balance = get_balance()
            time.sleep(8)
            print("place bet 4")
            side = get_random_side()
            print(side)
            bet_4(side)
            time.sleep(10)

            while (get_balance() == balance):
                print("balance not updated")
                time.sleep(1)

            if (get_balance() < balance):
                balance = get_balance()
                time.sleep(8)
                print("place bet 8")
                side = get_random_side()
                print(side)
                bet_8(side)
                time.sleep(10)

                while (get_balance() == balance):
                 print("balance not updated")
                 time.sleep(1)

                if (get_balance() < balance):
                      balance = get_balance()
                      time.sleep(8)
                      print("place bet 16")
                      side = get_random_side()
                      print(side)
                      bet_16(side)
                      time.sleep(10)

                      while (get_balance() == balance):
                          print("balance not updated")
                          time.sleep(1)
                          time.sleep(1)

                      if (get_balance() < balance):
                        balance = get_balance()
                        time.sleep(8)
                        print("place bet 32")
                        side = get_random_side()
                        print(side)
                        bet_32(side)
                        time.sleep(10)

                        while (get_balance() == balance):
                            print("balance not updated")
                            time.sleep(1)

                        if (get_balance() < balance):
                            balance = get_balance()
                            time.sleep(8)
                            print("place bet 64")
                            side = get_random_side()
                            print(side)
                            bet_64(side)
                            time.sleep(10)

                            while (get_balance() == balance):
                                print("balance not updated")
                                time.sleep(1)

                            if (get_balance() < balance):
                                balance = get_balance()
                                time.sleep(8)
                                print("place bet 128")
                                side = get_random_side()
                                print(side)
                                bet_128(side)
                                time.sleep(10)

                                while (get_balance() == balance):
                                    print("balance not updated")
                                    time.sleep(1)

                                if (get_balance() < balance):
                                    balance = get_balance()
                                    time.sleep(8)
                                    print("place bet 256")
                                    side = get_random_side()
                                    print(side)
                                    bet_256(side)
                                    time.sleep(13)

                                    while (get_balance() == balance):
                                        print("balance not updated")
                                        time.sleep(1)

                                    if (get_balance() < balance):
                                        balance = get_balance()
                                        time.sleep(8)
                                        print("place bet 512")
                                        side = get_random_side()
                                        print(side)
                                        bet_512(side)
                                        time.sleep(10)



