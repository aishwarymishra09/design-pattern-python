from computer import Desktop, Laptop


class Director:
    """ This class implements the encapsulation of the generation of the required product"""

    def __init__(self, processor, gen, ram, mem):
        self.pr = processor
        self.gen = gen
        self.ram = ram
        self.mem = mem

    def get_desktop(self):
        """ get the desktop """
        return Desktop().processor(self.pr) \
            .generation(self.gen) \
            .ram(self.ram) \
            .memory(self.mem) \
            .type().get_result()

    def get_laptop(self):
        """ get the laptop """
        return Laptop().processor(self.pr) \
            .generation(self.gen) \
            .ram(self.ram) \
            .memory(self.mem) \
            .type().get_result()
