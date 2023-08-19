import requests, time, random

def change_bio(bio):
    token = "YOUR DISCORD TOKEN"
    headers = {
        "cookie": "",
        "Content-Type": "application/json",
        "Authorization": token
    }
    payload = {"custom_status": {"text": bio}}
    print(bio)
    res = requests.request("PATCH", "https://discord.com/api/v10/users/@me/settings", headers=headers, json=payload)
    return res.text

bio_list = ['YOUR', 'CHANGING', 'STATUS']

while True:
    for i in bio_list:
        change_bio(i)

        sleep = random.randint(2,10) #change it on your preference
        print(sleep)
        time.sleep(sleep)

    sleep2 = random.randint(10,23)
    print(sleep2)
    time.sleep(sleep2)
