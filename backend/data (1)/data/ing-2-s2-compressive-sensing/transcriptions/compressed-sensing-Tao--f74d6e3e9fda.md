# compressed-sensing-Tao.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1uXTwZchRWpYTnlsCYrTMEqVtcTvuAmnt) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
          Introduction
   Compressed sensing
              Variants
          Applications




  Compressed sensing
Or: the equation Ax = b, revisited


              Terence Tao

   University of California, Los Angeles


      Mahler Lecture Series




           Terence Tao   Compressed sensing
~~~

## Page 2

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications


Acquiring signals

     Many types of real-world signals (e.g. sound, images,
     video)
          can  be viewed as an n-dimensional vector
            x1
     x =  ...  ∈ Rn of real numbers, where n is large (e.g.
          

           xn
     n ∼ 106 ).
     To acquire this signal, we consider a linear measurement
     model, in which we measure an m-dimensional vector
     b = Ax ∈ Rm for some m × n measurement matrix A (thus
     we measure the inner products of x with the rows of A).
     For instance, if we are measuring a time series in the
     frequency domain, A would be some sort of Fourier matrix.

                           Terence Tao   Compressed sensing
~~~

## Page 3

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications




This leads to the following classical question in linear algebra:
    Question: How many measurements m do we need to
    make in order to recover the original signal x exactly from
    b? What about approximately?
    In other words: when can we solve the equation Ax = b?




                           Terence Tao   Compressed sensing
~~~

## Page 4

~~~text
                           Introduction
                    Compressed sensing
                               Variants
                           Applications


The classical answer
  The classical theory of linear algebra, which we learn as
  undergraduates, is as follows:
      If there are at least as many measurements as unknowns
      (m ≥ n), and A has full rank, then the problem is
      determined or overdetermined, and one can easily solve
      Ax = b uniquely (e.g. by gaussian elimination).
      If there are fewer measurements than unknowns (m < n),
      then the problem is underdetermined even when A has full
      rank. Knowledge of Ax = b restricts x to an (affine)
      subspace of Rn , but does not determine x completely.
      However, if one has reason to believe that x is “small”, one
      can use the least squares solution
      x # = argminx:Ax=b kxk`2 = A∗ (AA∗ )−1 b as the “best
      guess” for x.
                            Terence Tao   Compressed sensing
~~~

## Page 5

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




                                             #
                                         x




                                                      Ax=b




A low-dimensional example of a least-squares guess.



                         Terence Tao   Compressed sensing
~~~

## Page 6

~~~text
                       Introduction
                Compressed sensing
                           Variants
                       Applications




In many situations the least squares solution is not
satisfactory.
For instance, consider the problem of reconstructing a
one-dimensional discrete signal f : {1, . . . , n} → C from a
partial collection f̂ (ξ1 ), . . . , f̂ (ξm ) of Fourier coefficients
                                       n
                             1X
                   f̂ (ξ) :=    f (x)e−2πixξ/n .
                             n
                                      x=1




                        Terence Tao        Compressed sensing
~~~

## Page 7

~~~text
                           Introduction
                    Compressed sensing
                               Variants
                           Applications




The least squares solution f # to this problem is easily seen to
be the partial Fourier series
                                m
                                X
                      f # :=           f̂ (ξj )e−2πiξj x/n
                                 j=1

which, when m is small, is often very different from the original
signal f , especially if f is “spiky” (consider for instance a delta
function signal).




                            Terence Tao     Compressed sensing
~~~

## Page 8

~~~text
                         Introduction
                  Compressed sensing
                             Variants
                         Applications




The Logan-Shepp phantom and its least squares reconstruction
after Fourier-sampling along 22 radial lines (here m/n ≈ 0.05).
This type of measurement is a toy model of that used in MRI.



                          Terence Tao   Compressed sensing
~~~

## Page 9

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications


Sparse recovery



     It is thus of interest to obtain a good estimator for
     underdetermined problems such as Ax = b in the case in
     which x is expected to be “spiky” - that is, concentrated in
     only a few of its coordinates.
     A model case occurs when x is known to be S-sparse for
     some 1 ≤ S ≤ n, which means that at most S of the
     coefficients of x can be non-zero.




                           Terence Tao   Compressed sensing
~~~

## Page 10

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications


Why sparsity?

     Sparsity is a simple but effective model for many real-life
     signals. For instance, an image may be many megapixels
     in size, but when viewed in the right basis (e.g. a wavelet
     basis), many of the coefficients may be negligible, and so
     the image may be compressible into a file of much smaller
     size without seriously affecting the image quality. (This is
     the basis behind algorithms such as the JPEG2000
     protocol.) In other words, many images are effectively
     sparse in the wavelet basis.
     More complicated models than sparse signals can also be
     studied, but for simplicity we will restrict attention to the
     sparse case here.

                           Terence Tao   Compressed sensing
~~~

## Page 11

~~~text
                            Introduction
                     Compressed sensing
                                Variants
                            Applications


Sparsity helps!

      Intuitively, if a signal x ∈ Rn is S-sparse, then it should only
      have S degrees of freedom rather than n. In principle, one
      should now only need S measurements or so to
      reconstruct x, rather than n. This is the underlying
      philosophy of compressive sensing: one only needs a
      number of measurements proportional to the compressed
      size of the signal, rather than the uncompressed size.
      An analogy would be with the classic twelve coins puzzle:
      given twelve coins, one of them counterfeit (and thus
      heavier or lighter than the others), one can determine the
      counterfeit coin in just three weighings, by weighing the
      coins in suitably chosen batches. The key point is that the
      counterfeit data is sparse.

                             Terence Tao   Compressed sensing
~~~

## Page 12

~~~text
                         Introduction
                  Compressed sensing
                             Variants
                         Applications




Compressed sensing is advantageous whenever
    signals are sparse in a known basis;
    measurements (or computation at the sensor end) are
    expensive; but
    computations at the receiver end are cheap.
Such situations can arise in
    Imaging (e.g. the “single-pixel camera”)
    Sensor networks
    MRI
    Astronomy
    ...


                          Terence Tao   Compressed sensing
~~~

## Page 13

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications


But can compressed sensing work?



     Proposition: Suppose that any 2S columns of the m × n
     matrix A are linearly independent. (This is a reasonable
     assumption once m ≥ 2S.) Then, any S-sparse signal
     x ∈ Rn can be reconstructed uniquely from Ax.
     Proof: Suppose not; then there are two S-sparse signals
     x, x 0 ∈ Rn with Ax = Ax 0 , which implies A(x − x 0 ) = 0. But
     x − x 0 is 2S-sparse, so there is a linear dependence
     between 2S columns of A, contradiction. 




                           Terence Tao   Compressed sensing
~~~

## Page 14

~~~text
                     Introduction
              Compressed sensing
                         Variants
                     Applications


In fact, the above proof also shows how to reconstruct an
S-sparse signal x ∈ Rn from the measurements b = Ax: x
is the unique sparsest solution to Ax = b. In other words,
                    x = argminx:Ax=b kxk`0
where
                    n
                    X
         kxk`0 :=          |xi |0 = #{1 ≤ i ≤ n : xi 6= 0}
                     i=1

is the sparsity of x.
Unfortunately, in contrast to the `2 minimisation problem
(least-squares), `0 minimisation is computationally
intractable (in fact, it is an NP-hard problem in general). In
part, this is because `0 minimisation is not a convex
optimisation problem.
                      Terence Tao   Compressed sensing
~~~

## Page 15

~~~text
                     Introduction
              Compressed sensing
                         Variants
                     Applications




To summarise so far: when solving an underdetermined
problem Ax = b, `2 minimisation is easy to compute, but
often wrong.
When x is sparse, `0 minimisation is often correct, but very
difficult to compute.
Is there a way to split the difference?




                      Terence Tao   Compressed sensing
~~~

## Page 16

~~~text
                          Introduction
                   Compressed sensing
                              Variants
                          Applications


Basis pursuit


     A simple, yet surprisingly effective, way to do so is `1
     minimisation or basis pursuit; thus, our guess x ] for the
     problem Ax = b is given by the formula

                        x ] = argminx:Ax=b kxk`1 .

     This is a convex optimisation problem and can be solved
     fairly quickly by linear programming methods (several
     specialised software packages are now also available).
     And... it works!



                           Terence Tao   Compressed sensing
~~~

## Page 17

~~~text
                         Introduction
                  Compressed sensing
                             Variants
                         Applications




                                        x




                                                        Ax=b




In this example, the signal x is reconstructed exactly from
b = Ax by `1 minimisation.




                          Terence Tao       Compressed sensing
~~~

## Page 18

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




Exact reconstruction of the Logan-Shepp phantom from partial
Fourier data by `1 minimisation (or more precisely, total
variation minimisation, i.e. the `1 norm of the gradient).



                         Terence Tao   Compressed sensing
~~~

## Page 19

~~~text
                     Introduction
              Compressed sensing
                         Variants
                     Applications




Basis pursuit was introduced empirically in the sciences
(e.g. in seismology by Claerbout-Muir and others) in the
1970s, and then studied mathematically in the 1990s by by
Chen, Donoho, Huo, Logan, Saunders, and others.
Near-optimal performance guarantees emerged in the
2000s by Candés-Romberg-Tao, Donoho, and others.
There are also several other compressed sensing
algorithms known (e.g. matching pursuit and its
refinements), but we will focus on basis pursuit here as it is
relatively simple to state.




                      Terence Tao   Compressed sensing
~~~

## Page 20

~~~text
                            Introduction
                     Compressed sensing
                                Variants
                            Applications


Theoretical results

      There are now several theoretical results ensuring that
      basis pursuit works whenever the measurement matrix A is
      sufficiently “incoherent”, which roughly means that its
      matrix entries are uniform in magnitude. (It’s somewhat
      analogous to how the secret to solving the twelve coins
      problem is to weigh several of the coins at once.) Here is
      one typical result:
      Theorem: (Candés-Romberg-T. 2004). Let
      ξ1 , . . . , ξm ∈ {1, . . . , n} be chosen randomly. Then with high
      probability, every S-sparse signal f : {1, . . . , n} → C can be
      recovered from f̂ (ξ1 ), . . . , f̂ (ξm ), so long as m > CS log n
      for some absolute constant C.

                             Terence Tao   Compressed sensing
~~~

## Page 21

~~~text
                      Introduction
               Compressed sensing
                          Variants
                      Applications




Numerical experiments suggest that in practice, most
S-sparse signals are in fact recovered exactly once
m ≥ 4S or so.
It turns out that basis pursuit is effective not only for Fourier
measurements, but for a much wider class of
measurement matrices. The necessary condition that
every 2S columns of A have to be linearly independent,
has to be strengthened somewhat (for instance, to the
assertion that every 4S columns of A are approximately
orthonormal). The precise condition used in the literature
is called the Restricted Isometry Property (RIP), and is
obeyed by many types of matrices (e.g. gaussian random
matrices obey the RIP with high probability).


                       Terence Tao   Compressed sensing
~~~

## Page 22

~~~text
                            Introduction
                     Compressed sensing
                                Variants
                            Applications


Variants and extensions
  There are many variants and extensions of compressed
  sensing in the literature (200+ papers in the last 3 years!). Here
  is a quick sample:
      Compressed sensing algorithms such as basis pursuit can
      not only recover sparse data x exactly from b = Ax, but
      can also recover compressible data (data which is
      approximately sparse) approximately, by a slight
      modification of the algorithm.
      In a similar spirit, these algorithms are also robust with
      regards to noise: if one only has some approximate
      measurements b = Ax + z of the signal x, where z is a
      noise vector (e.g. gaussian white noise), then basis pursuit
      will still recover a good approximation x ] to x.

                             Terence Tao   Compressed sensing
~~~

## Page 23

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




                                   x
                               #
                              x




                                                || Ax − b || < e




Reconstructing a sparse signal x approximately from noisy data
b = Ax + z, assuming that z has norm less than some error
tolerance e.



                         Terence Tao   Compressed sensing
~~~

## Page 24

~~~text
                     Introduction
              Compressed sensing
                         Variants
                     Applications




There is a “dual” to compressed sensing, namely linear
coding in which a signal x ∈ Rn is expanded into a larger
signal Ax ∈ Rm (where now m > n instead of m < n) to be
transmitted over a noisy network. Even if parts of the
transmitted signal are corrupted, so that the data received
is of the form b = Ax + e for some sparse e (representing
packet loss or corruption), one can recover x exactly in
many cases. (The trick is to view e, rather than x, as the
signal, in which case one can convert things back to a
compressed sensing problem.)




                      Terence Tao   Compressed sensing
~~~

## Page 25

~~~text
                    Introduction
             Compressed sensing
                        Variants
                    Applications




There are also matrix versions of compressed sensing:
instead of trying to reconstruct a sparse vector x from
some measurements Ax, one instead tries to reconstruct a
low-rank matrix M from some coefficients of that matrix.
There is an analogue of basis pursuit (using the nuclear
norm kMk1 rather than the `1 norm) which is effective in
many cases. This type of problem is relevant to real-life
matrix completion problems (e.g. the Netflix prize).




                     Terence Tao   Compressed sensing
~~~

## Page 26

~~~text
                         Introduction
                  Compressed sensing
                             Variants
                         Applications


Practical applications of compressed sensing



     Compressed sensing is a fairly new paradigm, but is
     already being used in practical settings, for instance to
     speed up MRI scans by requiring fewer measurements to
     achieve a given amount of resolution.
     One of the first prototype demonstrations of compressed
     sensing is the single pixel camera, developed by Rice
     University.




                          Terence Tao   Compressed sensing
~~~

## Page 27

~~~text
                         Introduction
                  Compressed sensing
                             Variants
                         Applications




A schematic of the Rice single pixel camera
(http://dsp.rice.edu/cscamera)


                          Terence Tao   Compressed sensing
~~~

## Page 28

~~~text
                    Introduction
             Compressed sensing
                        Variants
                    Applications




Physical implementation
(http://dsp.rice.edu/cscamera)

                     Terence Tao   Compressed sensing
~~~

## Page 29

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




Test image (16384 pixels) and CS reconstruction using 1600
and 3300 measurements
(http://dsp.rice.edu/cscamera)



                         Terence Tao   Compressed sensing
~~~

## Page 30

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




Test image (65536 pixels) and CS reconstruction using 6600
measurements (http://dsp.rice.edu/cscamera)

                         Terence Tao   Compressed sensing
~~~

## Page 31

~~~text
                        Introduction
                 Compressed sensing
                            Variants
                        Applications




MRI image of a mouse heart, and CS reconstruction using 20%
of available measurements (Blumensath-Davies)

                         Terence Tao   Compressed sensing
~~~
