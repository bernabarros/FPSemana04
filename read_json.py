import json

try:

    file_local = input()

    with open(file_local,"r", encoding = 'utf-8') as f:
        data = json.load(f)

    print(data)
except:
    print("Ocorreu um erro!")

finally:
    print("Processo concluído")