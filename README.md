# desubifier
---
desubifier is a simple program to decrypt messages that are encrypted using a substitution cipher. It is not perfect but nearly always comes up with an answer that is correct or very close to correct.

To use the program you must have Python 2.7 or greater installed, simply run the following command:

```
$ python desubifier.py
```

You will then be prompted for some encrypted text. This is an example of the output:

```
Enter text to be deciphered: 
h khrawkhrgtghc gn h ewsgtw yoq rpqcgcd toyyww gcro rawoqwkn

e menolmentater th e plital uds nfsrtry aduull trnd noldslmh -> -271.697867241
a casincasowoar of a undown the sperory whttnn orsh sinhencf -> -259.683624641
a masoymasilian if a bydily ter surning lettyy inse soyerymf -> -254.879492284
a mathematician is a device for turning coffee into theorems -> -209.259607393
```

Typically, the algorithm will run multiple times, only displaying its new highest result. If the higher result is not found after 100 attempts the program will ask if you want to try again.

### Resources
---

I used a slighty altered version of [this](http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/) to determine fitness.

I used [this](https://norvig.com/big.txt) to gather data about quadgram frequency.

 
