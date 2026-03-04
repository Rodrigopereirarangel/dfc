#!/usr/bin/env python3
"""
scripts/bootstrap.py

Bootstrap script para Claude Computer Use.
Este script prepara o ambiente do Claude para ler as skills corretamente,
garantindo que dependências estejam instaladas e a estrutura de pastas exista.
"""

import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"> {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erro ao executar: {cmd}")
        print(e)
        return False
    return True

def main():
    print("="*60)
    print("🚀 BOOTSTRAP: DCF PIPELINE V4.0")
    print("="*60)

    # 1. Instalar dependências
    print("\n📦 1. Instalando Dependências...")
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        run_cmd(f"{sys.executable} -m pip install -r {req_file}")
    else:
        # Fallback
        packages = ["markdown", "beautifulsoup4", "playwright", "matplotlib", "seaborn", "numpy", "pandas", "yfinance", "plotly", "scipy"]
        run_cmd(f"{sys.executable} -m pip install {' '.join(packages)}")

    # 1.5 Instalar Chromium interno
    print("\n🌐 1.5. Instalando Chromium Engine (Obrigatório para o PDF)...")
    run_cmd(f"{sys.executable} -m playwright install chromium")

    # 2. Verificar estrutura de diretórios
    print("\n📂 2. Verificando Estrutura de Diretórios...")
    dirs_needed = ["scripts", "skills", "templates", "output_payloads"]
    for d in dirs_needed:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"   [Criado] diretório ./{d}/")
        else:
            print(f"   [OK] diretório ./{d}/")

    print("\n✅ Ambiente pronto para uso pelo Claude.")
    print("👉 Você já pode iniciar a navegação das skills ou usar /dfc [TICKER].")

if __name__ == "__main__":
    main()
