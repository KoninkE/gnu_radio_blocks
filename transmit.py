import uhd
import random
import symbols
import numpy as np

class modulation:
    def __init__(self, name, bits_per_sym, const_map):
        self.name = name
        self.bits_per_sym = bits_per_sym
        self.const_map = const_map


mods = {0: modulation("BPSK", 1, symbols.bpsk_map),
        1: modulation("QPSK", 2, symbols.qpsk_map),
        2: modulation("4ASK", 2, symbols.ask4_map),
        3: modulation("16PSK", 4, symbols.psk16_map),
        4: modulation("16QAM", 4, symbols.qam16_map)
        }

def main(samps_per_mod, reps_per_symbol):
    usrp = uhd.usrp.MultiUSRP()
    
    duration = 10 # seconds
    center_freq = 915e6
    sample_rate = 1e6
    gain = 60 # [dB] start low then work your way up
    
    while True:
        select_mod = random.randint(0, 4)
        mod = mods[select_mod]
        rand_bits = [''.join(map(str, [random.randint(0, 1) for j in range(mod.bits_per_sym)])) for i in range(samps_per_mod)]
        samples = np.array([mod.const_map[bits] for bits in rand_bits])
        print("Modulation: ", mod.name)
        usrp.send_waveform(samples, duration, center_freq, sample_rate, [0], gain)
        
    return

main(20, 5)