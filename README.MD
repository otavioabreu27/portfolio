# Guia de instalação

## 1. Clone o repositório

```console
    git clone <url>
```

## 2. Crie um ambiente virtual

```console
    cd portfolio
    python -m venv <nome>
```

- Pode variar de so para so, em caso de erro utilize o código abaixo:

```console
    cd portfolio
    python3 -m venv <nome>
```

## 3. Ativando o ambiente
Agora que esta instalado vamos ativar o ambiente.

#### 3.1 CMD
No CMD navegue até a pasta /<nome>/Scripts e execute o código abaixo:

```console
   activate.bat
```

#### 3.2 PowerShell

```console
   .\<nome>\Scripts\Activate.ps1
```

#### 3.3 Linux Terminal / MacOS

```console
   source .\<nome>\bin\activate
```

## 4. Instalando pacotes

```console
   pip install -r requirements.txt
```

## 5. Rodando a aplicação

```console
   python app.py
```