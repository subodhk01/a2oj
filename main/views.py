from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .ladder import div_a, div_b, div_c, div_d, div_e, div_1d, div_1e
import codeforces_api
import json
import requests
import logging

def home(request):
    try:
        handle = request.GET['handle']
        div = request.GET['div']
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
    else:
        return render(request, 'index.html' , {'msg': 'Invalid Division selected '})
    for step in division:
        for sub in submissions['result']:
            try:
                if int(step[2])==sub['problem']['contestId'] and step[3]==sub['problem']['index'] and sub['verdict']=="OK":
                    ladder.append([ step[0],sub['problem']['name'], sub['problem']['contestId'], sub['problem']['index'], True ])
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
    return render(request, 'ladder.html', {'ladder':ladder, 'division':div_head, 'handle': handle})

    