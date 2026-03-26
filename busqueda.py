import requests
from typing import List, Dict

class OSINTRecon:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://google.serper.dev/search" # Ejemplo usando Serper.dev (Search API)

    def search_person(self, first_name: str, last_name: str, city: str = "") -> List[Dict]:
        """
        Ejecuta una búsqueda dorking programática.
        """
        query = f'"{first_name} {last_name}" {city} (teléfono OR celular OR contacto)'
        
        payload = {"q": query, "num": 10}
        headers = {'X-API-KEY': self.api_key, 'Content-Type': 'application/json'}
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        return response.json().get('organic', [])

    def parse_results(self, results: List[Dict]):
        """
        Lógica para filtrar números de teléfono usando Regex sobre los snippets.
        """
        import re
        phone_pattern = r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
        
        for item in results:
            snippet = item.get('snippet', '')
            found = re.findall(phone_pattern, snippet)
            if found:
                print(f"Posible coincidencia en {item['link']}: {found}")

# Uso lógico
# recon = OSINTRecon(api_key="TU_API_KEY")
# results = recon.search_person("Juan", "Pérez", "Madrid")
# recon.parse_results(results)