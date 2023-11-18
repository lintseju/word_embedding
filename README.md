# Word Embedding

Sample code for training Word2Vec and FastText using wiki corpus and their pretrained word embedding.

For technical details, please read my blog: [Chinese version](https://writings.jigfopsda.com/zh/posts/2019/wiki_word2vec_fasttext/) [English version](https://writings.jigfopsda.com/en/posts/2019/wiki_word2vec_fasttext/) 

## Environment Setup

I tested the code using Python 3.9, it may work on other Python version, but not guaranteed. Use `poetry` to setup the environment is recommended.

### Poetry (recommended)

```bash
pip install poetry
poetry install
```

### Pip

```bash
virtualenv .venv -p python3
source .venv/bin/activate
pip install -r requirement.txt
```

## Train Word Embedding on Latest Wikidump

```bash
poetry run python train.py --lang en --model word2vec --size 300 --output data/en_wiki_word2vec_300.txt
--lang: en for English, zh for Chinese
--model: word2vec or fasttext
--size: number of dimension of trained word embedding
--output: path to save trained word embedding
```

If you are using pip, please run:

```bash
python train.py --lang en --model word2vec --size 300 --output data/en_wiki_word2vec_300.txt
```

## Visualize the Trained Embedding:

The visualization supports only Chinese and English.

```bash
poetry run python demo.py --lang en --output data/en_wiki_word2vec_300.txt
--lang: en for English, zh for Chinese
--output: path for trained word embedding
```

If you are using pip, please run:
```bash
python demo.py --lang en --output data/en_wiki_word2vec_300.txt
```
## Pretrained Word Embedding:

| | Chinese | English |
|---|---|---|
| Word2Vec| [Download](https://drive.google.com/file/d/1rY9SMmYsgz0is3fgGkSQn3nDwc92ygd5/view?usp=sharing) | [Download](https://drive.google.com/file/d/12fkBMFubpg5oduN4KCTy5nHlHhOPObKr/view?usp=sharing) |
| FastText| [Download](https://drive.google.com/file/d/12o6EFoQGpaVhGwYrqvoXFiX__VG7-Uab/view?usp=sharing) | [Download](https://drive.google.com/file/d/1O8ck-y5Fw9llD3OwxDMah9nu4NcyNX54/view?usp=sharing) |
