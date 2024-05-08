import os

"""
Version: 0
@Author Matheus Bury create 19/03/24
"""



folder = r'Caminho/da/imagens/para/inserir/.jpg'

# Iterate
for file in os.listdir(folder):
# Checking if the file is present in the list
    if not file.endswith('.jpg'):
        oldName = os.path.join(folder, file)
        n = os.path.splitext(file)[0]

        b = n + '.jpg'
        newName = os.path.join(folder, b)

        # Rename the file
        os.rename(oldName, newName)

print('Finalizado')