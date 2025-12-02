comp = {
    "processador": {
        "marca": "intel",
        "série": "12400F",
        "quantidade de núcleos": "8",
        "Tipo":"Core i5",
        "cache": "L1",
        "geração": "12th",
        "Velocidade do processador": "3.40GZ",
        "Tamanho da memória externa":"8 GB",
        "Tecnologia da memória":"DDR",
        "Voltagem":"bivolt",
        "Potência em watts":"65 watts",
    },

     "placa_de_video":{
        "marca": "MSI",
        "série": "36NOL7MD1VOC",
        "Tipo":"GDDR6",
        "Velocidade": "1777 MHz",
        "VRAM":"12GB",
        "Voltagem":"bivolt",
        "Potência em watts":"170 watts",
    },
    "fonte":{
        "marca": "Corsair",
        "série": "CP-9020278-BR",
        "Tipo":"ATX",
        "Potência em watts":"650 watts",
        "voltagem":"bivolt",
    },
    "armazenamento":{
        "marca": "Kingston",
        "série": "SNV3S/1000G",
        "Tipo":"DIMM",
        "Velocidade": "1777 MHz",
        "Voltagem":"28 V",
        "Potência em watts":"50 watts",
    },
}

print("\nEspecificações do processador:")
for chave, valor in comp["processador"].items():
    print(f"- {chave}: {valor}")
