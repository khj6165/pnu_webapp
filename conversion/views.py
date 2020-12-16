from django.shortcuts import render
import json
import re

# Create your views here.
def jtop(request):
    return render(request, 'conversion/jtop.html')

def ptoj(request):
    return render(request, 'conversion/ptoj.html')

def presult(request):
    if request.method =="POST":
        jibun = request.POST.get('jibun')
        parse_jibun = jibun.split()
        jibun_num = parse_jibun.pop()

        #지목코드
        if(jibun_num[0]=='산'):
            jimok = '2'
        else:
            jimok = '1'

        #본번부번코드
        jibun_num = re.findall('\d+', jibun_num)
        num1 = jibun_num[0].zfill(4)
        if len(jibun_num)==1:
            num2 = '0000'
        else:
            num2 = jibun_num[1].zfill(4)

        #문자열 파싱
        search_list = ['','','','']
        flag = 0
        for i in range(len(parse_jibun)):
            if parse_jibun[i][-1] =='도':
                search_list[0] = parse_jibun[i]
                flag = 1
            elif parse_jibun[i][-1] =='시':
                if flag == 1:
                    search_list[1] = parse_jibun[i]
                else:
                    search_list[0] = parse_jibun[i]
            elif parse_jibun[i][-1]=='군' or parse_jibun[i][-1]=='구':
                if search_list[1]=='':
                    search_list[1] = parse_jibun[i]
                else:
                    search_list[1] = search_list[1] + " " + parse_jibun[i]
            elif parse_jibun[i][-1]=='읍' or parse_jibun[i][-1]=='면' or parse_jibun[i][-1]=='동' or parse_jibun[i][-1]=='가':
                search_list[2] = parse_jibun[i]
            elif parse_jibun[i][-1]=='리':# 여기에 동이 들어가는 case가 있는지 알아보기
                search_list[3] = parse_jibun[i]

        #법정동코드
        result = ""
        with open('bcode.json', "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            for i in json_data:
                if i['시도명']==search_list[0] and i['시군구명']==search_list[1] and i['읍면동명']==search_list[2] and i['동리명']==search_list[3]:
                    result = str(i['법정동코드'])

        result = result+jimok+num1+num2
        return render(request, 'conversion/presult.html', {'pnu':result, 'jibun':jibun})

def jresult(request):
    #if request.method =="POST":
    #시도 2자리 11-서울, 26-부산, 27-대구, 28-인천, 29-광주, 30-대전, 31-울산, 36-세종, 41-경기, 42-강원, 43-충북, 44-충남, 45-전북, 46-전남, 47-경북, 48-경남, 50-제주   
    return render(request, 'conversion/jresult.html')