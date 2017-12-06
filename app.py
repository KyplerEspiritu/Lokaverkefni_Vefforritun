#Kypler L. Espiritu
#Lokaverkefni - Forritun
#22.11.17


from bottle import *
from ftfy import fix_encoding
import pymysql

db = pymysql.connect(host="tsuts.tskoli.is",
                     user="2910003120",
                     passwd="kypler00",
                     db="2910003120_vef2lokaverk",
                     charset="utf8",
                     use_unicode=True)


cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS USER(username varchar(32) PRIMARY KEY, password varchar(32))')
cur.execute('CREATE TABLE IF NOT EXISTS ORDERS(Username varchar(32), texti varchar(500) NOT NULL)')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def sign_in():
    try:
        cur.execute('SELECT * FROM USER')
        users = cur.fetchall()

        notenda_listi = []
        for i, x in users:
            notenda_listi.append([i, x])

        if len(notenda_listi) == 0:
            cur.execute('INSERT INTO USER VALUES("kypler", "admin")')

        return template('sign_in.tpl')
    except pymysql.InterfaceError:
        pass

@route('/', method='POST')
def sign_in_info():

    cur.execute('SELECT * FROM USER')
    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    global signinUser
    signinUser = request.forms.get('SignIn_username')
    signinPass = request.forms.get('SignIn_password')

    signIn = list((signinUser, signinPass))

    for notandanafn, lykilord in notenda_listi:
        if signIn[0] == notandanafn and signIn[1] == lykilord:
            redirect('/heimasida')
            break
    else:
        return template('sign_in_error.tpl', message="Innskráning hefur ekki staðist")


@route('/signup')
def sign_up():
    return template('sign_up.tpl')

@route('/signup', method="POST")
def sign_up_info():
    cur.execute('SELECT * FROM USER')
    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    signupUser = request.forms.get('SignUp_username')
    signUpPass = request.forms.get('SignUp_password')

    signUp = list((signupUser, signUpPass))

    for notendanafn, lykilord in notenda_listi:
        if signUp[0] != notendanafn:
            cur.execute('INSERT INTO USER VALUES(%s, %s)', (signupUser, signUpPass))
            db.commit()
            return template('sign_up_message', message="Nýskráning hefur staðist")
        else:
            return template('sign_up_message', message="Nýskráning hefur ekki staðist")

@route('/heimasida')
def heimasida():

    return template('heimasida.tpl')

@route('/panta')
def panta():
    return template('pizza_panta.tpl')

@route('/panta', method="POST")
def panta_info():
    texti = request.forms.get('comment')

    try:
        cur.execute('INSERT INTO ORDERS VALUES(%s, %s)', (signinUser, texti))
        db.commit()
    except (pymysql.IntegrityError):
        pass
    redirect('/heimasida')

@route('/minar')
def minar_sidur():
    cur.execute('SELECT * FROM ORDERS WHERE USERNAME = %s', (signinUser))
    orders = cur.fetchall()

    listi = []
    for i, x in orders:
        listi.append([i, fix_encoding(x.encode('latin-1').decode('utf-8'))])

    return template('minar_sidur.tpl', data=listi, nafn=signinUser)



run(host='localhost', port=8080, reloader=True, debug=True)