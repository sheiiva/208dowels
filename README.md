208dowels
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
A power hammer mass produces dowels. Sometimes, some pieces are defective, and the whole process requires quality control: **100 samples of 100 pieces** are **randomly** taken, and defective pieces are numbered. We get what we call an observed serial. Then, a statistical fit is done using the binomial distribution, and validated using the x² test.


Let’s note ***x* the number of defective pieces**, ***Ox* the size of the observed sample**, and ***Tx* the theoretical size**. To ensure the consistency of the fit, statistical classes which have less than 10 elements are merged until there are only classes with 10 or more elements. Smallest classes are aggregated first. 


Finally, with the number of constraints for the fit being 2, the degrees of freedom parameter *ν* is equal to the number of classes minus 2.

Your program will take 9 integers as inputs, representing respectively *O0*, *O1*, ..., *O8+* and will output:
* An array showing observed and theoretical sizes for each statistical class (with totals)
* The chosen probability distribution for the fit
* The value of *x²*
* The value of *ν*
* The value range in which the probability falls if the fit is valid


## USAGE:

```
>> ./208dowels -h
USAGE
    ./208dowels O0 O1 O2 O3 O4 O5 O6 O7 O8

DESCRIPTIONO
    i   size of the observed class
```



Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva) and [**PATRICIA MONFA-MATAS**](https://github.com/patumm)
