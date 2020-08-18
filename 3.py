from plyer import notification
import time

for i in range(5):
    notification.notify(
        title='通知だよ',
        message=str(i),
        app_name='アプリ名だよ',
        timeout=0.9
    #   app_icon='./icon.jpg'
    )
    time.sleep(1)