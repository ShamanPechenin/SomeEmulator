
class Processor:
    def __init__(self):
        self.reg_A = 0
        self.reg_B = 0
        self.reg_C = 0
        self.reg_O = 0

        self.flag_c = 0
        self.flag_z = 0

        self.ram = [0 for _ in range(2**11)]

        self.address = 0
        self.halt = 0

    def load_ram(self, data, offset=0):
        self.ram[offset:offset+len(data)] = data

    def lda(self, address):
        self.reg_A = self.ram[address]
        self.address += 2

    def ldb(self, address):
        self.reg_B = self.ram[address]
        self.address += 2

    def ldc(self, address):
        self.reg_C = self.ram[address]
        self.address += 2

    def mova(self, address):
        self.ram[address] = self.reg_A
        self.address += 2

    def movb(self, address):
        self.ram[address] = self.reg_B
        self.address += 2

    def movc(self, address):
        self.ram[address] = self.reg_C
        self.address += 2

    def seta(self, value):
        self.reg_A = value
        self.address += 2

    def setb(self, value):
        self.reg_B = value
        self.address += 2

    def setc(self, value):
        self.reg_C = value
        self.address += 2

    def add(self):
        self.reg_C = self.reg_A + self.reg_B
        self.flag_c = self.reg_C > 255
        self.flag_z = self.reg_C == 0
        self.reg_C = self.reg_C % 256
        self.address += 1

    def sub(self):
        self.reg_C = self.reg_A - self.reg_B
        self.flag_c = self.reg_C < 0
        self.flag_z = self.reg_C == 0
        self.reg_C = self.reg_C % 256
        self.address += 1

    def log_and(self):
        self.reg_C = self.reg_A & self.reg_B
        self.address += 1

    def log_or(self):
        self.reg_C = self.reg_A | self.reg_B
        self.address += 1

    def log_xor(self):
        self.reg_C = self.reg_A ^ self.reg_B
        self.address += 1

    def log_not(self):
        self.reg_C = ~self.reg_A
        self.address += 1

    def hlt(self):
        self.halt = 1

    def out(self):
        self.reg_O = self.reg_C
        print(self.reg_O)
        self.address += 1

    def outc(self):
        self.reg_O = self.reg_C
        print(chr(self.reg_O), end="")
        self.address += 1

    def jmp(self, address):
        self.address = address

    def jmc(self, address):
        if self.flag_c:
            self.address = address
        else:
            self.address += 2

    def jmz(self, address):
        if self.flag_z:
            self.address = address
        else:
            self.address += 2

    def flc(self, value):
        self.flag_c = value & 1
        self.address += 2

    def flz(self, value):
        self.flag_z = value & 1
        self.address += 2

    def gec(self):
        self.reg_A = self.flag_c
        self.address += 1

    def gez(self):
        self.reg_A = self.flag_z
        self.address += 1

    def next(self):
        if not self.halt:
            value = self.ram[self.address+1]
            instr = self.ram[self.address] >> 3 & 0b11111
            #print(self.ram[self.address], self.ram[self.address+1], self.address)
            if instr == 0b00001:
                self.lda(value)
            elif instr == 0b00010:
                self.ldb(value)
            elif instr == 0b00011:
                self.ldc(value)
            elif instr == 0b00100:
                self.mova(value)
            elif instr == 0b00101:
                self.movb(value)
            elif instr == 0b00110:
                self.movc(value)
            elif instr == 0b00111:
                self.seta(value & 255)
            elif instr == 0b01000:
                self.setb(value & 255)
            elif instr == 0b01001:
                self.setc(value & 255)
            elif instr == 0b01010:
                self.add()
            elif instr == 0b01011:
                self.sub()
            elif instr == 0b01100:
                self.log_and()
            elif instr == 0b01101:
                self.log_or()
            elif instr == 0b01110:
                self.log_xor()
            elif instr == 0b01111:
                self.log_not()
            elif instr == 0b10000:
                self.hlt()
            elif instr == 0b10001:
                self.out()
            elif instr == 0b11001:
                self.outc()
            elif instr == 0b10010:
                self.jmp(value)
            elif instr == 0b10011:
                self.jmc(value)
            elif instr == 0b10100:
                self.jmz(value)
            elif instr == 0b10101:
                self.flc(value & 1)
            elif instr == 0b10110:
                self.flz(value & 1)
            elif instr == 0b10111:
                self.gec()
            elif instr == 0b11000:
                self.gez()
            else:
                self.address += 2
