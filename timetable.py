import threading

# The requests library is the standard for making HTTP requests in Python.
import requests
from bs4 import BeautifulSoup
import sendmail

import datetime
com_ar = ['Y'];
op_ar = ["d","f","g"]
in_ar = [1,2,3]

ap = [];
pa = [];
space = "      "

add_on = "---------------------------------------------------------------------------"


input = int(input("enter 1 for BFM 2 for SPM and 3 for DA: "))
if (input >= 1 and input <= 3):
    if input == in_ar[input-1]:
        com_ar.append(op_ar[input-1]);
        #option = com_ar[input-1];
        current_time = datetime.datetime.now()
        print("Year : ", end="")
        print(current_time.year)
        print("Month : ", end="")
        print(current_time.month)
        print("Day : ", end="")
        print(current_time.day)
        print(current_time)

cookies = {
    'MRBS_SESSID': 'tu5encpbetl033sd65tn8u7ob7',
}

headers = {
    'Host': 'time-table.sicsr.ac.in',
    'Content-Length': '20',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://time-table.sicsr.ac.in',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://time-table.sicsr.ac.in/day.php?year=2022&month=2&day=9&area=1&room=29',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

params = (
    ('year', current_time.year ),
    ('month', current_time.month),
    ('day', "2"),
    ('area', '1'),
    ('room', '29'),
)
msg = ["COMMON LECTURES", "SPECIALIZAION LECTURES"]
# option.append()
# option1 = ['Y']
# print("COMMON LECTURES")
count = 0
for x in com_ar:

    print(msg[count])

    data = 'type='+ x +'&submit=Submit'

    res = requests.post('http://time-table.sicsr.ac.in/day.php', headers=headers, params=params, cookies=cookies, data=data, verify=False)


    soup = BeautifulSoup(res.text, features="html.parser")

    for match in soup.find_all("div", class_="celldiv slots2"):
        result = match.a.text
        link = match.a
        data = {"content": add_on}
        # +" response"+ str(len(headline))}
        webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
        web_req = requests.post(webhook, data=data)
        data_re = {"content": str(result)}
        # +" response"+ str(len(headline))}
        webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
        web_req = requests.post(webhook, data=data_re)


        print(add_on)
        print(result)

        ap.append(result)
    # if not ap:
    #     no_lec = "No Lecture"
    #     data_no = {"content":msg[count] + space + no_lec}
    #     # +" response"+ str(len(headline))}
    #     webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
    #     web_req = requests.post(webhook, data=data_no)
    #
    # else:
    #     print()

        #main_link = link.get('values')
        main_li = link.get('href');
        #print(link.get('href'))
        #time get req

        # time_req = requests.get("http://time-table.sicsr.ac.in/"+main_link, headers=headers, params=params, cookies=cookies, verify=False)
        # soup1 = BeautifulSoup(time_req, features="html.parser")
        # print(soup1.text)
        # print("http://time-table.sicsr.ac.in/".link)
        # print()

        cookies1 = {
            '_gcl_au': '1.1.908835025.1651383882',
            '_ga': 'GA1.3.792130240.1651383883',
            '_fbp': 'fb.2.1651383882721.1840833001',
            '_uetvid': 'cc974470c91111eca0f7d3d1e41bce97',
            'MRBS_SESSID': 'ktigsqmk20e8312nt4kp3kcuc2',
        }

        headers1 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,haw;q=0.7,mr;q=0.6,la;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'http://time-table.sicsr.ac.in/day.php?year=2022&month=06&day=03&area=1&room=29',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
        }

        params1 = (
            ('id', '165826'),
            ('area', '1'),
            ('day', '3'),
            ('month', '6'),
            ('year', '2022'),
        )
        response = requests.get('http://time-table.sicsr.ac.in/'+str(main_li), headers=headers1,
                                cookies=cookies1, verify=False)
        li = [5, 7, 11, 9]
        y = ["Room", "Start Time and Date", "End Time and Date", "Duration"]

        soup = BeautifulSoup(response.text, features="html.parser")
        #print(soup)
        for match in soup.find_all("tr"):
            td = match.find_all("td")
            #print(td)

        td = soup.find_all("td")

        count1 = 0
        for x in li:
            print(y[count1] + ": " + td[x].text)
            pa.append(y[count1] + ": " + td[x].text)
            data_detail = {"content": y[count1] + ":" + str(td[x].text)}
            # +" response"+ str(len(headline))}
            webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
            web_req = requests.post(webhook, data=data_detail)

            count1 += 1

        print()

    count += 1
# discord = str(result) +":"+str(td[x].text)
# print(discord)
    # data1 = {"content": discord}
    # # +" response"+ str(len(headline))}
    # webhook1 = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
    # web_req1 = requests.post(webhook, data=data1)

# for lec_name in ap:
#     print(lec_name)
#     data_main = lec_name
#     for detail in pa:
#         print(detail)
        # time_count = 0
        # while time_count <= 3:
        #     print(pa[time_count])
        #     time_count = time_count +1

# data = {"content": )}
#             # +" response"+ str(len(headline))}
# webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
# web_req = requests.post(webhook, data=data)

# print();
# print();
# print(ap);
# print(pa);



sendmail.smtp(ap,pa);















#
#
#
#
#
#

# headline = match.a.text2
# print(headline)
# if headline == "none":
#     print("no lex");
# print(match.prettify());
# print(match.a)

# if "Pavandeepsingh" in soup.text:
#     print("y")
#     data = {"content": headline}
#     # +" response"+ str(len(headline))}
#     webhook = "https://discord.com/api/webhooks/922738749291499531/BevRpknW4f5PLHeeAVvg1rPo3PZ40s-02VmthQmv7rwOrtEvxU288Ef-hni6xfJZZU2n";
#     web_req = requests.post(webhook, data=data)
#     print(len(res.text));
# else:
#     print("n")