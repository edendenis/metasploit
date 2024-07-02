#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `metasploit` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `metasploit` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `metasploit` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `metasploit`
# 
# O metasploit é uma poderosa ferramenta de análise de protocolos de rede de código aberto, amplamente utilizada para capturar e inspecionar o tráfego de rede em tempo real. Ele permite que os usuários analisem pacotes de dados transmitidos por uma rede e fornece informações detalhadas sobre o tráfego, incluindo protocolos, origens e destinos de pacotes e seu conteúdo. O metasploit é uma escolha valiosa para administradores de rede, engenheiros de segurança e profissionais de TI que precisam solucionar problemas de rede, diagnosticar problemas de desempenho e identificar possíveis ameaças de segurança. Sua interface de usuário robusta e recursos avançados o tornam uma ferramenta essencial para a análise de tráfego de rede em ambientes corporativos e de pesquisa.

# ## 1. Como configurar/instalar o `metasploit` no Linux Ubuntu [1]
# 
# Para configurar/instalar o `metasploit` no Linux Ubuntu, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `metasploit` no Ubuntu através do terminal, você pode seguir os seguintes passos:
# 
# 3. **Instale as Dependências:** O Metasploit requer algumas dependências para funcionar corretamente. Instale-as com o comando: `sudo apt install curl gpg software-properties-common`
# 
# 4. **Adicione o Repositório do Metasploit:** O Metasploit não está disponível nos repositórios padrão do Ubuntu, então você precisa adicionar o repositório oficial. Faça isso com o seguinte comando:
# 
#     ```
#     curl https://apt.metasploit.com/metasploit-framework.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/metasploit-framework-archive-keyring.gpg
#     echo "deb [signed-by=/usr/share/keyrings/metasploit-framework-archive-keyring.gpg] https://apt.metasploit.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/metasploit-framework.list
#     ```
# 
# 5. **Atualize a Lista de Pacotes Novamente:** Com o novo repositório adicionado, atualize a lista de pacotes: `sudo apt update -y`
# 
# 6. **Instale o Metasploit:** Agora, você pode instalar o Metasploit com o comando: `sudo snap install metasploit-framework`
# 
# 7. **Inicialize o Banco de Dados:** O Metasploit usa um banco de dados para armazenar informações. Inicialize o banco de dados com: `msfdb init`
# 
# 8. **Inicie o Metasploit:** Para iniciar o Metasploit, use o comando: `msfconsole`
# 
# Isso abrirá a interface do console do Metasploit, onde você pode começar a usar as ferramentas e recursos disponíveis. Lembre-se de que o Metasploit é uma ferramenta poderosa, usada principalmente para testes de penetração e auditorias de segurança. É importante usá-lo de forma ética e responsável.

# ### 1.1 Código completo para configurar/instalar
# 
# Para instalar o `Metasploit` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean                                                            
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install curl gpg software-properties-common
#     curl https://apt.metasploit.com/metasploit-framework.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/metasploit-framework-archive-keyring.gpg
#     echo "deb [signed-by=/usr/share/keyrings/metasploit-framework-archive-keyring.gpg] https://apt.metasploit.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/metasploit-framework.list
#     sudo apt update -y
#     sudo snap install metasploit-framework
#     msfdb init
#     msfconsole
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar metasploit no ubuntu.*** Disponível em: <https://chat.openai.com/c/6a4e7077-eb3a-4ae6-a931-fbb5efa8d79f> (texto adaptado). Acessado em: 28/11/2023 23:30.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 28/11/2023 23:30.
# 
