from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from api.models import Question


class QuestionView(View):
    def get(self,request, id=None):
        questions = Question.objects.all()
        return render(request,'api/view_question.html',{'questions':questions})
    def post(self,request):
        question_text = request.POST.get('question_text')
        time_pub = request.POST.get('time_pub')
        if not question_text or not time_pub:
            return JsonResponse({'status':'error'})
        question = Question.objects.create(question_text=question_text,time_pub=time_pub)
        question.save()
        questions = Question.objects.all()
        return render(request, 'api/view_question.html',{'questions':questions})

    def delete(self,request, id):
        # question = Question.objects.get(id=id)
        # question.delete()
        return JsonResponse({'status':'success'})

# class QuestionListView(View):
#     def get(self,request):
#         questions = Question.objects.all()
#         return render(request,'api/list_question.html',{'questions':questions})
#     def post(self,request):
#         return render(request,'api/list_question.html')

