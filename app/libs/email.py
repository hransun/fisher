from threading import Thread
from flask import current_app, render_template
from flask_mail import Message,Mail

mail = Mail()


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=app.config['MAIL_USERNAME'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def _send_email():
    msg = Message('test mail', sender='hransun2020@gmail.com', body='test',recipients=['hransun2020@gmail.com'])
    mail.send(msg)
    pass




