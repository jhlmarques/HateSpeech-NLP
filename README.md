# HateSpeech-NLP
Repositório do trabalho final do curso NF01221 - Processamento de Linguagem Natural (PLN) 2024/2 (Prof. Dennis Giovani Balreira)

## Dataset Utilizados
[HateBR](https://github.com/franciellevargas/HateBR)
[ToldBR](https://github.com/joaoaleite/ToLD-Br)


## Instalação
Esse projeto utiliza o gerenciador de pacotes [miniconda3](https://docs.anaconda.com/miniconda/)

### Ambiente
A criação de ambiente é similar à fornecida pela biblioteca [simpletransformers](https://simpletransformers.ai/docs/installation/)
```
conda create -n hate_nlp python pandas tqdm nltk
conda activate hate_nlp
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip install simpletransformers
```
