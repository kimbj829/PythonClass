class Computer :
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu;
        self.ram = ram;
        self.vga = vga;
        self.ssd = ssd;

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu));
        print('RAM = {}'.format(self.ram));
        print('VGA = {}'.format(self.vga));
        print('SSD = {}'.format(self.ssd));

desktop = Computer();
desktop.set_spec("i7", "16GB", "GTX1060", "500GB");
desktop.hardware_info();

print("=====================");

notebook = Computer();
notebook.set_spec("i6", "8GB", 'MX300', "256GB");
notebook.hardware_info();