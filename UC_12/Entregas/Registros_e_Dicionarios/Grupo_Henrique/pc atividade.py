import yaml
pc = {
    "Processador": {
        "Fabricante": "AMD",
        "Modelo": "AMD Ryzen 9 9950X3D",
        "Núcleos": "16",
        "Threads": "32",
        "Frequência máxima": "5.7 GHz",
        "Cache": "144 MB",
        "Tecnologia de fabricação": "4 nm",
        "TDP": "170 Watts",
        "Compatibilidade": "Soquete AM5, suporta memória DDR5"
    },
    "Memória RAM":{
        "Fabricante": "Kingston",
        "Modelo": "Fury Beast",
        "Capacidade": "32GB (2x16GB)",
        "Tipo": "DDR5",
        "Velocidade": "5200MHz",
        "Latência": "CL40",
        "Compatibilidade": "Soquete AM5, suporte DDR5",
        "Recursos": "Intel XMP 3.0, on-die ECC, PMIC integrado"
    },
   "Placa de Video":{
       "Fabricante" : "Nvidia",
       "Modelo": "RTX 5090",
       "Arquitetura": "Blackwell 2.0, fabricada em tecnologia de 5 nm",
       "Memória": "32 GB de GDDR7, com uma largura de banda de 1,79 TB/s e um barramento de 512 bits",
       "Suporte": "DirectX 12 Ultimate, Vulkan 1.4 e OpenCL 3.0, com suporte a DLSS 4 e Ray Tracing completo"
   },
   "fonte":{
        "Fabricante": "Corsair",
        "Modelo": "HX1200i",
        "Potência": "1200 Watts",
        "Certificação": "80 Plus Platinum",
        "Conectores": "ATX 3.0, 12V-2x6 (600W), PCIe 8 pinos",
        "Eficiência": "Até 94%",
        "Tecnologia de resfriamento": "Ventoinha de 140 mm com modo Zero RPM",
        "Modularidade": "Totalmente modular",
        "Compatibilidade": "Suporta GPUs de alto consumo como RTX 5090 e CPUs topo de linha"
   },
   "PlacaMae": {
    "Fabricante": "ASUS",
    "Modelo": "ROG Crosshair X870E Extreme",
    "Chipset": "AMD X870E",
    "Soquete": "AM5",
    "Formato": "E-ATX",
    "Memória": "DDR5 até 256GB",
    "Slots M.2": "5x PCIe 5.0 M.2",
    "Expansão PCIe": "PCIe 5.0 x16, suporte multi-GPU",
    "Conectividade": "Wi-Fi 7, Bluetooth 5.4, LAN 10GbE",
    "Recursos": "Suporte a overclock avançado, AI Cooling, BIOS Flashback",
    "Compatibilidade": "Suporta Ryzen 9 9950X3D, RTX 5090 e memórias DDR5 de alta frequência"
}       
}


yaml_str = yaml.dump(pc, allow_unicode=True, sort_keys=False)

print(yaml_str)

with open("pc.yaml", "w", encoding="utf-8") as f:
    yaml.dump(pc, f, allow_unicode=True, sort_keys=False)
