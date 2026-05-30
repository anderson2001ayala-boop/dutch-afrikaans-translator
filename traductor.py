from deep_translator import GoogleTranslator
import pandas as pd
from datetime import datetime

def traducir_archivo(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    
    traduccion = GoogleTranslator(source='nl', target='af').translate(texto)
    return texto, traduccion

def generar_reporte(original, traducido):
    datos = {
        'Fecha': [datetime.now().strftime("%Y-%m-%d %H:%M")],
        'Palabras originales': [len(original.split())],
        'Palabras traducidas': [len(traducido.split())],
        'Idioma origen': ['Neerlandés'],
        'Idioma destino': ['Afrikáans']
    }
    df = pd.DataFrame(datos)
    df.to_csv('reporte.csv', index=False)
    print("Reporte generado: reporte.csv")

archivo = 'Hola, hoe gaat het met jou.txt'
original, traducido = traducir_archivo(archivo)

print("TEXTO ORIGINAL:")
print(original)
print("\nTRADUCCIÓN AL AFRIKÁANS:")
print(traducido)

with open('traduccion_resultado.txt', 'w', encoding='utf-8') as f:
    f.write(traducido)

generar_reporte(original, traducido)
print("\n✅ Traducción completada exitosamente")