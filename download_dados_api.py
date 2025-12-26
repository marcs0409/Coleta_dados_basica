import requests
import os

def baixar_arquivo(file_id):
    # Endpoint de download conforme a documentação
    url_api = f'https://pixeldrain.com/api/file/{file_id}'
    
    # Sua chave de API
    api_key = 'HERE GOES THE API KEY'
    
    # Onde o arquivo será salvo localmente
    nome_arquivo_local = f'downloaded_{file_id}.txt'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        print(f"Iniciando download do arquivo {file_id}...")
        
        # Realizamos a requisição GET com stream=True para baixar o arquivo em partes
        with requests.get(url_api, auth=('', api_key), headers=headers, stream=True, timeout=30) as resposta:
            # Verifica se o download é permitido
            resposta.raise_for_status()
            
            # Abrimos o arquivo local para escrita binária
            with open(nome_arquivo_local, 'wb') as f:
                for chunk in resposta.iter_content(chunk_size=8192):
                    if chunk: # Filtra chunks vazios
                        f.write(chunk)
            
            print(f"✅ Download concluído com sucesso!")
            print(f"Arquivo salvo como: {os.path.abspath(nome_arquivo_local)}")

    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro ao baixar arquivo: {e}")
        if resposta.status_code == 404:
            print("O arquivo não foi encontrado. Verifique se o ID está correto.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Extraído do link https://pixeldrain.com/u/X2vizQks
    ID_DO_ARQUIVO = 'X2vizQks'
    baixar_arquivo(ID_DO_ARQUIVO)