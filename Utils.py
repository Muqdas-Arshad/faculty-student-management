from View import View
from Controller import Controller
while True:
    try:
       new=View()
       new.display_menu()
    except Exception as e:
        print(str(e))
