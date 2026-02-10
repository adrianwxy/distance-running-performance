import requests

class OllamaClient:
    """
    Setting up the default inputs
    ": str" / ": int" to confirm input format
    timeout - wait 120s before giving up
    create a persistent http session
    """

    def __init__(
        self,
        model: str = "gemma3:12b",
        url: str = "http://localhost:11434/api/generate",
        timeout: int = 120
    ):
        self.model = model
        self.url = url
        self.timeout = timeout
        self.session = requests.Session()


    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        payload = {
            "model": self.model,  
            "prompt": prompt,     
            "stream": False,      
            "options": {
                "temperature": temperature  
            }
        }
        
        response = self.session.post(
            self.url,
            json=payload, 
            timeout=self.timeout
        )
    
        response.raise_for_status() 

        return response.json()["response"].strip()