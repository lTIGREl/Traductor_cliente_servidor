import requests
import uuid
import json


class ApiTranslator:
    suscripcionTexto = "80e58c3238f64f7ab4cf588eee354ac4"

    def traducirTexto(self, texto, idiomaFinal):
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        params = '&to='+idiomaFinal
        constructed_url = base_url + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': self.suscripcionTexto,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': texto
        }]

        request = requests.post(constructed_url, headers=headers, json=body)
        response = json.loads(str(request.text))
        return str(response[0]['translations'][0]['text'])
