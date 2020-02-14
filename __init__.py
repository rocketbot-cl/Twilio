# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
base_path  = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Twilio_' + os.sep + 'libs' + os.sep
sys.path.append(cur_path )
print(cur_path )
from twilio.rest import Client

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "sendSMS":
    account_sid = GetParams("sid")
    auth_token = GetParams("token")
    from_ = GetParams("from")
    to_ = GetParams("to")
    message = GetParams("message")
    var_ = GetParams("result")    

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    #account_sid = 'AC9c614220950b1817ceeef42f41818081'
    #auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=message,
                        from_=from_,
                        to=to_
                    )
    data = message.sid
    try:
        SetVar( var_,  data)
    except Exception as e:
        raise Exception(e)


if module == "sendWhatsapp":

    # Download the helper library from https://www.twilio.com/docs/python/install

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    from_ = GetParams("from")
    to_ = GetParams("to")
    account_sid = GetParams("sid")
    auth_token = GetParams("token")
    message = GetParams("message")
    var_ = GetParams("result")
    client = Client(account_sid, auth_token)
    #xx = 'whatsapp:'+from_
    #print(xx)


    message = client.messages.create(
        body=message,
        from_='whatsapp:'+from_,
        to='whatsapp:'+to_
    )

    data = message.sid

    try:
        SetVar(var_, data)
    except Exception as e:
        raise Exception(e)
