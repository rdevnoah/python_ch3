from django.db.models import Max, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    return render(request, 'helloworld/hello.html')


def counter_update(request):
    # groupno = 1 이고, orderno >= 2 인 게시물의 orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    # 여러번 update가 일어나야 할 때, 멍청하게 save()를 여러번 호출하지 마라.
    # model에는 update()도 지원해주고, 매개변수로 F() 객체도 지원한다.
    results = Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)

    return HttpResponse('ok')



def counter_add(request):
    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 1
    c.save();

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save();

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save();

    return HttpResponse('OK')


def counter_max(request):
    value = Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno = 0 if value["max_groupno"] is None else value["max_groupno"]
    return HttpResponse(f'max groupno:{max_groupno}')