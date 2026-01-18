# 🤖 Bot de Automação de Cadastro de Produtos

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![PyAutoGUI](https://img.shields.io/badge/Lib-PyAutoGUI-green.svg)](https://pyautogui.readthedocs.io/)
[![Pandas](https://img.shields.io/badge/Lib-Pandas-orange.svg)](https://pandas.pydata.org/)

## 📝 Descrição
Este projeto é um bot inteligente desenvolvido em Python para automatizar o processo de cadastro de produtos em sistemas web. Ele elimina o trabalho manual repetitivo, lendo dados de uma base externa (CSV) e preenchendo os campos de forma ultra-rápida utilizando simulação de teclado e mouse.

---

## 🚀 Funcionalidades
* **Integração com Base de Dados:** Lê automaticamente arquivos `.csv` com centenas de produtos.
* **Automação de Navegação:** Abre o navegador, acessa o link do sistema e realiza o login.
* **Cadastro em Loop:** Preenche múltiplos campos e repete o processo até finalizar a lista.
* **Segurança:** Configurado com `PAUSE` para evitar bloqueios e `FAILSAFE` para interrupção de emergência.

---

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal.
* **PyAutoGUI:** Para controle de mouse, teclado e tela.
* **Pandas:** Para manipulação e análise da base de dados.
* **Time:** Para controle de intervalos de execução.

---

## ⚙️ Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Pingowg/boot-automacao-python.git](https://github.com/Pingowg/boot-automacao-python.git)
Instale as dependências:

Bash

pip install pyautogui pandas numpy
Prepare a base de dados: Certifique-se de que o arquivo produtos.csv está na mesma pasta do script.

Execute o bot:

Bash

python codigo.py
⚠️ Atenção com a Resolução
Este bot utiliza coordenadas de pixel fixas. Se o seu monitor não for 1920x1080, você precisará:

Rodar o arquivo auxiliar.py.

Posicionar o mouse sobre os campos desejados para capturar as novas coordenadas.

Atualizar os valores de X e Y no arquivo codigo.py.

👤 Autor
Desenvolvido por Pingowg. Conecte-se comigo!



4.  Cole o texto acima, ajuste o que desejar e clique em **Commit changes** (o botão verde no topo ou no final da página).

**Gostaria que eu criasse um GIF ou uma imagem personalizada para você colocar no topo desse README e deixá-lo ainda mais visual?**
