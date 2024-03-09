###################################################
# 1. Librerias
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
import os
from Funciones import gather_user_data, gather_reservation_data, gather_medical_reason, not_talk
###################################################
# 2. Cargar variables entorno
load_dotenv();
openai_key= os.getenv("OPENAI_KEY");
#print(openai_key)
###################################################
# 3. Crear el cliente (permite la conexión con OPENAI)
client=OpenAI(api_key= "sk-XXXXXXXXXX",);
###################################################
# 4. Crear el asistente
assistant = client.beta.assistants.create(
    name = "Sabino Bot",
    instructions="No hagas supuestos acerca de los valores a utilizar en las funciones. Eres un aisstente que permite agendar una cita medica en el Hospital Bino.  Pregunta primero por nombre, apellido, email y telefono. Posteriormente pregunta por la razon medica. Luego pregunta sobre los detalles de la cita: fecha y hora. Finalmente si el usuario no quiere hablar mas termina la conversacion",
    model ="gpt-3.5-turbo-1106", # gpt-3.5-turbo-1106
    tools = [{"type":"function", "function":gather_user_data},
             {"type":"function", "function":gather_medical_reason},
             {"type":"function", "function":gather_reservation_data},
             {"type":"function", "function": not_talk}]
)
print(assistant.id) # asst_UoTWfetExbajw40Yp6CVoFsZ
###################################################
# 5. Listar asistentes disponibles
mis_asistentes=client.beta.assistants.list(order="desc", limit="20")
print(mis_asistentes.data)
#asst_ORyO0nxozisLp120HxdFSbBu