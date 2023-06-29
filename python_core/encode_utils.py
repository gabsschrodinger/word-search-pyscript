import json
from lzstring import LZString

def encode_data(data) -> str:
    json_data = json.dumps(data)
    compressed_data = LZString().compressToBase64(json_data)
    return compressed_data

def decode_data(encoded_data):
    try:
        decompressed_data = LZString().decompressFromBase64(encoded_data)
        json_data = json.loads(decompressed_data)
        return json_data
    except Exception as e:
        # Se ocorrerem erros durante a descompactação ou decodificação dos dados,
        # imprima o erro para fins de depuração
        print(f"Erro na decodificação: {e}")
        return None