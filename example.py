#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import imp
stdin, stdout, stderr = sys.stdin, sys.stdout, sys.stderr
imp.reload(sys)
sys.stdin, sys.stdout, sys.stderr = stdin, stdout, stderr
sys.setdefaultencoding('utf-8')
from socialsent import seeds
from socialsent import lexicons
from socialsent.polarity_induction_methods import *
from socialsent.evaluate_methods import binary_metrics
from socialsent.representations.representation_factory import create_representation

if __name__ == "__main__":
    print("Evaluting SentProp with 100 dimensional GloVe embeddings")
    print("Evaluting only binary classification performance on General Inquirer lexicon")
    lexicon = lexicons.load_lexicon("dic_sent", remove_neutral=True)
    pos_seeds, neg_seeds = seeds.hist_seeds()
    # set(lexicon.keys().encode("utf-8")).union(pos_seeds).union(neg_seeds)

    num_lines = sum(1 for line in open(
        '~/socialsent-master/socialsent/data/example_embeddings/data_emo.txt'))

    for f, t in zip(list(range(0, num_lines, 5000)), [x + 5000 for x in list(range(0, num_lines, 5000))]):
        if t > num_lines:
            t = num_lines
        embeddings = create_representation("GIGA", "socialsent/data/example_embeddings/data_emo.txt", set([x.encode('utf-8') for x in list(lexicon.keys())]).union(pos_seeds).union(neg_seeds), f, t)
        eval_words = [word for word in embeddings.iw
                    if not word in pos_seeds
                    and not word in neg_seeds]
    #for word in embeddings.iw:
    #    print word 

    # Using SentProp with 10 neighbors and beta=0.99
    # polarities = random_walk(embeddings, pos_seeds, neg_seeds, beta=0.99, nn=10, sym=True, arccos=True)
        polarities = graph_propagate(embeddings, pos_seeds, neg_seeds)
    # polarities = label_propagate_probabilistic(embeddings, pos_seeds, neg_seeds)

        import codecs
        import json
        with codecs.open('~/dic_sent_model_unseen_{part}.json'.format(part=f), 'w', "utf-8") as fp:
            json.dump(polarities, fp, ensure_ascii=False)
        print(polarities)
    type(lexicon)
    # acc, auc, avg_per = binary_metrics(polarities, lexicon, eval_words)
    # print "Accuracy with best threshold: {:0.2f}".format(acc)
    # print "ROC AUC: {:0.2f}".format(auc)
    # print "Average precision score: {:0.2f}".format(avg_per)
    #
