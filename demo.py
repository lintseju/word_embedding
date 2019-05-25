import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import PCA


def find_k_nearest(source, vectors, k):
    norm1 = np.linalg.norm(source)
    norm2 = np.linalg.norm(vectors, axis=1)
    cosine_similarity = np.sum(source * vectors, axis=1) / norm1 / norm2
    return np.argsort(cosine_similarity)[::-1][1:(k + 1)]


def get_args():
    parser = argparse.ArgumentParser(description='Train embedding')
    parser.add_argument('--lang', type=str, default='en', help='language')
    parser.add_argument('--output', type=str, required=True, help='output for word vectors')
    return parser.parse_args()


def main():
    args = get_args()
    if args.lang == 'zh':
        demo_nearest = ['狗', '山', '迪士尼', '太陽', '羽毛球']
        demo_country = [
            ('法國', '巴黎'),
            ('英國', '倫敦'),
            ('德國', '柏林'),
            ('韓國', '首爾'),
            ('日本', '東京')
        ]
    elif args.lang == 'en':
        demo_nearest = ['dog', 'mountain', 'disney', 'sun', 'badminton']
        demo_country = [
            ('france', 'paris'),
            ('england', 'london'),
            ('germany', 'berlin'),
            ('korea', 'seoul'),
            ('japan', 'tokyo')
        ]
    else:
        logging.info('Only support language zh and en, %s not supported.', args.lang)
        return
    demo_country_en = [
        ('france', 'paris'),
        ('england', 'london'),
        ('germany', 'berlin'),
        ('korea', 'seoul'),
        ('japan', 'tokyo')
    ]

    # load word vector
    words = []
    vectors = []
    logging.info('Loading word vector')
    with open(args.output) as f:
        # skip first line
        f.readline()
        line = f.readline()
        while len(line) > 0:
            line = line.split(' ')
            words.append(line[0])
            vectors.append(np.array([float(x) for x in line[1:]]))
            line = f.readline()
    vectors = np.vstack(vectors)

    # demo word similarity
    k = 5
    for word in demo_nearest:
        word_index = words.index(word)
        k_nearest = find_k_nearest(vectors[word_index], vectors, k)
        logging.info('Nearest words of %s', word)
        for index in k_nearest:
            v1 = vectors[word_index, :]
            v2 = vectors[index, :]
            logging.info('word %s score %f', words[index], np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

    # demo word analogy
    x_pca = []
    for country, capital in demo_country:
        x_pca.append(vectors[words.index(country)])
        x_pca.append(vectors[words.index(capital)])

    # workaround for cannot show Chinese by matplotlib
    name_pca = []
    for country, capital in demo_country_en:
        name_pca.append(country)
        name_pca.append(capital)

    pca = PCA(n_components=2)
    x_plot = pca.fit_transform(np.vstack(x_pca))

    fig, ax = plt.subplots()
    ax.scatter(x_plot[:, 0], x_plot[:, 1])
    for i, txt in enumerate(name_pca):
        ax.annotate(txt, (x_plot[i, 0], x_plot[i, 1]))
    fig.savefig(args.output.replace('txt', 'png'))

    logging.info('Done')


if __name__ == "__main__":
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)
    main()
