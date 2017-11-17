# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from mysite import models
from mysite.models import UserInfo
from mysite.core.ImageDiff import ImageDiff


def checkImage(request):
    imgageDiff = ImageDiff('C:\\Users\\Administrator.SKY-20170712YLK\\Desktop\\screen\\mmexport1510740255765.jpeg',
                           '1571200000', '12')
    return HttpResponse(
        imgageDiff.getEndCol(imgageDiff.agr2))


# 返回 字符串
def hello(request):
    return HttpResponse("Hello World!")


# 返回 html 模板
def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # 第一种添加数据到数据库方式
        # UserInfo.objects.create(user=username, pwd=password)
        # 第二种添加数据到数据库的方式
        user = UserInfo(user=username, pwd=password)
        user.save()

    user_list = models.UserInfo.objects.all()  # 从数据库 中查询 所有的数据
    return render(request, "success.html", {'data': user_list})

    # 一、 获取 数据库的数据


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    # list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = Test.objects.filter(id=1)

    # 获取单个对象
    # response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Test.objects.order_by('name')[0:2]

    # 数据排序
    # Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    # Test.objects.filter(name="runoob").order_by("id")


    #  二 、 更新数据

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # test1 = Test.objects.get(id=1)
    # test1.name = 'Google'
    # test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')


    # 三 、 删除数据

    # 删除id=1的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()
