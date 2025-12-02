import yaml

with open("hardware.yaml", "r", encoding="utf-8") as f:
    dados = yaml.safe_load(f)

print("Conteúdo do YAML:", dados)

print("Modelo da GPU:", dados["hardware"]["gpu"]["modelo"])

print("Memória RAM (GB):", dados["hardware"]["memoria_ram"]["capacidade_total_gb"])