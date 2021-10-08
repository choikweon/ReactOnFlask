from flask import render_template
import requests
import json

def send_email_test():
    subject="T subject here"
    sender="t_sender@example.com"
    recipients=["kweon.choi@vuno.co"]
    text_body="mail test, text body texttexttext not html"
    html_body="mail test, html body htmlhtmlhtml not text"
    jdata={}
    jdata['subject']=subject
    jdata['sender']=sender
    jdata['recipients']=recipients
    jdata['text_body']=text_body
    jdata['html_body']=html_body
    jdump=json.dumps(jdata)
    requests.post('http://email:5001/', data=jdump)
    return "test email sent"


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    subject='[Microblog] Reset Your Password'
    sender=app.config['ADMINS'][0]
    recipients=[user.email]
    text_body=render_template('email/reset_password.txt', user=user, token=token)
    html_body=render_template('email/reset_password.html', user=user, token=token)
    jdata={}
    jdata['subject']=subject
    jdata['sender']=sender
    jdata['recipients']=recipients
    jdata['text_body']=text_body
    jdata['html_body']=html_body
    jdump=json.dumps(jdata)
    requests.post('http://email:5001/', data=jdump)
    '''
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

    '''