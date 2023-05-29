import pandas as pd

base = "spotify23-US-"
bancofinal = pd.DataFrame()
for i in range(1,16):
    banco = pd.read_csv(base+str(i))
    bancofinal.append(banco)
