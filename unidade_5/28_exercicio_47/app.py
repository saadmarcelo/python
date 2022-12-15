pedal_a = ["helix", 13000]
pedal_b = ["Quadcortex", 14000]
pedal_c = ["kemper", 12000]

pedaleira = [pedal_a, pedal_b, pedal_c]

for x in pedaleira:
    print("O produto é: %s e tem o valor: R$ %.2f " % (x[0], x[1]))