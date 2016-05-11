# Code and Data Accompanying the Paper "Using Sequence Similarity Networks to Identify Partial Cognates in Multilingual Wordlists"

This repository offers code and data to replicate the analyses
underlying the paper "Using Sequence Similarity Networks to Identify
Partial Cognates in Multilingual Wordlists" by Johann-Mattis List,
Philippe Lopez, and Eric Bapteste (Proceedings of ACL 2016: Short
Papers).

## Requirements

In order to run all the analyses in this repository, please make sure
that the following requirements are fulfilled, and you have a Python3
installation version 3.4 or higher, along with the following packages
(and their major dependencies):

* lingpy, http://lingpy.org, version 2.5
* igraph, http://igraph.org, verson 0.6.5 or higher

Further requirements should be covered along with LingPy. If you
encounter difficulties, don't hesitate to ask us (<info@lingpy.org>).

## General information on source code

The source code we originally wrote for the paper was intended as a
plugin for the lingpy library. In the meantime, however, we managed to
integrate it fully into lingpy, so that the source code in this
repository is reduced to loading LingPy in its 2.5 and higher version,
and executing the algorithm. If you are interested in the details of
the algorithm, please turn to the LingPy software package, or visit us
at GitHub: http://github.com/lingpy/lingpy.

## Files in the Repository

The file structure in this repository should be relatively straighforward to
understand. Note that the BIN-files in the data-folder are frozen versions of
time-consuming LexStat-calculations, which are needed to exactly repeat our
analysis, since due to the shuffling procedure in the LexStat method, the
results can at times vary. 

## Information on the Structure of the Benchmark Data

The benchmark data tries to follow up some general ideas of the
[cldf](http://github.com/glottobank/cldf) format specification for
cross-linguistic data formats, but it remains still more in the LingPy style
than in pure CLDF form. Don't hesitate to ask us when encountering difficulties
in understanding the ideas behind the encoding.

## Data on Morpheme Distributions in Basic Words of Chinese Dialects

The data was originally taken from Hamed and Wang (2006) and supplemented again
in tab-separated format in List (2015, Bulletin of Chinese Linguistics). The
script morphemes.py calculates the number of morphemes for nouns and for all
words in the dataset. Since the annotation of partial cognacy was not
consistent in either of the original sources, we refined it and added our
analysis in the column "partial". In order to run the analysis, simply use the
make file:

```shell
$ make morphemes
```

Alternatively, run the Python script manually:

```python
$ python3 C_morphemes.py
```

The results should look as follows:

```text
Nouns consisting of 1 morpheme(s) 0.5077
Nouns consisting of 2 morpheme(s) 0.4390
Nouns consisting of 3 morpheme(s) 0.0488
Nouns consisting of 4 morpheme(s) 0.0041
Nouns consisting of 5 morpheme(s) 0.0005

Words consisting of 1 morpheme(s) 0.6778
Words consisting of 2 morpheme(s) 0.2876
Words consisting of 3 morpheme(s) 0.0316
Words consisting of 4 morpheme(s) 0.0028
Words consisting of 5 morpheme(s) 0.0002
```

So, as a result, you can see that almost 50% of the nouns in the data consist
of two or more morphemes, and also that more of 30% of all words in the data
are multi-morphemic. 

## Main Analysis of the Paper

The main analysis consists of two steps: 

1. basic analysis of partial and classical cognate detection and computation of evaluation scores
2. plotting of the data

In order to run the main analysis of the paper, simply use the make file

```shell
$ make all
```

In order to run only the plots (using the results as they were computed by our analysis), run:

```shell
$ make plot
```

In order to run only the cognate detection analysis, run:

```shell
$ make analysis
```

You can likewise run the analysis and the plots by invoking the two Python scripts analysis.py and plot.py.

The results in this analysis exceed those shown in the paper:

* in addition to strict coding of partial cognates, loose coding is also tested

We didn't report the results for this in the paper, since they do not differ
much from the strict comparison, and since there is only limited space, but you
may want to compare them against the other results.


