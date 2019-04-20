#! /usr/bin/env python
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
    lexicon = lexicons.load_lexicon("dic_sent", remove_neutral=True)
    pos_seeds, neg_seeds = seeds.hist_seeds()

    num_lines = sum(1 for line in open(
        'socialsent/data/example_embeddings/data_emo.txt'))

    for f, t in zip(list(range(0, num_lines, 5000)), [x + 5000 for x in list(range(0, num_lines, 5000))]):
        if t > num_lines:
            t = num_lines
        embeddings = create_representation("GIGA", "socialsent/data/example_embeddings/data_emo.txt", set([x.encode('utf-8') for x in list(lexicon.keys())]).union(pos_seeds).union(neg_seeds), f, t)
        eval_words = [word for word in embeddings.iw
                    if not word in pos_seeds
                    and not word in neg_seeds]
    polarities = graph_propagate(embeddings, pos_seeds, neg_seeds)
    
        import codecs
        import json
        with codecs.open('socialsent/data/polarities/dic_sent_model_unseen_{part}.json'.format(part=f), 'w', "utf-8") as fp:
            json.dump(polarities, fp, ensure_ascii=False)
        print(polarities)
        type(lexicon)
        
    acc, auc, avg_per = binary_metrics(polarities, lexicon, eval_words)
    print("Accuracy with best threshold: {:0.2f}".format(acc))
    