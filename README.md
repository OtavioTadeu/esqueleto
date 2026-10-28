# 💀 Esqueleto Prank (Esqueleto na Tela)

Um script divertido em Python que faz um esqueleto animado atravessar correndo a tela do seu computador em intervalos aleatórios de tempo.

O programa roda silenciosamente em segundo plano (sem exibir tela de terminal), com fundo transparente sobreposto a qualquer janela aberta.

---

## 📁 Estrutura do Projeto

```text
esqueleto-prank/
├── esqueleto.pyw        # Script principal em Python
├── esqueleto.gif        # Imagem animada do esqueleto
├── requirements.txt     # Dependências (PyInstaller)
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo de documentação
```

---

## 📋 Pré-requisitos

- **Sistema Operacional:** Windows 10 ou 11
- **Python:** Versão 3.8 ou superior ([Download Python oficial](https://www.python.org/downloads/))
  > ⚠️ Durante a instalação do Python no Windows, certifique-se de marcar a opção **"Add python.exe to PATH"** e a opção de instalar o **tcl/tk and IDLE** (já vem marcada por padrão).

---

## 📥 Como Baixar o Projeto

### Opção 1: Clonando via Git (Recomendado)
Abra o terminal (Prompt de Comando ou PowerShell) e execute:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### Opção 2: Download direto em arquivo ZIP
1. Clique no botão verde **Code** no topo desta página do GitHub.
2. Selecione **Download ZIP**.
3. Extraia o conteúdo do arquivo `.zip` em uma pasta de sua preferência.

---

## 🚀 Como Executar Diretamente (Modo Python)

Você pode testar e rodar o projeto diretamente sem compilar:

1. Dê um **duplo clique** sobre o arquivo `esqueleto.pyw`.
   - *Como a extensão é `.pyw`, ele será executado usando o `pythonw.exe`, rodando silenciosamente em segundo plano sem janela de console.*
2. Ou via terminal na pasta do projeto:
   ```bash
   python esqueleto.pyw
   ```

---

## 🛠️ Como Transformar em Executável (.exe)

Para poder rodar o programa em qualquer computador Windows sem precisar ter o Python instalado, você pode compilá-lo em um arquivo `.exe` usando a biblioteca **PyInstaller**.

### 1. Instalar o PyInstaller
Abra o Prompt de Comando ou PowerShell na pasta do projeto e instale o PyInstaller:
```bash
pip install pyinstaller
```

### 2. Compilar com o GIF Embutido (Recomendado)
Este comando cria um executável único que já traz o arquivo `esqueleto.gif` embutido por dentro do `.exe`. Assim você não precisa manter o arquivo `.gif` solto na mesma pasta:

```bash
pyinstaller --onefile --noconsole --add-data "esqueleto.gif;." esqueleto.pyw
```

#### O que cada parâmetro significa:
- `--onefile` (ou `-F`): Empacota tudo em um único arquivo `.exe`.
- `--noconsole` (ou `-w`): Oculta a janela preta do terminal do Windows.
- `--add-data "esqueleto.gif;."`: Inclui a imagem `esqueleto.gif` dentro do executável. O separador `;` é usado no Windows (`arquivo_origem;destino_interno`).

### 3. Localizar o Executável Gerado
Após a conclusão do processo:
1. Abra a pasta `dist` gerada dentro do diretório do projeto.
2. Lá estará o arquivo `esqueleto.exe`.
3. Você pode copiar este `esqueleto.exe` para onde quiser ou enviá-lo para seus amigos!

> 💡 **Nota:** As pastas `build/` e o arquivo `esqueleto.spec` gerados durante a compilação são apenas temporários e podem ser excluídos com segurança se desejar.

---

## 🛑 Como Encerrar o Programa

Como o programa executa em segundo plano sem nenhuma janela persistente na barra de tarefas:

1. Pressione as teclas `Ctrl` + `Shift` + `Esc` para abrir o **Gerenciador de Tarefas**.
2. Na aba **Processos**:
   - Se estiver rodando o executável: procure por **`esqueleto.exe`**.
   - Se estiver rodando o script Python: procure por **`pythonw.exe`** ou **`Python`**.
3. Clique com o botão direito sobre o processo e selecione **Finalizar Tarefa**.

---

## ⚙️ Personalização das Configurações

Você pode abrir o arquivo `esqueleto.pyw` em qualquer editor de texto (como Bloco de Notas ou VS Code) e alterar os valores nas linhas de configuração:

```python
# ================= CONFIGURAÇÕES =================
GIF_FILE = resource_path("esqueleto.gif")  # Nome do arquivo de animação
MIN_MINUTES = 1                           # Tempo mínimo de espera (em minutos)
MAX_MINUTES = 1                           # Tempo máximo de espera (em minutos)
TEMPO_TRAVESSIA_MS = 500                  # Duração do susto na tela em ms (500ms = meio segundo)
FRAME_DELAY_MS = 30                       # Intervalo entre os quadros da animação
# =================================================
```

- **Para alterar o intervalo:** mude `MIN_MINUTES` e `MAX_MINUTES` (ex: `MIN_MINUTES = 5` e `MAX_MINUTES = 15` para aparecer aleatoriamente entre 5 e 15 minutos).
- **Para alterar a velocidade:** diminua `TEMPO_TRAVESSIA_MS` para o esqueleto passar mais rápido, ou aumente para que passe mais devagar.

---

## 📤 Como Subir este Projeto para o Seu GitHub

Se você é o criador do projeto e quer colocá-lo no seu próprio GitHub pela primeira vez:

1. Acesse [github.com/new](https://github.com/new) e crie um novo repositório (ex: `esqueleto-prank`). Deixe desmarcada a opção de adicionar README (já temos um pronto aqui).
2. Abra o terminal na pasta do projeto e execute os seguintes comandos:

```bash
git init
git add .
git commit -m "feat: versao inicial do esqueleto prank"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/esqueleto-prank.git
git push -u origin main
```
*(Substitua `SEU_USUARIO` e `esqueleto-prank` pelos dados do seu repositório no GitHub).*

### 🎁 Dica: Criando uma Release com o `.exe`
O arquivo `.exe` não deve ser enviado no repositório Git padrão para não pesar o repositório (ele já está no `.gitignore`). Para disponibilizá-lo para download direto no GitHub:
1. Vá até a página do seu repositório no GitHub.
2. No menu lateral direito, clique em **Releases** -> **Create a new release**.
3. Defina uma tag (ex: `v1.0.0`).
4. Arraste e solte o arquivo `esqueleto.exe` (da pasta `dist`) no campo de anexos (Attach binaries).
5. Clique em **Publish release**. Agora qualquer pessoa pode baixar o `.exe` pronto com apenas um clique!
