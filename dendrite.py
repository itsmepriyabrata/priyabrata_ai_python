class Dendrite:
    def _init_(self):
        self.received_signal = 0

    def receive_signal(self, signal):
        self.received_signal += signal


class Neuron:
    def _init_(self):
        self.dendrites = []
        self.axon_terminal = None

    def add_dendrite(self, dendrite):
        self.dendrites.append(dendrite)

    def set_axon_terminal(self, axon_terminal):
        self.axon_terminal = axon_terminal

    def process_signals(self):
        total_signal = sum(dendrite.received_signal for dendrite in self.dendrites)
        self.axon_terminal.send_signal(total_signal)


class AxonTerminal:
    def _init_(self):
        self.sent_signal = 0

    def send_signal(self, signal):
        self.sent_signal = signal
        print(f"Axon terminal sent signal: {signal}")



if _name_ == "_main_":
    dendrite1 = Dendrite()
    dendrite2 = Dendrite()

    axon_terminal = AxonTerminal()

    neuron = Neuron()
    neuron.add_dendrite(dendrite1)
    neuron.add_dendrite(dendrite2)
    neuron.set_axon_terminal(axon_terminal)

    dendrite1.receive_signal(5)
    dendrite2.receive_signal(3)

    neuron.process_signals()
