comp = {
    "Processador": {
        "Marca": "intel",
        "Série": "12400F",
        "QuantidadeDeNúcleos": "8",
        "Tipo":"Core i5",
        "Cache": "L1",
        "Geracao": "12th",
        "VelocidadeDoProcessador": "3.40GZ",
        "TamanhoDaMemóriaExterna":"8 GB",
        "TecnologiaDaMemória":"DDR",
        "Voltagem":"bivolt",
        "PotênciaEmWatts":"65 watts",
    },
    "Placa_de_video":{
        "Marca": "MSI",
        "Série": "36NOL7MD1VOC",
        "Tipo":"GDDR6",
        "Velocidade": "1777 MHz",
        "VRAM":"12GB",
        "Voltagem":"bivolt",
        "Potência em watts":"170 watts",
    },
    "Fonte":{
        "Marca": "Corsair",
        "Série": "CP-9020278-BR",
        "Tipo":"ATX",
        "PotênciaEmWatts":"650 watts",
        "Voltagem":"bivolt",
    },
    "Armazenamento":{
        "Marca": "Kingston",
        "Série": "SNV3S/1000G",
        "Tipo":"DIMM",
        "Velocidade": "1777 MHz",
        "Voltagem":"28 V",
        "PotênciaEmWatts":"50 watts",
    },
}

print("\nEspecificações do Processador:")
for chave, valor in comp["Processador"].items():
    print(f"- {chave}: {valor}")
