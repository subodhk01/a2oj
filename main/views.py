from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .ladder import div_a, div_b, div_c, div_d, div_e, div_1d, div_1e, rating_1, rating_2, rating_3, rating_4, rating_5, rating_6, rating_7, rating_8, rating_9, rating_10, rating_11
import codeforces_api
import json
import requests
import logging
def home(request):
    try:
        handle = request.GET['handle']
        div = request.GET['div']
        rating = request.GET['rating']
        #print(div)
    except:
        return render(request, 'index.html')
    parser = codeforces_api.CodeforcesApi()
    try:
        submissions = parser.user_status(handle=handle)
    except:
        return render(request, 'index.html' , {'msg': 'Invalid Codeforces handle '})
    ladder = []
    division = []
    div = int(div)
    rating = int(rating)
    div_head = ""
    if div==1:
        division = div_a
        div_head = "DIV 2.A"
    elif div==2:
        division = div_b
        div_head = "DIV 2.B"
    elif div==3:
        division = div_c
        div_head = "DIV 2.C"
    elif div==4:
        division = div_d
        div_head = "DIV 2.D"
    elif div==5:
        division = div_e
        div_head = "DIV 2.E"
    elif div==6:
        division = div_1d
        div_head = "DIV 1.D"
    elif div==7:
        division = div_1e
        div_head = "DIV 1.E"
    elif rating==1:
        division = rating_1
        div_head = "Codeforces Rating < 1300"
    elif rating==2:
        division = rating_2
        div_head = "1300 <= Codeforces Rating <= 1399"
    elif rating==3:
        division = rating_3
        div_head = "1400 <= Codeforces Rating <= 1499"
    elif rating==4:
        division = rating_4
        div_head = "1500 <= Codeforces Rating <= 1599"
    elif rating==5:
        division = rating_5
        div_head = "1600 <= Codeforces Rating <= 1699"
    elif rating==6:
        division = rating_6
        div_head = "1700 <= Codeforces Rating <= 1799"
    elif rating==7:
        division = rating_7
        div_head = "1800 <= Codeforces Rating <= 1899"
    elif rating==8:
        division = rating_8
        div_head = "1900 <= Codeforces Rating <= 1999"
    elif rating==9:
        division = rating_9
        div_head = "2000 <= Codeforces Rating <= 2099"
    elif rating==10:
        division = rating_10
        div_head = "2100 <= Codeforces Rating <= 2199"
    elif rating==11:
        division = rating_11
        div_head = "Codeforces Rating >= 2200"
    else:
        return render(request, 'index.html' , {'msg': 'Invalid Division selected '})
    solved = 0
    for step in division:
        for sub in submissions:
            try:
                if int(step[2])==sub.problem.contest_id and step[3]==sub.problem.index and sub.verdict=="OK":
                    ladder.append([ step[0],sub.problem.name, sub.problem.contest_id, sub.problem.index, True ])
                    solved = solved + 1
                    break
            except:
                pass
        else:
            ladder.append([ step[0],step[1], step[2], step[3], False ])
    # for step in ladder:
    #     for x in step:
    #         print(x,)
    #     print("\n")
    try:
        logging.basicConfig(filename='handle.log',level=logging.INFO)
        logging.info(handle)
        #r = requests.get('http://kyukey-lock.herokuapp.com/a2oj/'+ handle)
    except:
        print("Error in logging")
    return render(request, 'ladder.html', {'ladder':ladder, 'division':div_head, 'handle': handle, 'solved':solved})