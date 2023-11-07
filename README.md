Word Embedding
===============================================

For technical details, please read my blog: [Chinese version](https://writings.jigfopsda.com/zh/posts/2019/wiki_word2vec_fasttext/) [English version](https://writings.jigfopsda.com/en/posts/2019/wiki_word2vec_fasttext/) 

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
| Word2Vec| [Download](https://drive.google.com/file/d/1rY9SMmYsgz0is3fgGkSQn3nDwc92ygd5/view?usp=sharing) | [Download](https://drive.google.com/file/d/12fkBMFubpg5oduN4KCTy5nHlHhOPObKr/view?usp=sharing) |
| FastText| [Download](https://drive.google.com/file/d/12o6EFoQGpaVhGwYrqvoXFiX__VG7-Uab/view?usp=sharing) | [Download](https://drive.google.com/file/d/1O8ck-y5Fw9llD3OwxDMah9nu4NcyNX54/view?usp=sharing) |
