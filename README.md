# Conversor de Imagens para Vídeos e Vice-Versa

Este projeto é um script em Python que permite converter uma série de imagens em um vídeo, além de extrair frames de um vídeo e salvar como imagens.
É útil para diversas aplicações, como edição de vídeos, processamento de imagens e automação de tarefas.

## Funcionalidades

- **Converter imagens para vídeo:** Cria um vídeo a partir de uma sequência de imagens.
- **Extrair frames de vídeo:** Salva cada frame de um vídeo como uma imagem separada.

## Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV**

## Instalação

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd nome-do-repositorio
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

### Converter Imagens para Vídeo

1. Organize as imagens que deseja converter em um diretório. Certifique-se de que os arquivos estejam nomeados sequencialmente (ex.: `frame1.jpg`, `frame2.jpg`, etc.).
2. Execute o seguinte comando:
    ```bash
    python images_to_video.py --input-dir caminho_para_imagens --output video.mp4 --fps 30
    ```
    - `--input-dir`: Caminho para a pasta que contém as imagens.
    - `--output`: Nome do arquivo de vídeo a ser gerado.
    - `--fps`: Frames por segundo (opcional, padrão é 30).

### Extrair Frames de um Vídeo

1. Para extrair frames de um vídeo, use o comando:
    ```bash
    python video_to_images.py --input video.mp4 --output-dir caminho_para_salvar_imagens
    ```
    - `--input`: Caminho para o vídeo que deseja extrair os frames.
    - `--output-dir`: Diretório onde as imagens serão salvas.

## Exemplos

### Converter imagens para vídeo
```bash
python images_to_video.py --input-dir ./imagens/ --output video_final.mp4 --fps 24



