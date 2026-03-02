#Modulos que se usaran
import requests #Para entender solicitudes
import json #Para reconocer el formato json
from tabulate import * #Para crear tablas
from constants import API_BASE_URL, API_USERNAME, API_PASSWORD

# Llamada al API por el ticket
headers = {"Content-Type": "application/json"} #Headers
data = json.dumps({"username": API_USERNAME, "password": API_PASSWORD}) #Credenciales
resp = requests.post(API_BASE_URL+"/ticket", data=data, headers=headers) #URL especifica

print("Status de Solicitud:")
print(resp.status_code)
result = resp.json()
# print(result)

ticket = result["response"]["serviceTicket"] #Printing ticket
print("\nEl Service Ticket es:")
print(ticket)


# Llamada al API para recibir los dispositivos de red
headers = {"X-Auth-Token": ticket}
resp = requests.get(API_BASE_URL+"/network-device", headers=headers) #URL especifica

# print (resp.status_code)
result = resp.json()
#print (json.dumps(result, indent=4))
print("\nDispositivos de Red:")
host_list=[]
i=0
for item in result["response"]:
    i+=1
    host_list.append([i,item["hostname"],item["serialNumber"],item["softwareVersion"]])
    #print(item["hostname"]+" "+item["serialNumber"]+" "+item["softwareVersion"]) #Lista completa

print(tabulate(host_list,headers=["Hostname","Serial Number","Software Version"],tablefmt='rst')) #Tabla ordenada

# Llamada al API para recibir los host
headers = {"X-Auth-Token": ticket }
resp = requests.get(API_BASE_URL+"/host", headers=headers) #URL especifica

# print (resp.status_code)
result = resp.json()
#print (json.dumps(result, indent=4))
print("\nHosts de la Red:")
host_list=[]
i=0
for item in result["response"]:
    i+=1
    host_list.append([i,item["hostName"],item["hostType"],item["hostIp"]])
    #print(item["hostName"]+" "+item["hostType"]+" "+item["hostIp"]) #Lista completa

print(tabulate(host_list,headers=["Hostname","Tipo","IP"],tablefmt='rst')) #Tabla ordenada
