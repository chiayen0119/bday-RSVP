import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_DEFAULT_SENDER='admin',
    MAIL_MAX_EMAILS=10,
    MAIL_USERNAME='wjy880119@gmail.com',
    MAIL_PASSWORD='fgdpidyoajyjfkvn'
)

mail = Mail(app)

# 存储活动信息的简单数据结构
events = [
    {"id": 1, "title": "Party on Aug 24th", "details": "Join us for a fun birthday party!", "date": "Aug 24th Saturday", "time": "7:00pm", "location": "Location 1"},
    {"id": 2, "title": "Party on Aug 25th", "details": "Join us for a fun birthday party!", "date": "Aug 25th Sunday", "time": "8:00pm", "location": "Location 2"},
    {"id": 3, "title": "Party on Aug 26th", "details": "Join us for a fun birthday party!", "date": "Aug 26th Monday", "time": "6:00pm", "location": "Location 3"}
]

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/rsvp/<int:event_id>', methods=['GET', 'POST'])
def rsvp(event_id):
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None:
        return "Event not found", 404

    if request.method == 'POST':
        # 当用户提交表单时，我们会收到所有信息
        name = request.form['name']
        dietary_restrictions = request.form.get('dietary_restrictions', '')
        message = request.form.get('message', '')
        part1 = request.form.get('part1')
        part2 = request.form.get('part2')
        part3 = request.form.get('part3')
        afterparty_idea = request.form.get('afterparty_idea', '')

        rsvp_info = {
            "event_id": event_id,
            "name": name,
            "dietary_restrictions": dietary_restrictions,
            "message": message,
            "part1": part1,
            "part2": part2,
            "part3": part3,
            "afterparty_idea": afterparty_idea
        }
        send_rsvp_email(rsvp_info)
        return redirect(url_for('thank_you'))

    return render_template('rsvp.html', event=event)



def send_rsvp_email(rsvp_info):
    msg = Message(f'New RSVP for Birthday Party on August 25th',
                  sender=("admin", 'wjy880119@gmail.com'),
                  recipients=['wjy880119@gmail.com'])
    msg.body = (f"Name: {rsvp_info['name']}\n"
                f"Dietary Restrictions: {rsvp_info['dietary_restrictions']}\n"
                f"Message: {rsvp_info['message']}\n"
                f"Part 1: {rsvp_info['part1']}\n"
                f"Part 2: {rsvp_info['part2']}\n"
                f"Part 3: {rsvp_info['part3']}\n"
                f"Afterparty Idea: {rsvp_info['afterparty_idea']}")
    mail.send(msg)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Heroku provides the port via环境变量
    app.run(host='0.0.0.0', port=port)
