# MLOPTIM.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1Jvzb9mqKiy4zKsvUx8b_sAV7xLURgm1k) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
Machine Learning and Optimisation
                 Linear Regression
               Logistic Regression




 Optimisation for Machine Learning
          with Focus on Logistic Regression


                           Maria Malek


                        14 octobre 2024




                     Maria Malek     Le perceptron   1/19
~~~

## Page 2

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression




1   Machine Learning and Optimisation
     Stochastic gradient descent


2   Linear Regression


3   Logistic Regression




                                Maria Malek     Le perceptron   2/19
~~~

## Page 3

~~~text
             Machine Learning and Optimisation
                              Linear Regression   Stochastic gradient descent
                            Logistic Regression


Machine Learning and Optimisation
       Many standard machine learning methods can be formulated
       as a convex optimisation problem.
       finding a minimiser of a convex function f that depends on a
       variable vector w (called weights) which has d + 1 entries.

  Objective function
  f (w ) = λR(w ) + n1 ni=1 L(w ; xi , yi ), where xi ∈ Rd+1 and yi is
                         P
  the label, n is the number of training examples
  w = (w0 , w1 , ..wd ), xi = (+1, xi1 , ..xid )
       L(w ; xi , yi ) is the loss function, R(w ) is the regulator
       λ defines the compromise between the two goals of
       minimising the loss (training error) and minimising model
       complexity (to avoid overfitting).

                                  Maria Malek     Le perceptron        3/19
~~~

## Page 4

~~~text
            Machine Learning and Optimisation
                             Linear Regression   Stochastic gradient descent
                           Logistic Regression


Convex Optimisation Problem


  Convex Optimisation Problem
      minimizex f(x)
      SubjectTo
           gi (x) ≤ 0, i = {1..k}
           hj (x) = 0 j = {1..l}
  WITH
      f is a convex function
      g is a convex set
      h is affine




                                 Maria Malek     Le perceptron        4/19
~~~

## Page 5

~~~text
           Machine Learning and Optimisation
                            Linear Regression   Stochastic gradient descent
                          Logistic Regression


Gradient descent - illustration




      E (x) = (x − 1)(x − 2)(x − 3)(x − 5),
      E ′ (x) = 4x3 − 33x2 + 82x − 61
      xi+1 = xi − γE ′ (xi )
          If x0 = 5 and γ = 0.001, DG finds x = 4.32 and E = −6.91 in
          447 iterations.
          If x0 = 5 and γ = 0.01, DG finds x = 4.32 and E = −6.91 in
          39 iterations.
                                Maria Malek     Le perceptron        5/19
~~~

## Page 6

~~~text
           Machine Learning and Optimisation
                            Linear Regression   Stochastic gradient descent
                          Logistic Regression


Gradient descent and optimisation


      Solve optimisation problems of the form

                                     minw ∈Rd+1 (f (w ))

      well-suited for large-scale and distributed computation.
      find a local minimum of a function by iteratively taking steps
      in the direction of steepest descent :
          the negative of the derivative (called the gradient) of the
          function at the current point
      Stochastic gradient descent (SGD)




                                Maria Malek     Le perceptron        6/19
~~~

## Page 7

~~~text
             Machine Learning and Optimisation
                              Linear Regression   Stochastic gradient descent
                            Logistic Regression


Stochastic Gradient descent

  SGD
        Optimisation formulations commonly usedP in supervised
        machine learning : f (w ) = λR(w ) + n1 ni=1 L(w ; xi , yi )
        Repeat until an approximate minimum is obtained :
             Randomly shuffle examples in the training set.
             For i=1,2,...,n do :
                   fw′ ,i = λRw′ ,i + L′w ,i where :
                   L′w ,i subgradient of the part of the loss function determined by
                   the ith datapoint : L′w ,i ∈ ∂w ∂
                                                     L(w ; xi , yi )
                      ′
                   Rw ,i is a subgradient of the regulariser determined by the ith
                   datapoint : Rw′ ,i ∈ ∂w   ∂
                                               R(w )
                   Walking in the direction of the negative stochastic
                   subgradient : w t+1 = w t − γfw′ ,i , γ is the step size.



                                  Maria Malek     Le perceptron        7/19
~~~

## Page 8

~~~text
             Machine Learning and Optimisation
                              Linear Regression   Stochastic gradient descent
                            Logistic Regression


Loss Functions
  Objective function
  f (w ) = λR(w ) + n1 ni=1 L(w ; xi , yi ), where xi ∈ Rd+1 and yi is
                         P
  the label, n is the number of training examples
  w = (w0 , w1 , ..wd ), xi = (+1, xi1 , ..xid )

  Squared Loss for linear regression
   Function : L(w ; xi , yi ) = 21 (w T xi − yi )2 , y ∈ R
    Gradient : L′w = (w T x − y )x

  Logistic loss for logistic regression
   Function : L(w ; xi , yi ) = ln(1 + exp(−yi w T xi )) , y ∈ {−1, 1}
    Gradient : L′w = −y (1 − (1+exp(−yw
                                   1
                                        T x) )x



                                  Maria Malek     Le perceptron        8/19
~~~

## Page 9

~~~text
              Machine Learning and Optimisation
                               Linear Regression     Stochastic gradient descent
                             Logistic Regression


Regularisers
  Objective function
  f (w ) = λR(w ) + n1 ni=1 L(w ; xi , yi ), where xi ∈ Rd+1 and yi is
                         P
  the label, n is the number of training examples
  w = (w0 , w1 , ..wd ), xi = (+1, xi1 , ..xid )

  L2- ridge
                                                   Pj=d
   Function : R(w ) = 12 ∥w ∥22 =                   j=0 wj
                                                          2

    Gradient : Rw′ = w

  L1– lasso
                                              Pj=d
   Function : R(w ) = ∥w ∥1 =                      j=0 |wj |
    Gradient : Rw′ = sign(w )

                                   Maria Malek       Le perceptron        9/19
~~~

## Page 10

~~~text
            Machine Learning and Optimisation
                             Linear Regression
                           Logistic Regression


Linear Regression- illustration




      Average loss or training error : n1 ni=1 (w T xi − yi )2
                                           P

      w = (w0 , w1 , ..wd ), x = (+1, x1 , ..xd )
      w0 = b0 , w1 = b1
                                 Maria Malek     Le perceptron   10/19
~~~

## Page 11

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Linear Regression


      Linear least squares is the most common formulation for
      regression problems.
      Loss function is given by the squared loss :
      L(w ; x, y ) = 21 (w T x − y )2
      Various related regression methods : linear least squares uses
      no regularisation ; ridge regression uses L2 regularisation ; and
      Lasso uses L1 regularisation.
      The average loss or training error : n1 ni=1 (w T xi − yi )2 ,
                                                 P
      w = (w0 , w1 , ..wd ), x = (+1, x1 , ..xd )




                                Maria Malek     Le perceptron   11/19
~~~

## Page 12

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression - illustration




      Probability of happiness (H) knowing (Income) , find
           ez        1
      p = 1+e z = 1+e −z with z = w0 + w1 x1 , where x1 is income

      if p >= 0.5 then the happiness is positive, otherwise it’s
      negative

                                Maria Malek     Le perceptron   12/19
~~~

## Page 13

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression : loss function wt bipolar
representation
      In general, a binary logistic regression model make predictions
      as follow :
           Given a new data point, denoted by x (having d features) :
           the model makes predictions by applying : f (z) = 1+e1 −z with
           z = wT x
           if f (w T x) > 0.5 where w = (w0 , w1 , ..wd ), x = (+1, x1 , ..xd )
           then the outcome is positive, otherwise it’s negative.
                                          ez
           notice that : p(Y = 1 | Z ) = 1+e z ,
                                                       1
           p(Y = −1 | Z ) = 1 − p(Y = 1 | Z ) = 1+e      z = f (−z)

      It is easier to optimise the log-likelihood of : p(y | z) = f (yz),
      y ∈ {−1, 1}
      Maximising ln(f (yz)) ⇒ minimise the loss function
      −ln(f (yz))
      Loss function is given by the logistic loss :
      L(w ; x, y ) = ln(1 + exp(−yw T x)), y ∈ {−1, 1}
                                Maria Malek     Le perceptron   13/19
~~~

## Page 14

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression : loss function wt binary representation
      In general, a binary logistic regression model make predictions
      as follow :
           Given a new data point, denoted by x (having d features) :
           the model makes predictions by applying : f (z) = 1+e1 −z with
           z = wT x
           if f (w T x) > 0.5 where w = (w0 , w1 , ..wd ), x = (+1, x1 , ..xd )
           then the outcome is positive, otherwise it’s negative.
      It is easier to optimise the log-likelihood of :
      p(y | z) = f (z)y ∗ (1 − f (z))(1−y ) , y ∈ {0, 1}
      Maximising ln(f (z)y ∗ (1 − f (z)(1−y ) )) ⇒ minimise the loss
      function −ln(f (z)y ∗ (1 − f (z)(1−y ) ))
      Loss function is given by the logistic loss (Binary
      Cross-Entropy) :
                                 1                            1
      L(w ; x, y ) = y ∗ln( 1+exp(−w T x) )+(1−y )∗ln(1− 1+exp(−w T x) ),

      y ∈ {0, 1}
                                Maria Malek     Le perceptron   14/19
~~~

## Page 15

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression : Odds, Logit and Logistic Functions
      Consider a two-outcome probability space, where p(O1) = p
      and p(O2) = 1 − p = q :
      for exemple O1 is happiness and O2 is no happiness
      standard probability p ∈ [0, 1]
              odds qp ∈ [0, ∞[
      log odds (logit) ln( qp ) ∈] − ∞, ∞[
                                          p                p
      Notice that : p = 1+e1 −z so e z = 1−p and z = ln( 1−p ) with
            T
      z = w x, w = (w0 , w1 , ..wd ), x = (+1, x1 , ..xd )

              p
      odds : 1−p
                                p
      Logit Function : z = ln( 1−p ) = wT x
                               e        1   z
      Logistic Function : p = 1+e z = 1+e −z



                                Maria Malek     Le perceptron   15/19
~~~

## Page 16

~~~text
            Machine Learning and Optimisation
                             Linear Regression
                           Logistic Regression


Logistic Regression : interpretation


  The Model
      Model consists of finding a vector w in d-dimensional feature
      space
      For a point x in feature space, project it onto w to convert it
      into a real number z in the range ] − ∞, ∞[
      z = w0 + w T x = w0 + w1 x1 + ... + wd xd
      Map z to the range 0 to 1 using the logistic function
           ez       1
      p = 1+e z = 1+e −z

      So, logistic regression maps a point x in d-dimensional feature
      space to a value in the range 0 to 1



                                 Maria Malek     Le perceptron   16/19
~~~

## Page 17

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression-multimodal-1


      The algorithm outputs a binary logistic regression model
      can be generalized into multinomial logistic regression to train
      and predict multiclass classification problems.
      First strategy     For K possible outcomes, one of the outcomes
                               can be chosen as a ”pivot”, and the other K-1
                               outcomes can be separately regressed against
                               the pivot outcome.
                               Given a new data points, K-1 models will be
                               run, and the class with largest probability will
                               be chosen as the predicted class.




                                Maria Malek     Le perceptron   17/19
~~~

## Page 18

~~~text
           Machine Learning and Optimisation
                            Linear Regression
                          Logistic Regression


Logistic Regression-multimodal-2


      The algorithm outputs a binary logistic regression model
      can be generalized into multinomial logistic regression to train
      and predict multiclass classification problems.
      Second strategy       For each outcome, other K-1 outcomes are
                               regressed against this outcome.
                               Given a new data points, K models will be run,
                               and the class with largest probability will be
                               chosen as the predicted class
                               Loss function is given by the logistic loss
                               (Categorial Cross-Entropy) :
                                             PK                  1
                               L(w ; x, y ) = k=1 yk ∗ ln( 1+exp(−w Tx ))
                                                                      k




                                Maria Malek     Le perceptron   18/19
~~~

## Page 19

~~~text
          Machine Learning and Optimisation
                           Linear Regression
                         Logistic Regression


Logistic Regression - Example




                               Maria Malek     Le perceptron   19/19
~~~
