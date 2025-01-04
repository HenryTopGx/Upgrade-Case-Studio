import os
import struct

def open_file_with_default_app(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Erro ao tentar abrir o arquivo: {e}")
def byte_to_hex(byte_data):
    return ' '.join(f'{byte:02X}' for byte in byte_data)
def update_process_positions(input_file_path, output_file_path):
    with open(input_file_path, "rb") as file:
        content = bytearray(file.read())

    process_marker = b'\xF5\x01\x7E\x00'
    y_spacing = 100
    x_center = 400

    # Find all process positions
    process_positions = []
    position = 0

    while position < len(content):
        print("AQUI")
        position = content.find(process_marker, position)
        if position == -1:
            break
        process_positions.append(position)
        position += 4  # Move past the marker

    # Update positions of processes
    
    for i, position in enumerate(process_positions):
        print(position)
        y_position = (i + 1) * y_spacing
        y_position_hex = struct.pack('<I', y_position)
        x_position_hex = struct.pack('<I', x_center)
        print(content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03")+9)
        print(byte_to_hex(content[position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03")+8:position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03") + 12]))
        # Update X position (at offset 22 from process marker)
        content[position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03")+8:position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03") + 12] = x_position_hex

        # Update Y position (at offset 26 from process marker)
        content[position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03")+12:position+content[position:len(content)].find(b"\xE8\x03\x00\x00\x00\x00\xE9\x03") + 16] = y_position_hex

    # Write the updated content to a new file
    with open(output_file_path, "wb") as file:
        file.write(content)

    open_file_with_default_app(output_file_path)

# Path to the existing Case Studio file
input_file_path = "input.dm2"
output_file_path = "output.dm2"
update_process_positions(input_file_path, output_file_path)
