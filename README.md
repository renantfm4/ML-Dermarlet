
# 🤖 DermAlert - Comunidade Machine Learning

A aplicação  [DermAlert](https://github.com/DermAlert/dermalert.github.io) é um aplicativo mobile multiplataforma desenvolvido com React Native, com suporte do Expo, Redux Toolkit para gerenciamento de estado global e React Navigation para navegação entre telas. O app tem como objetivo principal facilitar o registro, avaliação e acompanhamento clínico de pacientes com lesões dermatológicas, especialmente voltado para o apoio ao diagnóstico de câncer de pele.

---

## 📌 Objetivo

Centralizar e organizar:
- Modelos de Machine Learning utilizados no projeto
- Notebooks de experimentação
- Pipelines automatizadas
- Avaliações, métricas e documentação das decisões técnicas

---

## 📁 Estrutura do Repositório

```bash
├── config/                     # Arquivos de configuração do projeto
├── dags/                       # Definições de DAGs para orquestração com Airflow
├── data/                       # Dados do projeto, incluindo imagens divididas em treino e teste
├── docs/                       # Documentação em Markdown para MkDocs
├── src/                        # Código-fonte principal
├── tests/                      # Testes automatizados
├── .gitignore                  # Arquivos e pastas ignorados pelo Git
├── LICENSE                     # Licença do projeto
├── README.md                   # Documentação principal do repositório
├── Dockerfile                  # Imagem Docker do frontend (Expo) (ADD FUTURAMENTE)
├── package.json                # Dependências JS   (ADD FUTURAMENTE)
├── yarn.lock                      (ADD FUTURAMENTE)
├── requirements.txt            # Dependências do projeto
```

---

## 🚀 Tecnologias Utilizadas

- `Python 3.10+`
- `TensorFlow` / `Keras` ou `PyTorch`
- `Scikit-learn`
- `Pillow`
- `OpenCV`
- `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`
- `MLflow` / `DVC`
- `Airflow`
- `Flask` / `FastAPI`

---
## Documentação Técnica

Toda a documentação técnica do projeto está disponível na [GitHub Pages do projeto](https://www.dermalert.ai/land/dist/index.html).  

Lá você encontra:

- 📦 Como clonar e rodar o projeto localmente  
- 🚀 Guia de contribuição para colaboradores  
- 📡 Detalhamento das rotas da API backend  
- ⚙️ Estrutura e arquitetura da aplicação  
- 🧪 Boas práticas e padrões adotados  
- 📖 Outras informações técnicas relevantes

Acesse e contribua! 😉

----

## 🧪 Como Executar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/DermAlert/ml.git
cd ml

# 2. Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## 🤝 Como Contribuir

Confira o [guia de contribuição](https://www.dermalert.ai/guia-de-contribuicao/) para saber como colaborar!

Contribuições bem-vindas:

- :sparkles: feat: nova funcionalidade
- :bug: fix: correção de bug
- :books: docs: alterações na documentação
- :art: style: mudanças visuais ou de formatação
- :recycle: refactor: refatoração sem mudança de funcionalidade
- :white_check_mark: test: criação ou alteração de testes
- :wrench: chore: tarefas administrativas

----

## 📦 Requisitos

- Python 3.10+
- Virtualenv (opcional, mas recomendado)
- Docker (para ambiente containerizado, opcional)
- Git

---
  
## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/renantfm4/ML-Dermarlet.git
cd ML-Dermarlet
```

### 2. Crie um ambiente virtual e ative

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute um exemplo de pipeline ou notebook

```bash
python src/train/train_pipeline.py
```

Ou abra um notebook em:

```bash
jupyter notebook
```

---

## 🐳 Dockerfile

O projeto já está configurado com suporte Docker. Utilize o Dockerfile abaixo para construir o ambiente em contêineres.

```Dockerfile
# Use uma imagem base do Node.js
FROM node:14

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo package.json e yarn.lock
COPY package.json yarn.lock ./

# Instale as dependências do projeto
RUN yarn install

# Copie todo o código para o container
COPY . .

# Exponha a porta 19000 (porta padrão do Expo)
EXPOSE 19000

# Comando para rodar o servidor Expo
CMD ["yarn", "start"]
```

---

### 🐳 Como Rodar com Docker

1. **Construa a imagem Docker**:

```bash
docker run -it --rm -p 8000:8000 ml-dermalert
```

2. **Execute o container**:

```bash
docker run -p 19000:19000 ml-dermarlet
```

Acesse o aplicativo usando o QR Code exibido no terminal ou manualmente pelo IP da máquina host
  
---

## 📎 Links Importantes

- [Site do projeto DermAlert](https://www.dermalert.ai/land/dist/index.html)
- [Repositório do Backend](https://github.com/DermAlert/dermalert-backend)
- [Repositório Frontend](https://github.com/DermAlert/dermalert-frontend)
- [Diretrizes Éticas de IA na Saúde – OMS](https://www.who.int/publications/i/item/9789240029200)

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor | Revisor |
| :----: | ---- | --------- | ----- | ------- |
| `1.0`  |23/04/2025| Adicionando descrição, link para gitpage e como rodar aplicação | [Esther Sena](https://github.com/esmsena) e [Davi Araújo](https://github.com/dcasseb) | [Renan Araújo](https://github.com/renantfm4)  |
| `1.1`  |25/04/2025| Adicionando as pastas no tópico de Estruturas do Repositório | [Renan Araújo](https://github.com/renantfm4)  | [Esther Sena](https://github.com/esmsena)  |
| `1.2`  |25/04/2025| Atualizando o tópico de Estruturas do Repositório e adicionando os topicos Requisitos, Como Executar Localmente (sem Docker), Com Docker, Dockerfile e Licença | [Esther Sena](https://github.com/esmsena) | [Renan Araújo](https://github.com/renantfm4) |
| `1.2`  |27/04/2025| Atualizando o tópico de Estruturas do Repositório e adicionando os topicos Requisitos, Como Executar Localmente (sem Docker), Com Docker e adicionando Como Rodar com Docker e excluíndo Dockerfile (EXEMPLO POIS AINDA NÃO EXISTE) | [Esther Sena](https://github.com/esmsena) |[Renan Araújo](https://github.com/renantfm4)   |
