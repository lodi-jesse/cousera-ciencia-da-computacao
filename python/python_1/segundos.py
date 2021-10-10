segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = segundos // 86400
restoDia = segundos % 86400
horas = restoDia // 3600
restoHora = restoDia % 3600
minuto = restoHora // 60
restoSegundos = restoHora % 60

print(f"{dia} dias, {horas} horas, {minuto} minutos e {restoSegundos} segundos.")