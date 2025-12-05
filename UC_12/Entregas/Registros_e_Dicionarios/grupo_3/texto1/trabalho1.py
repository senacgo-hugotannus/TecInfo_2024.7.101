hardware = {
    "processador": {
        "fabricante": "Intel",
        "modelo": "Core i5-11400F",
        "geracao": "11ª",
        "suporte_socket": "LGA1200",
        "frequencia_base_mhz": 2600,   # 2.60 GHz
        "turbo_max_mhz": 4400,         # até 4.4 GHz
        "bus_processador": ["DMI 3.0"],
        "gravacao_nm": 14,             # nanômetros
        "cache_l1_kb": 80,
        "cache_l2_kb": 512,
        "cache_l3_mb": 12,
        "tdp_w": 65
    },

    "placa_mae": {
        "modelo": "Gigabyte Z590 AORUS Elite",
        "formato": "ATX",
        "socket_cpu": "LGA1200",
        "chipset": "Intel Z590",
        "processadores": "Intel 10ª e 11ª geração",
        "memoria": {
            "tipo": "DDR4",
            "slots": 4,
            "maximo": "128 GB",
            "velocidade_suportada": "até 5400 MHz (OC)"
        },
        "armazenamento": {
            "sata": 6,
            "m2": {
                "slots": 3,
                "detalhe": [
                    "M2A: PCIe 4.0 x4 (somente com CPU 11ª gen)",
                    "M2B/C: PCIe 3.0 x4"
                ]
            }
        },
        "slots_pcie": [
            "PCIe x16 (GPU principal, PCIe 4.0 com CPU 11ª gen)",
            "PCIe x16 (elétrico x4)",
            "2x PCIe x1"
        ],
        "portas_io": [
            "USB 3.2 Gen2",
            "USB 3.2 Gen1",
            "USB 2.0",
            "HDMI",
            "DisplayPort",
            "RJ-45 2.5GbE",
            "Áudio 7.1"
        ],
        "energia": ["24 pinos ATX", "8 pinos CPU", "4 pinos CPU extra"],
        "vrm": "12+1 fases digitais, dissipadores grandes",
        "bios": "UEFI DualBIOS, Q-Flash Plus",
        "extras": ["RGB Fusion 2.0", "Smart Fan 6"]
    },

    "memoria_ram": {
        "kit": "Corsair Vengeance LPX",
        "capacidade_total_gb": 32,
        "configuracao": "2x16 GB",
        "frequencia_mhz": 3200,
        "latencia_cl": 16,
        "perfil": "XMP 2.0"
    },

    "gpu": {
        "modelo": "MSI GeForce RTX 5060 Ti 16G SHADOW 2X OC PLUS",
        "memoria": {
            "capacidade": "16 GB",
            "tipo": "GDDR7",
            "velocidade": "28 Gbps"
        },
        "barramento": "128-bit",
        "interface": "PCIe 5.0",
        "sistema_refrigeracao": {
            "ventoinhas": 2,
            "tecnologia": "STORMFORCE",
            "caracteristicas": [
                "Design otimizado para dissipação de calor",
                "Operação silenciosa"
            ]
        },
        "saidas_video": [
            "HDMI 2.1b",
            "DisplayPort (suporte até 8K)"
        ],
        "arquitetura": "NVIDIA Ada Lovelace (RTX série 50)",
        "recursos_graficos": {
            "ray_tracing": True,
            "dlss": "DLSS 3.5",
            "compatibilidade_api": [
                "DirectX 12",
                "OpenGL"
            ]
        }
    },

    "armazenamento_adicional": {
        "ssd_sistema": {
            "modelo": "Samsung 980 PRO",
            "formato": "M.2 NVMe",
            "interface": "PCIe 4.0 x4",
            "capacidade_gb": 1000
        },
        "ssd_games": {
            "modelo": "Crucial P3",
            "formato": "M.2 NVMe",
            "interface": "PCIe 3.0 x4",
            "capacidade_gb": 2000
        },
        "hdd_backup": {
            "modelo": "Seagate Barracuda",
            "formato": "3.5\" SATA",
            "capacidade_tb": 4,
            "rpm": 5400
        }
    },

   "fonte": {
        "modelo": "Corsair RM650",
        "potencia_w": 650,
        "certificacao": "80 Plus Gold",
        "padrao": "ATX",
        "modularidade": "Full Modular",
        "ventoinha": {
            "modo": "Zero RPM",
            "descricao": "Silenciosa, não gira em cargas leves"
        },
        "capacitores": "105°C, nível industrial",
        "conectores": {
            "eps12v": 2,
            "pcie_8_pinos": "múltiplos",
            "sata": "sim",
            "molex": "sim"
        },
        "tecnologias": ["Modern Standby", "PFC Ativo"],
        "dimensoes_mm": {"largura": 150, "altura": 86, "profundidade": 160},
        "peso_kg": 1.6,
        "garantia_anos": 7,
        "sku": "CP-9020280-BR",
        "uso_recomendado": "PC gamer ou workstation de médio a alto desempenho"
    },
 
    "cooler_cpu": {
        "modelo": "Cooler Master Hyper 212 Black Edition",
        "tipo": "Air cooler torre",
        "suporte_socket": ["LGA1200", "LGA115x", "AM4"],
        "altura_mm": 158
    },

    "gabinete": {
        "modelo": "NZXT H510 Flow",
        "formato_suportado": ["ATX", "Micro-ATX", "Mini-ITX"],
        "altura_max_cooler_mm": 165,
        "comprimento_max_gpu_mm": 360,
        "baias": {"2.5": 2, "3.5": 2}
    },

    "refrigeracao_adicional": {
        "fans": [
            {"tamanho_mm": 120, "posicao": "frente", "modelo": "Arctic P12 PWM", "quantidade": 2},
            {"tamanho_mm": 120, "posicao": "traseira", "modelo": "Arctic P12 PWM", "quantidade": 1}
        ]
    },
    "monitor": {
        "modelo": "AOC 24G2",
        "tamanho_polegadas": 24,
        "resolucao": "1920x1080",
        "taxa_atualizacao_hz": 144,
        "painel": "IPS"
    },

    "perifericos": {
        "teclado": "Logitech G213",
        "mouse": "delux M900 pro",
        "headset": "havit",
        "microfone": "Fifine AM8",
        "mousepad": "PK_CONTROL",
    }
}

def mostrar_componente(hardware, componente):
    if componente in hardware:
        print(f"\nEspecificações de {componente.capitalize()}:")
        for chave, valor in hardware[componente].items():
            print(f"- {chave}: {valor}")
    else:
        print(f"\nComponente '{componente}' não encontrado no hardware.")


mostrar_componente(hardware, "processador")
mostrar_componente(hardware, "placa_mae")
mostrar_componente(hardware, "gpu")
mostrar_componente(hardware, "fonte")
mostrar_componente(hardware, "monitor")
mostrar_componente(hardware, "perifericos")