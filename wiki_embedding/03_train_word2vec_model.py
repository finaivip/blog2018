# -*- coding: utf-8  -*-
#使用gensim word2vec训练脚本获取词向量

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告

import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

'''
  使用gensim中的Word2Vec进行训练
    size: 词向量的纬度；
    window: 预测该距离范围内的其他词；
    min_count: 如果语料中的词的数量小于该值，忽略该词；
    
  执行方式: python3 03_train_word2vec_model.py
  注意：
'''


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp为输入语料, outp1 为输出模型, outp2为原始c版本word2vec的vector格式的模型
    fdir = ''
    inp = fdir + 'wiki.zh.simp.seg.txt'
    outp1 = fdir + 'wiki.zh.text.model'
    outp2 = fdir + 'wiki.zh.text.vector'

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    # 保存模型
    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)


