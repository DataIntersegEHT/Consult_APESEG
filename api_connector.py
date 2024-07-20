import requests

def get_data(numero_placa):
        headers = {'Ocp-Apim-Subscription-Key': ''}
        data = requests.get("https://apesegsoat.azure-api.net/consultasoatprd/api/Busqueda/BuscarCertificadosPorPlaca/{0}".format(numero_placa)
                ,headers=headers)
        if data.status_code==200:
            data=data.json()
            data=data['Certificados']
        return data
