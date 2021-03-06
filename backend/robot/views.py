from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import utils


# Create your views here.

def index(request):
    return render(request,"index.html")

@csrf_exempt
def msgAsk(request):
    # 文字问答的处理程序
    json = {"code": 0, "data": {"answer": ""}, "msg": ""}
    answer = None
    if(request.method == 'GET'):
        json['code'] = 400
        json['msg'] = "ERROR:请求方式错误"

    elif(request.method == 'POST'):
        json['code'] = 200
        json['msg'] = "SUCCESS"

        try:
            # 主要的语言处理函数
            question = username = request.POST.get('question')
            if question == None:
                question = "No msg"

            # answer 为回复
            answer = utils.chatterBotRepeat(question)

            if answer == 0:
                answer = utils.myChatterBotRepeat(question)
                answer = str(answer)
            if answer == '0':
                answer = utils.get_default_answer()

        except Exception as ex:
            question = ex.message
        
        json["data"]['answer'] = answer
    else:
        json['code'] = 404
        json['msg'] = "FAILD:未执行功能"
    response = JsonResponse(json)
    response['Access-Control-Allow-Origin'] = '*'
    return response

@csrf_exempt
def voiceToWord(request):
    # pcm语音文件转文字返回
    json = {"code": 0, "data": {"answer": ""}, "msg": ""}
    answer = None
    if(request.method == 'GET'):
        json['code'] = 400
        json['msg'] = "ERROR:请求方式错误"

    elif(request.method == 'POST'):
        json['code'] = 200
        json['msg'] = "SUCCESS"

        try:
            # 主PCM处理函数

            data = request.body

            if(data!=None):
                answer = utils.voiceToWord(data)
            else:
                # answer 为回复
                answer = "No data"

        except Exception as ex:
            question = ex.message
        
        json["data"]['answer'] = answer
    else:
        json['code'] = 404
        json['msg'] = "FAILD:未执行功能"
    response = JsonResponse(json)
    response['Access-Control-Allow-Origin'] = '*'
    return response