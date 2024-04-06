import math

ook_map = {'0' : 0,
            '1' : 1}

ask2_map = {'0' : 0.5,
            '1' : 1}

ask4_map = {'00' : 0.25,
            '01' : 0.5,
            '10' : 0.75,
            '11' : 1}

bpsk_map = {'0' : -1,
            '1' : 1}

qpsk_map = {'00' : (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j,
            '01' : -1 * (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j,
            '10' : -1 * (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j,
            '11' : (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j}

psk16_map = {'0000' : 1 + 0j,
            '0001' : (math.sqrt(3)/2) - 0.5j,
            '0010' : 0.5 - (math.sqrt(3)/2) * 1j,
            '0011' : (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j,
            '0100' : -1 * (math.sqrt(3)/2) - 0.5j,
            '0101' : -1 * (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j,
            '0110' : 0 - 1j,
            '0111' : -0.5 - (math.sqrt(3)/2) * 1j, 
            '1000' : (math.sqrt(3)/2) + 0.5j,
            '1001' : (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j,
            '1010' : 0 + 1j,
            '1011' : 0.5 + (math.sqrt(3)/2) * 1j,
            '1100' : -1 - 0j,
            '1101' : -1 * (math.sqrt(3)/2) + 0.5j,
            '1110' : -0.5 + (math.sqrt(3)/2) * 1j,
            '1111' : -1 * (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j}

qam16_map = {'0000' : (math.sqrt(2)/6) + (math.sqrt(2)/6) * 1j,
            '0001' : (math.sqrt(2)/2) + (math.sqrt(2)/6) * 1j,
            '0010' : (math.sqrt(2)/6) + (math.sqrt(2)/2) * 1j,
            '0011' : (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j,
            '0100' : (math.sqrt(2)/6) - (math.sqrt(2)/6) * 1j,
            '0101' : (math.sqrt(2)/6) - (math.sqrt(2)/2) * 1j,
            '0110' : (math.sqrt(2)/2) - (math.sqrt(2)/6) * 1j,
            '0111' : (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j, 
            '1000' : -1 * (math.sqrt(2)/6) + (math.sqrt(2)/6) * 1j,
            '1001' : -1 * (math.sqrt(2)/6) + (math.sqrt(2)/2) * 1j,
            '1010' : -1 * (math.sqrt(2)/2) + (math.sqrt(2)/6) * 1j,
            '1011' : -1 * (math.sqrt(2)/2) + (math.sqrt(2)/2) * 1j,
            '1100' : -1 * (math.sqrt(2)/6) - (math.sqrt(2)/6) * 1j,
            '1101' : -1 * (math.sqrt(2)/2) - (math.sqrt(2)/6) * 1j,
            '1110' : -1 * (math.sqrt(2)/6) - (math.sqrt(2)/2) * 1j,
            '1111' : -1 * (math.sqrt(2)/2) - (math.sqrt(2)/2) * 1j}