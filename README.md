# socialsent3

*Code and data for inducing domain-specific sentiment lexicons.*

Update for SocialSent package to use it with python3 and Russian language.

Now you can get sentiments using GIGA extention based on the word2vec embeddings.

## Install

```
!pip install git+https://github.com/olgasilyutina/socialsent3.git
```

## Lexicons for Russian language:

Лукашевич Н.В., Левчик А.В. Создание лексикона оценочных слов русского языка РуСентилекс // Труды конференции OSTIS-2016, С.377-382.

Seed words are the most frequent words from Russian twitter texts used in emopok repository.

## Limitations:

Not all functions are working stable. Most of the package scripts were converted to python3 using 2to3 package, 
so, if you try functions out of the example script, be ready to face with errors.

