from django.shortcuts import render
from appCreditoBanco.Logica import modeloSNN #para utilizar el método inteligente
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

class Clasificacion():
    def determinarAprobacion(request):
        return render(request, "aprobacioncreditos.html")
    @api_view(['GET','POST'])
    def predecir(request):
        try:
            #Formato de datos de entrada
            age     =   int(request.POST.get('age'))
            job		=	request.POST.get('job')
            marital	=	request.POST.get('marital')
            education=	request.POST.get('education')
            default	=	request.POST.get('default')
            balance	=	int(request.POST.get('balance'))
            housing	=	request.POST.get('housing')
            loan	=	request.POST.get('loan')
            contact	=	request.POST.get('contact')
            day		=	int(request.POST.get('day'))
            month	=	request.POST.get('month')
            duration=	int(request.POST.get('duration'))
            campaign=	int(request.POST.get('campaign'))
            pdays	=	int(request.POST.get('pdays'))
            previous=	int(request.POST.get('previous'))
            poutcome=	request.POST.get('poutcome')
            #Consumo de la lógica para predecir si se llama o no al cliente
            resul=modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN,age=age,job=job,marital=marital,education=education,default=default,balance=balance,housing=housing,loan=loan,
                                                            contact=contact,day=day,month=month,duration=duration,campaign=campaign,pdays=pdays,previous=previous,poutcome=poutcome)
        except:
            resul='Datos inválidos'
        return render(request, "informe.html",{"e":resul})
    
    @csrf_exempt
    @api_view(['GET','POST'])
    def predecirIOJson(request):
        print(request)
        print('***')
        print(request.body)
        print('***')
        body = json.loads(request.body.decode('utf-8'))
        #Formato de datos de entrada
        age     =   int(request.POST.get('age'))
        job		=	body.get('job')
        marital	=	body.get('marital')
        education=	body.get('education')
        default	=	body.get('default')
        balance	=	int(body.get('balance'))
        housing	=	body.get('housing')
        loan	=	body.get('loan')
        contact	=	body.get('contact')
        day		=	int(body.get('day'))
        month	=	body.get('month')
        duration=	int(body.get('duration'))
        campaign=	int(body.get('campaign'))
        pdays	=	int(body.get('pdays'))
        previous=	int(body.get('previous'))
        poutcome=	body.get('poutcome')
        resul=modeloSNN.modeloSNN.predecirNuevoCliente(modeloSNN.modeloSNN,age=age,job=job,marital=marital,education=education,default=default,balance=balance,housing=housing,loan=loan,
                                                            contact=contact,day=day,month=month,duration=duration,campaign=campaign,pdays=pdays,previous=previous,poutcome=poutcome)
        data = {'result': resul}
        resp=JsonResponse(data)
        resp['Access-Control-Allow-Origin'] = '*'
        return resp