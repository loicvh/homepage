
I have no word
______________

.. raw:: html

    <style> .red {color:#aa0060; font-weight:bold; font-size:16px} </style>
    <style> .blue {color:#023891; font-weight:bold; font-size:16px} </style>

.. role:: red
.. role:: blue

Words, and more specifically their meaning, have always raised debates and questions among philosophers and other thinkers. This is one of the reason why philosophy often seems difficult to grasp, the sentences are long and the word tedious; this is because philosophers want to be *right*.

**Precision** and **accuracy** are required to explain the challenging concepts and ideas that we encounter every day or that pop into our minds. How, using words, would you describe precisely and accurately: 

* The difference between the :red:`red` and :blue:`blue` colours;

* The feelings towards loved ones;

* The comfort of being in your warm bed when the thunder rumbles and the rain hits the windows;

* The parfume of freshly cut grass.

Obviously, it is possible to give *some* interpretations to these examples. One could say that *"blue is more deep than red"*, or "*freshly cut grass smell like spring*" but these descriptions are neither precise nor accurate. 

In the following, let us try to speak of *semantic*, and maybe the link with the mathematics.

As a good mathematician or as a good semanticist (semantician?), let us define *what is* semantic. According to wikipedia,

.. topic:: Semantic

    Semantics (from Ancient Greek: σημαντικός sēmantikós, "significant") is the linguistic and philosophical study of meaning in language, programming languages, formal logic, and semiotics.
    It is concerned with the relationship between signifiers—like words, phrases, signs, and symbols—and what they stand for in reality, their denotation.

Equipped with this definition, let's look at why this relationship is not working as expected. 

The inherent problem of the language
====================================

Let us first try to understand *what are the issues of the words we use*. It seems clear, and we will try to look at this issue as a mathematician later on, that we do not have enough words to describe the infinite realities we experiment. Is a wooden chair the same object as a plastic chair? Are these two chairs exactly equivalent? It seems wrong to call both of these "chair", while they obviously are not a hundred percent equal.

The second issue is due to context, words have different meanings in different region of the world or at different time; "loyalty" is probably a different concept now than it was in the Middle Ages, "brother" has different meaning depending on the community.

Another issue, linked to the first one, is the multi-meaning nature of the words. A letter is one-in-26, or received in the mail. 

.. topic:: Letter vs. letter

    When I say: *"I love reading letters"*, you have **no** way of knowing which letters I am talking about. You could *guess* with the context but you are never sure.

Another problem, which has been raised several times, is the issue of traduction. Translator will wittingly or unwittingly introduce different meaning in the translated version. This explains why some people learn German -- or any other language -- with the acknowledge aim of reading the *true* word of Kant or Nietzsche.

This list is obviously not exhaustive and many more communication problem can be linked with the limitation of our languages. Let us see some of the workaround that has been used.

Some tricks to limit the misunderstanding
========================================================


To address this inherent problem of our limited language, philosophers *define* -- or at least try to define -- what they mean with the words they use.

In "What is authority" from [#f1]_, Hannah Arendt starts by explaining what *was* and what *is not* authority. Her idea is first to deconstruct what the reader thinks of the authority. After this *tabula rasa* and on fresh basis, it is easier to explain the concept. In a similar way, Socrates usually begins his elenchus with "*what is*", which has been seen as a search of a formal definition of the studied concept, *e.g.*, "what is piety?" [#f2]_. In this way, the interlocutor realized that he did not grasp the *true* concept of piety.

A straight forward way of dealing with disambiguation is to use formal definitions. In the first page of the introduction of "*The Critique of Pure Reason*", Immanuel Kant already describes what he exactly meant by "*a priori* knowledge":

.. topic:: Kant's definition of '*a priori* knowledge'

    In this book, therefore, I will understand by '*a priori* knowledge' not knowledge that comes independently of this or that experience, but rather what occurs absolutely independently of all experience. Opposed to it there is empirical knowledge, i.e. knowledge that is possible only *a posteriori*, through experience. An item of *a priori* knowledge is called 'pure' if nothing empirical is mixed into it. The proposition 'Every alteration has its cause' is an *a priori* proposition, but it isn’t pure because the concept of alteration has to be taken from experience [#Kant_critique]_.

From the beginning, Kant is afraid that the reader does not understand correctly his words, which have already been translated here.

A third way of making sure that the correct message get passed is to create word or to use word from another language. This explains strange words -- often inspired from ancient Greek -- as the cogito, the conatus, the logos, the monad, and so on. Starting from such a word, the reader **must** use the definition given by the author with no other connotation.


More recently the massive use of social media, and henceforth written conversations, surges the need of a way of disambiguate our messages; this leads to the smiley. A simple character can make the clear distinction between the following sentences.

* I am going to the hospital! :)
* I am going to the hospital. :(

Note that here punctuation has also a role in the appeared meaning of the sentence.


On the limited power of the language
====================================

In the following, we will try to prove the following proposition:

    **Proposition 1 (P1): Written languages consisted of a given alphabet cannot explain unambiguously any concept**

Note that as rigorous we would like to be, this proposition can not be proven: if (P1) is true than the (written) proof (in English) will be ambiguous. Let us try to give some intuition about why this is probably true.

On the countability of words
----------------------------
Using the 26 letters of the latin alphabet, it is possible to build *a lot* of words. "Chair" is a valid word, as is "Chiar", and "Chaaaaaaaaair", and provided that we chose a meaning to these words. It seems fair that an *infinite* number of words can be constructed. But how large is this infinity?

Infinity in arithmetic
^^^^^^^^^^^^^^^^^^^^^^

In mathematics, infinities can be smaller than others. For instance, we can distinct countably infinite set and uncountably infinite set. An example of the first one is "the set of even numbers", and an example of the second one is "the set of real number between 0 and 1". More specifically, we say that a set is countably infinite if there is a one-to-one *correspondence* -- or bijection -- between this set and the set of natural numbers (0, 1, 2, ...), and we say that a set X is uncountably infinite if there is no one-to-one *function* -- or injection between X  and the set of natural numbers.

Proving that the set of even number, :math:`E`, is countable is really easy and the bijection is the following: it suffices to match every positive even number to itself and every negative even number to its opposite minus one.

.. math:: f: E \to \mathbb{N} : n \mapsto     \begin{cases}
      0, & \text{if}\ n=0; \\
      n, & \text{else if n even;} \\
      -n-1, & \text{else.}
    \end{cases} 

Computing the first elements of the bijection gives

+-------------------+-------------------+
| :math:`E`         | :math:`\mathbb{N}`|
+===================+===================+
| 0                 |  0                | 
+-------------------+-------------------+
| -2                |  1                | 
+-------------------+-------------------+
| 2                 |  2                | 
+-------------------+-------------------+
| -4                |  3                | 
+-------------------+-------------------+
| 4                 |  4                | 
+-------------------+-------------------+

The proof of the second proposition is a bit more tedious and relies on Cantor's diagonal argument, which is a bit similar to the Russel's paradox. Expressed in a very informal way, this gives the barber paradox:

.. topic:: The barber paradox.

    The barber is the "one who shaves all those, and those only, who do not shave themselves". The question is, does the barber shave himself?

This question is unsatisfiable and the proposition of the existence of such a barber must be false. With this idea kept in mind, let us prove that the set of real number between 0 and 1 is not countable.

Let us assume by contradiction that this set :math:`[0, 1]` is in fact countable. Therefore, it exists a bijection and its inverse

.. math:: f: [0, 1] \to \mathbb{N} : n \mapsto f(n)

.. math:: f^{-1}: \mathbb{N} \to [0, 1] : x \mapsto f^{-1}(x)

Writing a similar table as before, we would have something like the following

+-------------------+----------------------+
| :math:`\mathbb{N}`| :math:`[0,1]`        |
+===================+======================+
| 0                 |  0.\ **9**\ 184919...| 
+-------------------+----------------------+
| 1                 |  0.5\ **8**\ 03284...| 
+-------------------+----------------------+
| 2                 |  0.82\ **2**\ 7340...| 
+-------------------+----------------------+
| 3                 |  0.622\ **7**\ 448...| 
+-------------------+----------------------+
| 4                 |  0.7210\ **3**\ 96...| 
+-------------------+----------------------+

The idea now is to consider the real number :math:`c \in [0, 1]` which consists of the elements "on the diagonal", the elements in bold. From this number, 0.98273..., we construct another number :math:`\overline{c} \in [0, 1]` by incrementing each digit: :math:`\overline{c}=0.09384`. This number cannot be in any line :math:`n` of the array since by construction, the :math:`n-`\ th digit will be different. Remembering the barber paradox, the question here is not "Who shaves the barber?" but "Which number counts :math:`\overline{c}`?". As we found a contradiction, our hypothesis on the countability of :math:`[0, 1]` must be false, and therefore this set is uncountable.

(Countable) Infinity of words
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
With this little background of arithmetic, we can prove our first little lemme:

**Lemma 1 (L1): The number of words that can be build with a finite alphabet is countably infinite**

This Lemma can be proven by simply exhibiting a bijection. Here we simply choose the base-26: "0" is encoded with "z", "1" is encoded with "a" and "2" is encoded with "b". If we want to encode 1236, we note that

.. math:: 1236 = 26^2 \cdot 6 + 26^1 \cdot 21 + 26^0 \cdot 14

since the 6th letter is "F", the 21st letter is "U" and the 14th is "N"; this gives FUN [#bijection]_.

(Uncountable) Infinity of concepts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. rubric:: Footnotes

.. [#f1] Arendt, Hannah (2006) [1961, New York: Viking]. *Between Past and Future*. Penguin Publishing Group. ISBN 978-1-101-66265-6. 

.. [#f2] Internet of Philosophy, Socrates. Consulted [ONLINE] on 2020-08-09, https://iep.utm.edu/socrates. 

.. [#Kant_critique] Kant, Immanuel, et al. The Critique of Pure Reason. Cambridge University Press, 2009.

.. [#bijection] Notice that here, the proposed mapping is not really a bijection since the number 003 is considered as 3 and we will *not* have the word "zzc". In fact, we proved that the number of (finite) words is greater (or equal) than the number of natural. It suffices to reverse the relation to proof that the cardinality of the natural number is greater than the finite words. Hence, the cardinality of both sets is equal, and the proof is complete.
