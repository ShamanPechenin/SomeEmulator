from processor import Processor
from compiler import translate


with open("for_loop.asm", "r", encoding="utf-8") as file:
    code = file.read()

machine_code = translate(code)
print(len(machine_code))
with open("multiply.bin", "wb") as file:
    for value in machine_code:
        file.write(value.to_bytes(1, "little"))
'''machine_code = []
with open('for_loop.bin', "rb") as file:
    while True:
        byte = file.read(1)
        if byte:
            machine_code.append(int.from_bytes(byte, "little"))
        else:
            break
print(machine_code)'''
proc = Processor()
proc.load_ram(machine_code)
while not proc.halt:
    proc.next()