import json

try:

    file_local = input()

    with open(file_local) as f:
        data = json.load(f)

    print(data)
except:
    print("Ocorreu um erro!")

finally:
    print("Processo concluído")