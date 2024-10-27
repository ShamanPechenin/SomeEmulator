from processor import Processor
from compiler import translate


path = input("Enter file path: ")
if path.endswith(".asm"):
    with open(path, "r", encoding="utf-8") as file:
        code = file.read()
    print("Compiling code...")
    machine_code = translate(code)
    print(f"Compiled code length is {len(machine_code)} bytes")
    if input("Do you want to save complied file as binary?[y/n]: ").lower().strip() == "y":
        name = input("Enter file name without extension:\n")
        if not name.endswith(".bin"):
            name += ".bin"
        with open(name, "wb") as file:
            for value in machine_code:
                file.write(value.to_bytes(1, "little"))
elif path.endswith(".bin"):
    machine_code = []
    with open(path, "rb") as file:
        while True:
            byte = file.read(1)
            if byte:
                machine_code.append(int.from_bytes(byte, "little"))
            else:
                break
    print(f"Loaded {len(machine_code)} bytes of code")
else:
    print("Invalid file extension.")
    quit()

proc = Processor()
proc.load_ram(machine_code)
while not proc.halt:
    proc.next()
