Word Embedding
===============================================

For technical details, please read my blog: [Chinese version](https://medium.com/@black_swan/%E7%94%A8%E7%B6%AD%E5%9F%BA%E8%AA%9E%E6%96%99%E8%A8%93%E7%B7%B4-word2vec-%E5%92%8C-fasttext-embedding-25ede5b15994) [English version](https://medium.com/@black_swan/how-to-train-word2vec-and-fasttext-embedding-on-wikipedia-corpus-9e8ac45a0c0a) 

Environment setup:
```
virtualenv __ -p python3
source __/bin/activate
pip install -r requirement.txt
```

Train word embedding on latest wikidump:
```
python train.py --lang en --model word2vec --size 300 --output data/en_wiki_word2vec_300.txt
--lang: en for English, zh for Chinese
--model: word2vec or fasttext
--size: number of dimension of trained word embedding
--output: path to save trained word embedding
```

Visualization of trained embedding (for English and Chinese only):
```
python demo.py --lang en --output data/en_wiki_word2vec_300.txt
--lang: en for English, zh for Chinese
--output: path for trained word embedding
```

Pretrained word embedding:

| | Chinese | English |
|---|---|---|
| Word2Vec| [Download](https://drive.google.com/file/d/1rY9SMmYsgz0is3fgGkSQn3nDwc92ygd5/view?usp=sharing) | [Download](https://drive.google.com/file/d/1F9pndKlaMCRWp9awvQsoC5XLeRANclnV/view?usp=sharing) |
| FastText| [Download](https://drive.google.com/file/d/12o6EFoQGpaVhGwYrqvoXFiX__VG7-Uab/view?usp=sharing) | [Download](https://drive.google.com/file/d/1U3rYodGoo6BRzuOA53WBY9OY_QaWZcey/view?usp=sharing) |
