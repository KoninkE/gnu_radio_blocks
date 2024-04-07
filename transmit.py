import uhd
import random
import symbols
import numpy as np

class modulation:
    def __init__(self, name, bits_per_sym, const_map):
        self.name = name
        self.bits_per_sym = bits_per_sym
        self.const_map = const_map


mods = {
        0: modulation("OOK", 1, symbols.ook_map),
        1: modulation("2ASK", 1, symbols.ask2_map),
        2: modulation("BPSK", 1, symbols.bpsk_map),
        3: modulation("QPSK", 2, symbols.qpsk_map),
        4: modulation("4ASK", 2, symbols.ask4_map),
        5: modulation("8PSK", 3, symbols.psk8_map),
        6: modulation("16PSK", 4, symbols.psk16_map),
        7: modulation("16QAM", 4, symbols.qam16_map),
        8: modulation("32QAM", 5, symbols.qam32_map)
        }

def main(samps_per_mod, reps_per_symbol):
    usrp = uhd.usrp.MultiUSRP()
    
    duration = 0.5 # seconds
    center_freq = 915e6
    sample_rate = 10e6
    gain = 60 # [dB] start low then work your way up
    
    while True:
        select_mod = random.randint(0, 8)
        mod = mods[select_mod]
        rand_bits = [''.join(map(str, [random.randint(0, 1) for j in range(mod.bits_per_sym)])) for i in range(samps_per_mod)]
        samples = np.array([mod.const_map[bits] for bits in rand_bits])
        print("Modulation: ", mod.name)
        usrp.send_waveform(samples, duration, center_freq, sample_rate, [0], gain)
        
    return

main(1000, 5)
