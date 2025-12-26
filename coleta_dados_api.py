import requests
import os

def enviar_arquivo():
    # Caminho do arquivo a ser enviado
    caminho = 'C:/Users/marcs/Desktop/teste.txt'
    
    # Sua chave de API fornecida
    api_key = '0d9b3b59-c241-48f8-995e-0fce32811a11'
    
    # Verifica se o arquivo existe antes de tentar enviar
    if not os.path.exists(caminho):
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return

    # Endpoint para upload
    url_api = 'https://pixeldrain.com/api/file'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        print("Enviando arquivo com autenticação...")
        
        with open(caminho, 'rb') as f:
            # O campo 'auth' com ('', api_key) realiza a autenticação Basic do HTTP
            # Onde o usuário é vazio e a senha é a sua chave.
            resposta = requests.post(
                url_api, 
                files={'file': f}, 
                headers=headers,
                auth=('', api_key),
                timeout=30
            )
        
        # Verifica erros de comunicação antes de tentar ler o JSON
        resposta.raise_for_status()
        
        dados = resposta.json()

        if dados.get('success'):
            file_id = dados.get('id')
            url_final = f"https://pixeldrain.com/u/{file_id}"
            print("\n✅ Sucesso! Arquivo vinculado à sua conta.")
            print(f"Link de acesso: {url_final}")
        else:
            print("\n❌ A API retornou sucesso=false:", dados)

    except requests.exceptions.HTTPError as e:
        if resposta.status_code == 401:
            print("\n❌ Erro de Autenticação: Verifique se sua API Key está correta.")
        else:
            print(f"\n❌ Erro HTTP {resposta.status_code}: {e}")
        try:
            print("Resposta do servidor:", resposta.json())
        except:
            print("Corpo da resposta:", resposta.text[:200])
            
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")

if __name__ == "__main__":
    enviar_arquivo()
