comp = {
    "Processador":{
        "Marca":"intel",
        "Serie":"12400F",
        "QuantidadeDeNucleos":"8",
        "Tipo":"Core i5",
        "Cache":"L1",
        "Geracao":"12th",
        "VelocidadeDoProcessador":"3.40GZ",
        "TamanhoDaMemoriaExterna":"8 GB",
        "TecnologiaDaMemoria":"DDR",
        "Voltagem":"bivolt",
        "PotenciaEmWatts":"65 watts",
    },
    "Placa_de_video":{
        "Marca":"MSI",
        "Serie":"36NOL7MD1VOC",
        "Tipo":"GDDR6",
        "Velocidade":"1777 MHz",
        "VRAM":"12GB",
        "Voltagem":"bivolt",
        "Potencia em watts":"170 watts",
    },
    "Fonte":{
        "Marca":"Corsair",
        "Serie":"CP-9020278-BR",
        "Tipo":"ATX",
        "PotenciaEmWatts":"650 watts",
        "Voltagem":"bivolt",
    },
    "Armazenamento":{
        "Marca":"Kingston",
        "Serie":"SNV3S/1000G",
        "Tipo":"DIMM",
        "Velocidade":"1777 MHz",
        "Voltagem":"28 V",
        "PotenciaEmWatts":"50 watts",
    },
}

print("\nEspecificações do Processador:")
for chave, valor in comp["Processador"].items():
    print(f"- {chave}: {valor}")
