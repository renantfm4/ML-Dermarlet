
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

## 📦 Requisitos

- Node.js >= 14
- Yarn
- Expo CLI (`npm install -g expo-cli`)
- Docker (opcional)
- Python 3.8+ (para backend e Airflow, se for usar)

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

  
---

## 🚀 Como Executar

### Localmente (sem Docker)

1. Instale as dependências do frontend:

```bash
yarn install
Inicie o servidor Expo:

bash
Copiar
Editar
yarn start
Use o app Expo Go para testar no seu celular ou configure um emulador Android/iOS.

```
---

### Com Docker

1. Construa a imagem:

```bash
docker build -t ml-dermarlet .
```

2. Execute o container:

```bash
docker run -p 19000:19000 ml-dermarlet
```

> Acesse pelo QR Code no terminal ou manualmente usando o IP da máquina host.

---

## 🐳 Dockerfile  (EXEMPLO POIS AINDA NÃO EXISTE)

```Dockerfile
FROM node:14

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 19000

CMD ["yarn", "start"]
```

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
| `1.0`  |23/04/2025| Adicionando descrição, link para gitpage e como rodar aplicação | [Esther Sena](https://github.com/esmsena) e [Davi Araújo](https://github.com/dcasseb) |   |
| `1.1`  |25/04/2025| Adicionando as pastas no tópico de Estruturas do Repositório | [Renan Araújo](https://github.com/renantfm4)  |   |
| `1.2`  |25/04/2025| Atualizando o tópico de Estruturas do Repositório e adicionando os topicos Requisitos, Como Executar Localmente (sem Docker), Com Docker, Dockerfile e Licença | [Esther Sena](https://github.com/esmsena) |   |

