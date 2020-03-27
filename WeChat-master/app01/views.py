from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
def send(request):
    """
    发送消息
    :param request:
    :return:
    """
    return render(request, 'send.html', locals())
def send_msg(request):
    """
    发送消息
    :param request:
    :return:
    """
    import json
    import requests
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": settings.WECHAT_PUBLIC.get('appid'),
            "secret": settings.WECHAT_PUBLIC.get('secret'),
        }
    )
    access_token = r1.json().get('access_token')
    body = {
        "touser": 'o-KVCxIFr71XVsEuOWnc7dylCtPA',
        "template_id": '0qPNmbDHa0FtwkBPwnV63U33eJw_-1tRosPlNzVkZmw',
        "data": {
            "value1": {
                "value": "vip",
                "color": "#173177"
            },
            "date": {
                "value": str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)+' '+str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second),
                "color": "#173177"
            },
            "mon": {
                "value": '￥ 299999',
                "color": "#173177"
            },
            "mon1": {
                "value": '￥ 233',
                "color": "#173177"
            },
            "mon2": {
                "value": '￥ 466',
                "color": "#173177"
            }
        }
    }

    r2 = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            'access_token': access_token
        },
        data=json.dumps(body)
    )
    print(r2.text)
    return HttpResponse('微信发送成功')

def send_email_msg(request):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    # ahqeqnmoptsliajj
    sender = '0@qq.com'  # 自己邮箱
    receiver = '9@qq.com'  # 接收者邮箱
    message = MIMEText('test ---------test')
    message['From'] = Header('量化交易', 'utf-8')
    message['To'] = Header('接收', 'utf-8')
    subject = '量化交易提醒'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect('smtp.qq.com', 25)
        smtpobj.login('0@qq.com', 'optsliajj')#发送人邮箱，后面为申请的授权码
        smtpobj.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功')
        return HttpResponse('发送成功')
    except smtplib.SMTPException as e:
        print(e, '发送失败')
        return HttpResponse('发送失败')