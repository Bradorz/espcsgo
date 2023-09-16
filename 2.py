class Socket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 6000))

    def getProcessBaseAddress(self, processID):
        self.socket.send(Packet(processID, 0, 0, 0, 0))
        return Packet.from_buffer_copy(self.socket.recv(ctypes.sizeof(Packet))).result

    def readProcessMemory(self, processID, address, size):
        self.socket.send(Packet(processID, address, 1, size, 0))
        return Packet.from_buffer_copy(self.socket.recv(ctypes.sizeof(Packet))).result

    def writeProcessMemory(self, processID, address, size, value):
        self.socket.send(Packet(processID, address, 2, size, value))
        return Packet.from_buffer_copy(self.socket.recv(ctypes.sizeof(Packet))).result == value