# o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
# de fiecare data cand adaugam o pagina noua in proiect ea va trebui
# adaugata si in context
# before_all = nume de metoda standardizat care da informatii ca acele
# instructiuni trebie executate inainte de executarea unui scenariu


from pages.sign_in_page import Sign_In_Page
from browser import Browser
from pages.forgot_pasword_page import Forgot_Pwd_Page


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_In_Page()
    context.forgot_pass = Forgot_Pwd_Page()
    # context.sign_up_page = SignUpPage()


def after_all(context):
    context.browser.close()
