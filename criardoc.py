import sys
import os

def open_file_with_default_app(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Erro ao tentar abrir o arquivo: {e}")



ind = 1 # 0 - EXE | 1 - Python

qntE = int(sys.argv[ind])
NomeE = []
lastInd = ind
for i in range(qntE):
    NomeE.append(sys.argv[i+ind+1])
    lastInd = i+ind+1
qntP = int(sys.argv[lastInd+1])
NomeP = []
ind = lastInd = lastInd+1
for i in range(qntP):
    NomeP.append(sys.argv[ind+1+i])
    lastInd=ind+1+i
qntD = int(sys.argv[lastInd+1])
NomeD = []
ind = lastInd = lastInd+1
for i in range(qntD):
    NomeD.append(sys.argv[i+ind+1])
    lastInd = i+ind+1

def decimal_to_hex_4bytes_reverse(decimal_number):
    # Converte o número para uma string hexadecimal de 8 dígitos
    hex_str = f'{decimal_number:08X}'
    # Divide a string em pares de caracteres e inverte a ordem
    hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    # Junta os pares em uma string e reverte a ordem
    formatted_hex = ' '.join(hex_pairs[::-1])
    return formatted_hex

def string_to_hex(s):
    return ' '.join(f'{ord(c):02X}' for c in s)
def decimal_to_hex(decimal_number):
    return f'{decimal_number:02X}'
def create_case_studio_file_with_entities(file_path):
    # Hexadecimal structure of a blank document in Case Studio for Access 2000
    header_document_hex = (
        "02 00 E9 03 DC 00 29 04 93 89 32 8E C3 B8 C1 47 B6 13 8D 6D CA 09 8C FC 1D 04 06 00 00 00 41 72 69 61 6C 00 08 00 00 00 00 01 EB 03 "
        "FF FF FF 00 4C 04 FF FF FF 00 4D 04 FF FF FF 00 EC 03 64 ED 03 00 EE 03 00 00 00 00 EF 03 00 00 00 00 F0 03 03 F1 03 00 F2 03 00 0F "
        "04 01 10 04 0A 00 00 00 25 65 6E 74 6E 61 6D 65 25 00 1A 04 0A 00 00 00 25 61 74 72 6E 61 6D 65 25 00 1B 04 0B 00 00 00 25 64 69 63 "
        "74 6E 61 6D 65 25 00 22 04 0F 00 00 00 70 6B 5F 25 74 61 62 6C 65 6E 61 6D 65 25 00 F4 03 0A 00 00 00 25 72 65 6C 6E 61 6D 65 25 00 "
        "F3 03 00 00 00 00 F5 03 01 F6 03 01 F7 03 00 F8 03 00 F9 03 01 FA 03 01 FB 03 00 FC 03 00 FD 03 00 FE 03 00 FF 03 00 00 04 00 01 04 "
        "00 02 04 00 03 04 00 04 04 00 05 04 00 06 04 00 07 04 00 08 04 00 09 04 00 0A 04 00 0C 04 00 0D 04 00 0E 04 00 1C 04 00 1F 04 00 20 "
        "04 00 21 04 00 0B 04 01 00 00 00 00 2A 04 00 00 00 00 23 04 FF FF FF 00 24 04 06 00 00 00 41 72 69 61 6C 00 08 00 00 00 00 01 25 04 "
        "64 26 04 01 27 04 01 28 04 01 3A 04 01 2B 04 01 2C 04 C8 00 00 00 2D 04 00 2E 04 00 2F 04 00 30 04 00 31 04 00 32 04 00 33 04 00 3C "
        "04 00 3E 04 0A 00 00 00 25 72 65 6C 6E 61 6D 65 25 00 36 04 01 3B 04 00 37 04 01 38 04 01 39 04 0A 00 00 00 32 2E 32 35 2E 30 2E 31 "
        "30 00 3D 04 01 3F 04 00 40 04 00 00 00 00 41 04 05 00 00 00 32 2E 31 35 00 42 04 01 43 04 00 44 04 01 45 04 01 46 04 01 47 04 01 48 "
        "04 00 49 04 00 4A 04 0A 00 00 00 4B 04 0A 00 00 00 4E 04 01 00 00 00 00 4F 04 01 50 04 01 1E 04 00 00 00 00 F5 01 03 00 58 02 00 00 "
        "00 00 59 02 01 00 00 00 00 5A 02 2C 57 78 3B 07 69 26 47 AA FF 73 39 C1 54 D2 7D E8 03 01 00 00 00 00 E9 03 01 00 00 00 00 EA 03 01 "
        "00 00 00 00 EB 03 01 00 00 00 00 EC 03 01 00 00 00 00 ED 03 4D A2 AD 6C D1 31 E6 40 EE 03 62 8A 9A 6F D1 31 E6 40 EF 03 00 00 00 "
        "00 F0 03 00 00 00 00 F5 01 71 00 58 02 00 00 00 00 59 02 0B 00 00 00 4D 61 69 6E 20 6D 6F 64 65 6C 00 5A 02 9C C3 5E C6 95 06 29 4F "
        "BD 9E 86 14 76 F6 E9 74 E8 03 64 E9 03 FF FF FF 00 EA 03 00 EB 03 03 EC 03 00 F6 03 00 ED 03 00 F9 03 06 00 00 00 41 72 69 61 6C 00 "
        "08 00 00 00 00 01 EF 03 0A 00 F0 03 0A 00 F1 03 00 F2 03 00 F5 03 01 F7 03 01 F8 03 01 FA 03 01 FB 03 01 FC 03 01 FD 03 01"
    )
    end_of_file = "F5 01 01 00"                                                                                                                                                        
    st_entity_block = "F5 01 80 00"
    st_process_block = "F5 01 7E 00"
    full_document_hex = f"{header_document_hex}"
    i=0
    #qntE = int(input("Quantidade de Entidades: "))
    for nE in NomeE:
        entity_name = nE #input("Nome da Entidade "+str(i+1)+": ")
        entity_name_hex = string_to_hex(entity_name)
        entity_name_len = decimal_to_hex(len(entity_name)+1)
        x = 50
        y = i*100+100
        entity_x = decimal_to_hex_4bytes_reverse(x)
        entity_y = decimal_to_hex_4bytes_reverse(y)
                                                                                                                                        # Algo Aleatório ?!
        entity_terminator_hex = "58 02 "+decimal_to_hex(i+1)+" 00 00 00 59 02 "+entity_name_len+" 00 00 00 "+entity_name_hex+" 00 5A 02 "+"95 78 2B C9 DD D9 10 47 8E B7 9C CC 10 69 CF 1C"+" E8 03 00 00 00 00 E9 03 " +  entity_x + " " + entity_y + " EA 03 00 00 00 00 EB 03 00 00 00 00 00 00 00 00 EC 03 01 00 00 00 00 ED 03 01 00 00 00 00 EE 03 FF FF FF 00"
        
        # Concatenate the blank document hex with the entity hex sequences
       
        full_document_hex += f" {st_entity_block} {entity_terminator_hex}"
        i+=1
    #qntP = int(input("Quantidade de Processos: "))
    i=0
    for nP in NomeP:
        entity_name = nP #input("Nome do Processo "+str(i+1)+": ")
        
        entity_name_hex = string_to_hex(entity_name)
        entity_name_len = decimal_to_hex(len(entity_name)+1)
        x = 200
        y = i*100+100
        entity_x = decimal_to_hex_4bytes_reverse(x)
        entity_y = decimal_to_hex_4bytes_reverse(y)
        entity_terminator_hex = "58 02           01            00 00 00 59 02         09          00 00 00        00           00 5A 02    14 3F A2 62 2F 2C 80 47 90 EA 12 E7 87 8F 71 3A    E8 03 00 00 00 00 E9 03     B5 00 00 00     94 00 00 00    EA 03 00 00 00 00 EB 03 00 00 00 00 00 00 00 00 EC 03 01 ED 03 00 00 00 00 EE 03 00 00 00 00 F0 03 00 00 00 00 EF 03 01 00 00 00 F1 03 FF FF FF 00"
                                                                                                                                        # Algo Aleatório ?!
        entity_terminator_hex = "58 02 "+decimal_to_hex(i+1)+" 00 00 00 59 02 "+entity_name_len+" 00 00 00 "+entity_name_hex+" 00 5A 02 "+"95 78 2B C9 DD D9 10 47 8E B7 9C CC 10 69 CF 1C"+" E8 03 00 00 00 00 E9 03 " +  entity_x + " " + entity_y + " EA 03 00 00 00 00 EB 03 00 00 00 00 00 00 00 00 EC 03 01 ED 03 00 00 00 00 EE 03 00 00 00 00 F0 03 00 00 00 00 EF 03 "+decimal_to_hex(i+1)+" 00 00 00 F1 03 FF FF FF 00"
        
        # Concatenate the blank document hex with the entity hex sequences
        
        full_document_hex += f" {st_process_block} {entity_terminator_hex}"
        i+=1
        # Convert the concatenated hex string to bytes
    full_document_hex += f" {end_of_file}"
    document_bytes = bytes.fromhex(full_document_hex)
    # Write the bytes to a file
    with open(file_path, "wb") as file:
        file.write(document_bytes)
    
    open_file_with_default_app(file_path)

# Create a Case Studio file with two entities 'Terminator1' and 'Terminator2'
create_case_studio_file_with_entities("output.dm2")
