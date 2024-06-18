# Dependências necessárias:

Script Python que converte URLs do Youtube para um arquivo MP3.

    Python: O ambiente de execução para o script.
    yt-dlp: Ferramenta para baixar vídeos do YouTube.
    ffmpeg: Software para manipulação de áudio e vídeo.

Instruções para instalação:
### 1. Instalar Python (se ainda não estiver instalado):

**Windows**:
        Baixe o instalador do Python em python.org.
        Durante a instalação, marque a opção "Adicionar Python ao PATH".

**macOS**:
        Python geralmente já está instalado. Verifique digitando python3 --version no terminal.
        Se necessário, instale o Homebrew em brew.sh, e então execute brew install python3.

**Linux**:
        Python geralmente já está instalado. Verifique digitando python3 --version no terminal.
        Use o gerenciador de pacotes do seu sistema (como apt, yum, dnf) para instalar Python.

### 2. Instalar yt-dlp:

Execute o seguinte comando no terminal:

```pip install yt-dlp```

### 3. Instalar ffmpeg:

**Windows**:
        Baixe a versão estática do ffmpeg em ffmpeg.org.
        Extraia o arquivo ZIP e adicione o caminho da pasta bin ao PATH do sistema.

**macOS**:
    Instale o Homebrew se ainda não tiver:
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Use o Homebrew para instalar o ffmpeg:

    brew install ffmpeg

**Linux**: Use o gerenciador de pacotes do seu sistema para instalar ffmpeg:
        
*Debian/Ubuntu*:

```sudo apt update```

```sudo apt install ffmpeg```


*Fedora*:

```sudo dnf install ffmpeg```

*Arch Linux*:

```sudo pacman -S ffmpeg```

Verificar a instalação:

Após a instalação, você pode verificar se tudo está configurado corretamente:

    Python: Digite python3 --version para verificar a versão instalada.
    yt-dlp: Execute yt-dlp --version para verificar se yt-dlp está instalado corretamente.
    ffmpeg: Verifique com ffmpeg -version para garantir que o ffmpeg esteja instalado e funcionando.

Com todas essas dependências instaladas, você poderá executar o script.
