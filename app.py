from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Tina Li! This is my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    message = "You entered your favorite course as: {} {}".format(subject, course_number)
    print(message)

    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html',form_submitted=True)
    else:
        return render_template('contact.html')
    return render_template('contact.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()