ppl = int(input('Hoeveel mensen gaan er mee?'))
ppd = float(7.45)
vrtime = int(input('Hoeveel minuten gaan jullie op de vr?'))
vrprice = float(0.37)

totalprice = int((ppl*ppd)+((vrtime/5)*vrprice*ppl)*100)

print('Dit geweldige dagje-uit met',ppl,'mensen in de Speelhal met',vrtime,'minuten VR kost je maar', totalprice,'cent')