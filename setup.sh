#!/bin/bash

# Atualize os pacotes e instale dependências do sistema
sudo apt-get update -y
sudo apt-get install -y build-essential python3-dev gcc libffi-dev

# Instale as dependências Python
pip install -r requirements.txt
