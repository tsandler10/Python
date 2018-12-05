import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show = pg.prompt("What is your favorite show? ")

if show == "Impractical Jokers":
    pg.alert("What a great show!")
    points += 4
    wb.open("https://www.google.com/search?q=impractical+jokers&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjhiZW2443eAhWBc98KHXFHCw0Q_AUIECgD&biw=1366&bih=657#imgrc=TQtFIF0MCGlcTM")
elif show == "Modern Family":
    pg.alert("That show is excellent!")
    points += 3
    wb.open("https://www.google.com/search?q=modern+family&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiO0Jy-5Y3eAhVEh-AKHZIxARcQ_AUIDygC&biw=940&bih=647#imgrc=PUWHc3lcdTe3XM")
elif show == "The Flash":
    pg.alert("That is quite the show!")
    points += 1
    wb.open("https://www.google.com/search?q=the+flash&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwizrP_x5Y3eAhVpneAKHWCkDGgQ_AUIDygC&biw=940&bih=647#imgrc=XsoLnRF_7Z-otM")
elif show == "The Office":
    pg.alert("The Office is one of the best shows ever made!")
    points += 5
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=940&bih=647&tbm=isch&sa=1&ei=dFbHW9DxE8zN_AaG_pLgDg&q=michael+scott+memes&oq=michael+scott+memes&gs_l=img.1.0.0l3j0i30j0i5i30l5j0i8i30.1317.5101..6158...1.0..0.60.344.7......0....1..gws-wiz-img.......0i67j0i10i24.-wmz9eiJDDg#imgrc=T2zSpt-4XiAdUM")
elif show == "Arrow":
    pg.alert("Great show!")
    points += 7
    wb.open("https://www.google.com/search?q=arrow&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLg9LKt5_eAhVhiOAKHeR9BV8Q_AUIDygC&biw=924&bih=639#imgrc=OhJQ0-I4U83aNM:")
elif show == "Scrubs":
    pg.alert("That's such a funny show!")
    points += 9
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=924&bih=639&tbm=isch&sa=1&ei=q5XQW6CTEsi3gge60p3ABw&q=scrubs+show&oq=scrubs+sh&gs_l=img.1.0.0l10.1580.1962..3301...0.0..0.50.143.3......0....1..gws-wiz-img.......0i67.0VImaRDvV50#imgrc=hNjJgxaA7pK0SM:")
else:
    pg.alert("Your favorite show is " + str(show))
    points += 3
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiizL2g543eAhVknuAKHf4IDT4Q_AUIDigB&biw=940&bih=647#imgrc=_9iG3c3pqaIcTM")

t.sleep(4)
food = pg.prompt("What is your favorite food? ")
if food == "Pasta":
    pg.alert("Pasta is the best food ever!")
    points += 7
    wb.open("https://www.google.com/search?q=pasta+memes&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjQhtyo5I3eAhXkSt8KHTi9DO0Q_AUIDigB&biw=940&bih=647#imgrc=U-ulSv9Y3ZfVbM")
elif food == "Bean Enchiladas":
    pg.alert("Great Choice!")
    points += 4
    wb.open("https://www.google.com/search?q=bean+enchiladas&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiWwqfo543eAhVxS98KHd2wBaIQ_AUIDygC&biw=940&bih=647#imgrc=b2hDAojocFjV2M")
elif food == "Tacos":
    pg.alert("Tacos are so good!")
    points += 3
    wb.open("https://www.google.com/search?q=tacos&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ46yD6I3eAhUJmuAKHWoEAFEQ_AUIDygC&biw=940&bih=647#imgrc=7Ks07d4VnVKaAM")
elif food == "Stir Fry":
    pg.alert("Stir Fry is so flavorful!")
    points += 2
    wb.open("https://www.google.com/search?q=stir+fry&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiIs6iV6I3eAhXEY98KHbGWCz4Q_AUIDygC&biw=940&bih=647#imgrc=Ui5B1b5B8sRefM")
elif food == "Rice":
    pg.alert("I love rice!")
    points += 1
    wb.open("https://www.google.com/search?q=rice&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj88JvAtp_eAhVHT98KHX5sAMQQ_AUIDigB&biw=924&bih=639#imgrc=JdI--yoAa2VbTM:")
elif food == "Tortillas":
    pg.alert("Tortillas are so good!")
    points += 3
    wb.open("https://www.google.com/search?q=tortillas&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwinu6jotp_eAhWsnuAKHff0BCYQ_AUIDigB&biw=924&bih=639#imgrc=_rqMGrmtVuSc6M:")
else:
    pg.alert("Fascinating choice!")
    points += 1
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwicosSs6I3eAhWRnOAKHRbzDBkQ_AUIDigB&biw=940&bih=647#imgrc=_9iG3c3pqaIcTM")

t.sleep(4)
movie = pg.prompt("What is your favorite movie? ")
if movie == "The Martian":
    pg.alert("That's my favorite movie as well!")
    points += 9
    wb.open("https://www.google.com/search?q=the+martian&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj50KK86I3eAhVGm-AKHZvPDncQ_AUIECgD&biw=940&bih=647#imgrc=03iDzCqRiXnyXM")
elif movie == "Monsters University":
    pg.alert("That's an excellent movie!")
    points += 8
    wb.open("https://www.google.com/search?q=mike+wazowski&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjW-LWC5Y3eAhXRc98KHavwAL4Q_AUIDigB&biw=940&bih=647#imgrc=HnYvqmWaqzH-dM")
elif movie == "Jurassic Park":
    pg.alert("That's a classic!")
    points += 5
    wb.open("https://www.google.com/search?q=jurassic+park&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwipkNrW6I3eAhVpneAKHWCkDGgQ_AUIDigB&biw=940&bih=647#imgrc=dWudqIH4L1JHaM")
elif movie == "Kung Fu Panda":
    pg.alert("That movie is so funny!") 
    points += 4
    wb.open("https://www.google.com/search?q=kung+fu+panda&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_v6_r6I3eAhUEmuAKHfXIDB8Q_AUIDigB&biw=940&bih=647#imgrc=styCtT8ihPeKvM")
elif movie == "Grown Ups":
    pg.alert("That's a funny movie!")
    points += 2
    wb.open("https://www.google.com/search?q=grown+ups&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiNrIr_r5_eAhVFmuAKHdo8Ck8Q_AUIDigB&biw=1366&bih=657#imgrc=Yn45XYxpfHCqOM:")
elif movie == "Happy Gilmore":
    pg.alert("Best movie ever!")
    points += 10
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=924&bih=639&tbm=isch&sa=1&ei=BY7QW_PsFYGHggfWg4SoCg&q=happy+gilmore&oq=happy+gilmore&gs_l=img.3..0i67l2j0l6j0i67j0.42217.42217..42760...0.0..0.192.192.0j1......0....1..gws-wiz-img.1ZNYEFyPfP4#imgrc=C9URhk8V6H28OM:")         
else:
    pg.alert("That's a pretty good choice.")
    points += 2
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjiz4v66I3eAhUOT98KHaPHCb4Q_AUIDigB&biw=940&bih=647")

t.sleep(4)
country = pg.prompt("What is your favorite country? ")
if country == "The United States":
    pg.alert("That's my favorite country as well!")
    points += 9
    wb.open("https://www.google.com/search?q=USA&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiw3qf1_rDeAhXjRt8KHayrBcIQ_AUIECgD&biw=681&bih=647#imgrc=9Bi_WafFXFKx1M:")
elif country == "Mexico":
    pg.alert("That's an excellent country!")
    points += 8
    wb.open("https://www.google.com/search?q=mexico&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiNu9GP_7DeAhWmTt8KHXirByMQ_AUIECgD&biw=681&bih=647#imgrc=LEWjxDqHUy7nKM:")
elif country == "Cuba":
    pg.alert("That's a good choice!")
    points += 5
    wb.open("https://www.google.com/search?q=cuba&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiCl7ai_7DeAhVEheAKHRikBBQQ_AUIECgD&biw=681&bih=647#imgrc=ElSVAmf1Ky3KjM:")
elif country == "England":
    pg.alert("Such a beautiful country!")
    points += 4
    wb.open("https://www.google.com/search?q=england&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiz0Oq-_7DeAhVng-AKHTHhAqUQ_AUIECgD&biw=681&bih=647#imgrc=aRPeM68eGlEDbM:")
elif country == "Poland":
    pg.alert("That's an iteresting country!")
    points += 2
    wb.open("https://www.google.com/search?q=poland&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRxuLb_7DeAhUFVd8KHT9kC-0Q_AUIECgD&biw=681&bih=647#imgrc=eSXgbtn-jHnNzM:")
elif country == "Philippines":
    pg.alert("I want to go there someday!")
    points += 10
    wb.open("https://www.google.com/search?q=philippines&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjm9Kjy_7DeAhVtk-AKHZuuDlwQ_AUIECgD&biw=681&bih=647#imgrc=Ia5jHn4tK14WwM:")         
else:
    pg.alert("That's a pretty good choice.")
    points += 2
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjiz4v66I3eAhUOT98KHaPHCb4Q_AUIDigB&biw=940&bih=647")

t.sleep(4)
soup = pg.prompt("What is your favorite soup ")
if soup == "Brocolli Cheddar":
    pg.alert("That's my favorite soup as well!")
    points += 15
    wb.open("https://www.google.com/search?q=broccoli+cheddar&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiY7d2cuJ_eAhUNm-AKHYFuAlwQ_AUIDygC&biw=924&bih=639#imgrc=8kyl_fDTIDOGUM:")
elif soup == "Tomato Soup":
    pg.alert("That goes well with grilled cheese!")
    points += 8
    wb.open("https://www.google.com/search?q=tomato+soup&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwil3Ye5uJ_eAhUOSN8KHdwEDsYQ_AUIDygC&biw=924&bih=639#imgrc=5HSDqZLvZFuQaM:")
elif soup == "Chicken Soup":
    pg.alert("That's a classic!")
    points += 7
    wb.open("https://www.google.com/search?q=chicken+soup&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj8v8XQuJ_eAhUwWN8KHbj6DOsQ_AUIDigB&biw=924&bih=639#imgrc=N9ghu-9LLPfU3M:")
elif soup == "Turkey Chili":
    pg.alert("I love that soup!")
    points += 4
    wb.open("https://www.google.com/search?q=kung+fu+panda&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_v6_r6I3eAhUEmuAKHfXIDB8Q_AUIDigB&biw=940&bih=647#imgrc=styCtT8ihPeKvM")
elif soup == "Clam Chowder":
    pg.alert("Great Choice!")
    points += 2
    wb.open("https://www.google.com/search?q=clam+chowder&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwij79TpuJ_eAhUlh-AKHehYBKIQ_AUIDygC&biw=924&bih=639#imgrc=fTCNec1qD6czhM:")
elif soup == "Pasta Fagioli":
    pg.alert("Not my favorite but I respect it")
    points += 2
    wb.open("https://www.google.com/search?q=pasta+fagioli&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLpt6EuZ_eAhULJt8KHbREDyIQ_AUIDygC&biw=924&bih=639#imgrc=ovSvgOqZHcH7LM:")         
else:
    pg.alert("That's a pretty good choice.")
    points += 2
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjiz4v66I3eAhUOT98KHaPHCb4Q_AUIDigB&biw=940&bih=647")

t.sleep(4)
sport = pg.prompt("What is your favorite sport ")
if sport == "Lacrosse":
    pg.alert("That's my favorite sport as well!")
    points += 15
    wb.open("https://www.google.com/search?q=lacrosse&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiu8_yYuZ_eAhVyk-AKHT6jAPkQ_AUIDigB&biw=924&bih=639#imgrc=PHLcEZN_N-hF9M:")
elif sport == "Soccer":
    pg.alert("That's a great sport!")
    points += 8
    wb.open("https://www.google.com/search?q=soccer&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjWgvy8uZ_eAhUKTN8KHdzNCpoQ_AUIDygC&biw=924&bih=639#imgrc=oZXZ4C8lSXAfIM:")
elif sport == "Football":
    pg.alert("That'a fantastic sport!")
    points += 7
    wb.open("https://www.google.com/search?q=football&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiU4rLTuZ_eAhWyTd8KHXHjC-UQ_AUIDigB&biw=924&bih=639#imgrc=66Naev1XqGjl5M:")
elif sport == "Baseball":
    pg.alert("That's an American classic!")
    points += 4
    wb.open("https://www.google.com/search?q=baseball&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiY2YbnuZ_eAhViRN8KHRNVCfgQ_AUIDigB&biw=924&bih=639#imgrc=3IAxBYE45qSLGM:")
elif sport == "Golf":
    pg.alert("Great Choice!")
    points += 2
    wb.open("https://www.google.com/search?q=golf&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiPu9L9uZ_eAhXvQ98KHemlAb0Q_AUIECgD&biw=924&bih=639#imgrc=DNrJb9S8LZM9mM:")
elif sport == "Tennis":
    pg.alert("Not my favorite but I respect it")
    points += 2
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US774&biw=924&bih=639&tbm=isch&sa=1&ei=BY7QW_PsFYGHggfWg4SoCg&q=happy+gilmore&oq=happy+gilmore&gs_l=img.3..0i67l2j0l6j0i67j0.42217.42217..42760...0.0..0.192.192.0j1......0....1..gws-wiz-img.1ZNYEFyPfP4#imgrc=C9URhk8V6H28OM:")         
else:
    pg.alert("That's a pretty good choice.")
    points += 2
    wb.open("https://www.google.com/search?q=smiley+face&rlz=1C1GCEA_enUS752US774&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjiz4v66I3eAhUOT98KHaPHCb4Q_AUIDigB&biw=940&bih=647")





pg.alert(points)

