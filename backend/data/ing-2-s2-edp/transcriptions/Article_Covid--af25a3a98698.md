# Article_Covid.pdf

[Ouvrir l’original](https://drive.google.com/open?id=1TXEPkKkmqGSXfcppcNNCeDyKX7TqtPXl) · Nombre de pages contrôlé et caractères alphanumériques comparés entre deux lectures du PDF. Les positions des symboles et les éléments graphiques se vérifient sur l’original.

## Page 1

~~~text
                                            DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                  1




                                                Mathematical Modeling of Epidemic Diseases; A
                                                  Case Study of the COVID-19 Coronavirus
                                                                                                                Reza Sameni*
                                                                                                              Grenoble, France
                                                                                                            Revision: 19 May 2020



                                               Abstract—The outbreak of the Coronavirus COVID-19 has                          shown by simulation, how social measures such as distancing,
                                            taken the lives of several thousands worldwide and locked-                        regional lockdowns and public health vigilance, can influence
                                            out many countries and regions, with yet unpredictable global                     the model parameters, which in turns change the mortality
arXiv:2003.11371v3 [q-bio.PE] 19 May 2020




                                            consequences. In this research we study the epidemic patterns of
                                            this virus, from a mathematical modeling perspective. The study                   rates and active contaminated cases over time.
                                            is based on an extensions of the well-known susceptible-infected-                    It should be highlighted that mathematical models applied
                                            recovered (SIR) family of compartmental models. It is shown                       to real-world systems (social, biological, economical, etc.) are
                                            how social measures such as distancing, regional lockdowns,                       only valid under their assumptions and hypothesis. Therefore,
                                            quarantine and global public health vigilance, influence the model
                                                                                                                              this research— and similar ones— that address epidemic pat-
                                            parameters, which can eventually change the mortality rates and
                                            active contaminated cases over time, in the real world. As with all               terns, do not convey direct clinical information and dangers for
                                            mathematical models, the predictive ability of the model is limited               the public, but should rather be used by healthcare strategists
                                            by the accuracy of the available data and to the so-called level of               for better planning and decision making. Hence, the study of
                                            abstraction used for modeling the problem. In order to provide                    this work is only recommended for researchers familiar with
                                            the broader audience of researchers a better understanding of
                                                                                                                              the strength points and limitations of mathematical modeling
                                            spreading patterns of epidemic diseases, a short introduction on
                                                                                                     .
                                            biological systems modeling is also presented and the Matlab                      of biological systems. The Matlab codes required for repro-
                                                                                                                              ducing the results of this research are also online available in
                                            source codes for the simulations are provided online.
                                                                                                                              the Git repository of the project [7].
                                                                                                                                 In Section II, a brief introduction to mathematical modeling
                                                                      I. I NTRODUCTION                                        of biological systems is presented, to highlight the scope of
                                               Since the outbreak of the Coronavirus COVID-19 in January                      the present study and to open perspectives for the interested
                                            2020, the virus has affected most countries and taken the lives                   researchers, who may be less familiar with the context. The
                                            of several thousands of people worldwide. By March 2020,                          proposed model for the outspread of the Coronavirus is
                                            the World Health Organization (WHO) declared the situation a                      presented in Section III. The article is concluded with some
                                            pandemic, the first of its kind in our generation. To date, many                  general remarks and future perspectives.
                                            countries and regions have been locked-down and applied
                                            strict social distancing measures to stop the virus propagation.                      II. A N INTRODUCTION MATHEMATICAL EPIDEMIOLOGY
                                            From a strategic and healthcare management perspective, the                                    AND COMPARTMENTAL MODELING
                                            propagation pattern of the disease and the prediction of its
                                            spread over time is of great importance, to save lives and to                     A. Mathematical modeling
                                            minimize the social and economic consequences of the disease.                        A model is an entity that resembles a system or object in
                                            Within the scientific community, the problem of interest has                      certain aspects, but is easier to work with as compared to the
                                            been studied in various communities including mathematical                        original system. Models are used for the 1) identification and
                                            epidemiology [1], [2], biological systems modeling [3], [4],                      better understanding of systems, 2) simulation of a system’s
                                            signal processing [5] and control engineering [6].                                behavior, 3) prediction of its future behavior, and ultimately
                                               In this study, epidemic outbreaks are studied from                             4) system control. Apparently, from item 1 to 4, the problem
                                            an interdisciplinary perspective, by using an extension of                        becomes more difficult and although the ultimate objective is
                                            the susceptible-exposed-infected-recovered (SEIR) model [2],                      to harness or control a system, this objective is not necessarily
                                            which is a mathematical compartmental model based on the                          achievable. While modeling is the first and most important step
                                            average behavior of a population under study. The objective                       in this path, it is highly challenging and nontrivial. The various
                                            is to provide researchers a better understanding of the signif-                   issues that one faces in this regard, include:
                                            icance of mathematical modeling for epidemic diseases. It is
                                                                                                                              • Models are not unique and different models can co-exist for
                                              * R. Sameni is Associate Professor of Biomedical Engineering at School of         a single system.
                                            Electrical & Computer Engineering, Shiraz University, Shiraz, Iran, currently     • A model is only a slice of reality and all models have a
                                            on sabbatical leave as a visiting researcher at GIPSA-lab, Université Grenoble     scope, outside of which, they are invalid.
                                            Alpes, CNRS, Grenoble INP, 38000 Grenoble, France and a member of the
                                            SEEPIA (Simulation & Estimation of Epidemics with Algorithms) project             • Modeling can be done in different levels of abstraction,
                                            working group (e-mail: reza.sameni@gmail.com).                                      which corresponds to the level of simplification and the
~~~

## Page 2

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                   2



  specific aspects of the system that are considered by the             exponentially spreads among the population, the infected
  model.                                                                population tend to encounter each other and repeated healthy
                                                                        ones (the healthy individuals already contacted by another
Example 1. The response of global stock markets with numer-
                                                                        infected person). Hence, the stochastic model of infection
ous economic, political, industrial, social and psychological
                                                                        propagation, somehow saturates1 . The probabilistic models
factors, to a high impact news can in cases be modeled with
                                                                        used for modeling such epidemic spread are commonly based
a second-order differential equation, with a step-like over-
                                                                        on the branching process and a Poisson distributions for the
damped behavior that reaches its steady state after a while.
                                                                        probability of contact between infectious and healthy subjects.
Or in medicine, the response of the human body— with more
                                                                        The stochastic perspective to epidemic modeling has been
that thirty-seven trillion cells— to medication can in many
                                                                        extensively studied in the literature [2], [11]–[13]. Herein, we
cases be “resonably” modeled with a first order differential
                                                                        adopt a more heuristic approach for model formation, which
equation.
                                                                        is less rigorous, but is equally accurate in large populations
   While various types of models are used for biological sys-           (refer to the above references for the justification).
tems, we are commonly interested in mathematical models [8],               Suppose that x(t) denotes the number of infected indi-
as they permit the prediction and possible control of biological        viduals of a population at time t. Next, assuming that the
systems. In choosing among different available models, the              chance of infection increases with the number of infected
widely accepted principle is the model parsimony, which sim-            individuals, we assume that the variations in the population
ply means that “a model should be as simple as possible and             of the number of infected between time t and t + ∆ (over
as complex as necessary!”. The model parsimony, is also an              relatively small intervals ∆) is proportional to the number of
important factor for estimating the unknown model parameters            infected individuals, i.e.,
using real data. A more accurate model with fewer number                            dx(t)     x(t + ∆) − x(t)
of parameters is evidently preferred over a less accurate and                              ≈                   = φ(t)x(t)          (1)
                                                                                      dt             ∆
more complex model. But how should one select between
                                                                        Let us name φ(t) the reproduction function, which models
a more accurate complex model and a less accurate simpler
                                                                        how the infected population evolves over time. This function
one? Measures such as the Akaike information criterion (AIC),
                                                                        accounts for the expectation of various probabilistic factors,
the Bayesian information criterion (BIC) and the minimum
                                                                        such as the rate of infection transmission, population density
description length (MDL), address the balance between the
                                                                        and contact patterns. Note that although the x(t) on the right
number of observations and the model unknown parameters
                                                                        hand side of (1) could have been unified in φ(t), the above
to select between competing models with variable number of
                                                                        form has the advantages that φ(t) can be interpreted as the
parameters and different levels of accuracy [9], [10]. Finally,
                                                                        exponential rate, with inverse time units.
the physical interpretability of the model parameters and the                                                                       ∆
ability to estimate the parameters such that the model matches            Denoting the kth generation of the infection spread by xk =
real-world data, is what makes the whole modeling framework             x(k∆), (1) can be discretized as follows:
meaningful.                                                                                   xk+1 = [1 + ∆φ(k∆)]xk
                                                                                                                               ∆
                                                                        Now, defining the reproduction number rk = [1 + ∆φ(k∆)],
B. From stochastic infection propagation models to ordinary             it is evident that the population at the discretized time index
differential (difference) equation modeling                             k can be recursively found from the initial condition x0 :
   The outbreak of a contagious disease in a large population
                                                                                              xk = (rk−1 rk−2 · · · r0 )x0                        (2)
is a stochastic event. Starting from a single infected individual,
the infection is transmitted to others in a stochastic manner,          Apparently, if for all k, rk < 1 (or equivalently φ(t) < 0),
either by direct contact, proximity, or environmental traces (in-       the infection would decay to zero; otherwise if rk > 1 (or
fected objects left over in the environment). The new infected          φ(t) > 0) it spreads. In the simplest case, for which the
generation in turns transmits the infection (again probabilisti-        reproduction function is a constant φ(t) = λ, we have a
cally) to the healthy individuals that they meet or encounter.          constant reproduction number R0 = 1 + λ∆, resulting in an
During the primary stages of an epidemic outbreak, healthy-             exponential growth/decay:
infected individual encounters are statistically independent. As
                                                                                                       xk = x0 Rk0 ,                              (3)
a result, the chance of multiple infected people meeting a
single healthy individual is probabilistically low. Therefore,          or in the continuous case:
assuming that each infected individual contaminates R0 new
people on average (known as the reproduction number, more                                            x(t) = x(0)eλt                               (4)
rigorously defined in Section II-E), if R0 > 1 the disease              The equivalence of the discrete and continuous solutions is
spreads exponentially from one time step to another (for                evident up to the first order approximation of the derivative,
example on a daily basis). However, in a finite population,             as assumed in (1).
the exponential growth can not continue for ever. Depending
                                                                           1 Another interpretation is that after a while, it becomes more and more
on the population size and contact patterns, the probability
                                                                        difficult for the average infected person to meet R0 non-infected individuals,
of infected people encountering independent healthy indi-               and therefore the reproduction number drops and the number of new infections
viduals decreases. Therefore, after the initial outbreak that           decreases exponentially.
~~~

## Page 3

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                        3



   More generally, the reproduction function φ(t) (or rk in             Compartmental modeling is also known as mass transport
the discrete case) can be a time-varying function of factors            [15], or mass action [16], in other contexts. More technically, a
such as the total susceptible population, the population of             compartmental model is a weighted directed graph represen-
the exposed individuals (carriers of the disease but without            tation of a dynamic system. Each compartment corresponds
symptoms), contact patterns, and countermeasures such as                to a node of the graph and the linking arrows are the graph
social distancing and lockdowns. As shown in the sequel,                edges. From this perspective, for an n compartment system,
the notion of reproduction function (number) and its impact             the compartment variables can be considered as state variables
on epidemic outbreak generalizes to eigen-analysis of vector-           denoted in vector form as x(t) = [x1 (t), . . . , xn (t)]T . The
valued dynamic epidemic models (when the population is                  compartmental model provides a graphical representation of
divided into multiple groups of individuals known compart-              the state-space model:
ments), enabling the stability analysis of such models.
   As a reminder for later use, when λ < 0, the exponential                              ẋ(t) = f (x(t), w(t); θ(t), t)
                                                                                                                                       (5)
law in (4) implies that the population of the infected cases                             y(t) = g(x(t); θ(t), t) + v(t)
drops 63%, 86%, 95%, 98%, 99%, and 99.75% from its initial              where f (·) is the state dynamics function corresponding to
value, after λ−1 , 2λ−1 , 3λ−1 , 4λ−1 , 5λ−1 , and 6λ−1 time            the compartmental model graph (which can be possibly time-
units, respectively. The latter indicates for example that after        variant and nonlinear), w(t) = [w1 (t), . . . , wl (t)]T represents
6λ−1 time units, only 25 cases out of 10,000 would still be             deterministic or stochastic external system inputs, y(t) =
infected. This property is later used to estimate the model             [y1 (t), . . . , ym (t)]T is the vector of observable model vari-
parameters from clinical experimental results. It is good to note       ables considered as outputs (the measurements), g(·) if the
that although the exponential law for infection spread is the           function that maps the state variables to the observations
most common assumption, depending on the application, more              (measurements), v(t) = [v1 (t), . . . , vm (t)]T is the vector of
accurate non-exponential models have also been considered               measurement inaccuracies, considered as additive noise and
[14].                                                                   θ(t) = [θ1 (t), . . . , θp (t)]T is a vector of model parameters
                                                                        to be set or identified. Researchers familiar with estimation
C. Compartmental modeling                                               theory, have already guessed that the state-space form of
                                                                        (5), implies that one may eventually be able to estimate and
   Differential (difference) equations arise in many modeling
                                                                        predict the compartment variables from noisy measurements,
problems. The major application of these equations is when
                                                                        using state-space estimation techniques, such as the Kalman
the rate of change of a variable is related to other variables,
                                                                        or extended Kalman filter [17].
as it is so in most physical and biological systems. Many
                                                                           With this background, the basic steps of compartmental
powerful mathematical tools exist for the analysis and (nu-
                                                                        modeling are:
merical) solution of models based on differential equations.
Despite their vast applications, differential equations are dif-        1) Identifying the quantities of interest as distinct compart-
ficult to conceive and interpret without visualization. In this            ments and selecting a variable for each quantity as a
context, compartmental models are used as a visual means                   function of time. These variables are the state variables
of representing differential equations of dynamic systems. A               of the resulting state-space equations.
compartment is an abstract entity representing the quantity             2) Linking the compartments with arrows indicating the rate
of interest (volume, number, density, etc.). Depending on the              of quantity flow from each compartment to another (visu-
level of abstraction, each of the variables of interest (equivalent        ally denoted over the arrows connecting the compartments).
to system states in dynamic systems) are represented by                 3) Writing the corresponding first-order (linear or nonlinear)
a single compartment, conceptually represented by a box.                   differential equations for each of the state variables of the
Each compartment is assumed to be internally homogeneous,                  model. In writing the equations from the graph represen-
which implies that all entities assumed inside the compartment             tation, the edge weights multiplied by the state variable
are indistinguishable. For example, depending on the model                 of their start node are added to (subtracted from) the rate
complexity selected for modeling a certain epidemic disease,               change equation of the end node (start node). External
men and women at risk can be assumed to conform a single                   inputs can be considered to be originated from an external
compartment, or may alternatively be considered as different               node with value 1.
compartments. A similar partitioning may be considered for              4) Setting initial conditions and solving the system of equa-
different age groups, ethnicities, countries, etc., at a cost of a         tions (either analytically or numerically), which is in the
more complex (less parsimonious) model with additional states              form of a first-order state-space model.
and parameters to be identified. Apparently, the available real-        A compartmental model is linear (nonlinear), when its rate
world data may be insufficient for the parameter identification         flow factors are independent (dependent) of the state variables.
of a more detailed (complex) model.                                     A compartmental model is time-invariant (time-variant), when
   The compartments interact with one another through a set             its rate flow factors are independent (dependent) of time. Com-
of rate equations, visually represented by arrows between               partmental models may be open or closed. In closed systems,
the compartments. Therefore, compartmental models can be                the quantities are only passed between the compartments,
converted to a set of first order linear or nonlinear equations         while in open systems the quantities may flow into or out
(and vice versa), by writing the net flow into a compartment.           of the whole system. In a closed compartmental model, the
~~~

## Page 4

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                            4




                                                                                                                 γ
                              γx
          u                                           ρ
                  x                             z                                             s              i              r
                          α            β                                                            αi               β

                                   y
                                                                           Fig. 2. The basic susceptible-infected-recovered (SIR) model

Fig. 1. A sample compartmental model corresponding to the set of dynamic
equations in (6)
                                                                           in fact the fraction of each group’s population divided by N ).
                                                                           Accordingly, the system is closed and we have
sum of all the differential equations of the system is zero (for
all t).                                                                                           s(t) + i(t) + r(t) = 1                   (7)
Example 2. A three compartment model corresponding to the                  A compartmental model for the propagation of the disease is
following set of equations is shown in Fig. 1.                             shown in Fig. 2. The compartmental representation of Fig. 2
                dx(t)                                                      is equivalent to the following set of differential equations:
                      = u − γx(t)2 − αx(t)
                 dt                                                                            ds(t)
                dy(t)                                                                                = −αs(t)i(t) + γr(t)
                      = αx(t) − βy(t)                      (6)                                  dt
                 dt
                dz(t)                                                                          di(t)
                      = γx(t)2 + βy(t) − ρz(t)                                                       = αs(t)i(t) − βi(t)                   (8)
                 dt                                                                             dt
which can be put in the matrix form of (5). Due to the state-                                  dr(t)
                                                                                                     = βi(t) − γr(t)
dependency of the rate flow between x and z, the model is                                       dt
nonlinear. It is also an open system, since the sum of rate                Accordingly, moving from the susceptible group to the in-
changes is non-zero, i.e., there is net flow in and out of the             fected group takes place at a rate that is proportional to the
whole system (due to u and ρ).                                             population of the infected and susceptible groups, with pa-
                                                                           rameter α. At the same time, infected individuals are assumed
D. Mathematical epidemiology                                               to recover at a constant rate of β. Finally, considering that
   In order to model the propagation of epidemic diseases in a             the disease is not assumed to result in lifetime immunity
population, certain disease- and population-specific assump-               of the subjects, the recovered individuals again return to the
tions are required. The most common assumptions in this                    susceptible group at a fixed rate of γ. From (8), it is evident
context include:                                                           that
                                                                                             ds(t) di(t) dr(t)
• The diseases are contagious and transfer via contact.                                            +       +        =0                 (9)
• A disease may or may not be fatal.
                                                                                              dt       dt       dt
• There may be births during the period of study, and the                  which is in accordance with (7) and the fact that the system
   birth may (or may not) be congenitally transferred from the             is assumed to be closed (no births or deaths have been
   mother to the baby.                                                     considered).
• The disease can have an exposure period, during which the                   Assuming initial conditions for each group, the set of
   contaminants carry and spread the disease, but do not have              nonlinear equations (8) can be (numerically) solved to find the
   visible symptoms.                                                       evolution of the population of each compartment over time.
• Catching the disease may or may not result in short-term or              The numerical solution of a basic (non-fatal) SIR model is
   long-term immunity. Depending on the case, the recovered                shown in Fig. 3, with and without lifetime immunity. The time-
   patients can again become susceptible to the disease.                   step for numerical discretizing of the differential equations of
• Interventions such as medication, vaccination, lockdown,                 this simulation has been chosen to be ∆=0.1 of a day. Notice
   quarantine and social distancing can change the pattern of              how the outbreak of a disease that does not cause lifetime
   propagation.                                                            immunity (such as a typical flu), can result in a constant
Let us consider an example, which is the basic model that we               rate of illness throughout time, after its transient period. For
later extend for the COVIC-19 virus propagation pattern.                   widespread epidemic diseases, the healthcare strategists are in-
   1) The susceptible-infected-recovered model: A basic                    terested in the slopes of s(t), i(t) and r(t), rather than the total
model used for modeling epidemic diseases without lifetime                 number of infected individuals (as it is currently the case for
immunity is known as the susceptible-infected-recovered (SIR)              the COVID-19 Coronavirus). The prolongation of the disease
model [2], [18], [19]. In this model, the total population of              spread provides the better management of healthcare resources
N individuals exposed to an epidemic disease at each time                  such as hospitalization, medication, healthcare personnel, etc.
instant t is divided into three groups (each represented by a
compartment): the susceptible group fraction denoted by s(t),                For later reference, it is interesting to study the fixed-point
the infected group fraction denoted by i(t), and the recovered             of the SIR model (where ṡ(t) = i̇(t) = ṙ(t) = 0). Equating
group fraction denoted by r(t) (the compartment variables are              the left sides of (8) with zero, it can be algebraically shown
~~~

## Page 5

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                            5



                                                                                             replacing the perturbed point in (8) and neglecting second and
                      1
                                                                             S(t)            higher order terms containing ǫ, we obtain:
                                                                             I(t)
                     0.8                                                     R(t)
                                                                                                           ds(t)
                                                                                                                  = −α(1 − ǫ)ǫ ≈ −αǫ < 0
  Population Ratio




                                                                                                             dt
                     0.6                                                                                   di(t)
                                                                                                                  = α(1 − ǫ)ǫ − βǫ ≈ (α − β)ǫ             (12)
                                                                                                             dt
                     0.4                                                                                   dr(t)
                                                                                                                  = βǫ > 0
                                                                                                             dt
                     0.2
                                                                                             As a result, the first fixed-point is unstable, since due to the
                                                                                             sign of the derivatives of the perturbed system, the system’s
                      0
                           0                50              100                 150          dynamics drives the state vector away from the fixed-point
                                                   days                                      (since the population of the susceptible group has a negative
                                       (a) Basic SIR with immunity                           derivative). However, depending on whether α > β or not, the
                                                                                             outbreak may or may not result in an increase in the infected
                      1                                                                      population. Simply put, if the infection rate is greater than
                                                                             S(t)
                                                                             I(t)
                                                                                             the recovery rate (α > β) the disease would lead into an
                     0.8                                                     R(t)            outspread; but if the recovery rate is faster than the infection
  Population Ratio




                                                                                             rate (α < β) the percentage of the infected population
                     0.6                                                                     will remain close to zero. In either case, for a non-fatal
                                                                                             non-immunizing disease, all individuals that become infected
                     0.4                                                                     recover after a while and move to the recovered group and
                                                                                             again go back to the susceptible group at a rate of γ. Note
                     0.2                                                                     that a SIR model with a non-zero infected population fraction
                                                                                             in steady-state, indicates that there is a constant flow between
                      0
                           0                50              100                 150          the compartments, i.e., people are constantly contaminated,
                                                   days                                      recovered and again become susceptible to the disease.
                                     (b) Basic SIR without immunity
                                                                                                Perturbing the second fixed-point results in
                                                                                                  ds(t)         β
Fig. 3. Simulation of a basic non-fatal SIR model with α=0.5 and β=0.05                                 = −α( − ǫ)(I0 + ǫ) + βI0 ≈ ǫ(αI0 − β)
in two cases: a) γ=0.0 (lifetime immunity) and b) γ=0.04                                            dt          α
                                                                                                  di(t)       β
                                                                                                        = α( − ǫ)(I0 + ǫ) − βI0 ≈ −ǫ(αI0 − β)         (13)
                                                                                                   dt         α
that if α, γ 6= 0 (the non-immunizing case), the SIR model                                        dr(t)
                                                                                                         = β(I0 + ǫ) − β(I0 + ǫ) = 0
has only two fixed-points:                                                                          dt
                                                                                             In this case, depending on whether (αI0 − β) > 0 or not, the
                                  (s∗ (t), i∗ (t), r∗ (t)) = (1, 0, 0)                       fixed-point may be stable or unstable.
                                                              β       β               (10)      For later use, we can show that during the outbreak of the
                                  (s∗ (t), i∗ (t), r∗ (t)) = ( , I0 , I0 )
                                                              α        γ                     SIR model (s(t) ≈ 1), the number of infected cases follows
                                                                                             an exponential pattern:
                               ∆ γ(α − β)
where I0 =              . The first fixed-point corresponds to the                                              i(t) ≈ i(0) exp[(α − β)t]                (14)
             α(γ + β)
lack of any infected cases, and the second corresponds to a
                                                                                               2) The fatal SIR model: A fatal version of the SIR model
persistent disease in the population, as illustrated in Fig. 3(b).
                                                                                             with rates of birth µ∗ and with different death rates from the
This situation is only reachable if β < α, i.e., when the
                                                                                             susceptible (µs ), infected (µi ) and recovered (µr ) groups is
infection rate is greater than the recovery rate.
                                                                                             shown in Fig. 4. This system is no longer closed and its state
   We can also verify whether or not the fixed-points are
                                                                                             equations can be written as follows:
stable. Various methods can be used for this purpose. Perhaps,
the most tangible approach is based on perturbation theory.                                             ds(t)
                                                                                                              = γr(t) − αs(t)i(t) − µs s(t) + µ∗
Simply stated, one can add small perturbations to the fixed-                                             dt
points of the system and check whether or not the perturbations                                         di(t)
                                                                                                              = αs(t)i(t) − βi(t) − µi i(t)              (15)
are compensated by the system’s dynamics by pushing the                                                  dt
state vector back to its fixed-point. Accordingly, the first fixed-                                     dr(t)
                                                                                                              = βi(t) − γr(t) − µr r(t)
point in (10) can be perturbed to:                                                                       dt

                                    (s(t), i(t), r(t)) = (1 − ǫ, ǫ, 0)                (11)
                                                                                             E. The basic reproduction number (R0)
where 0 < ǫ ≪ 1 is a small perturbation (e.g., equivalent to                                  As noted before, the outbreak threshold of epidemiology
a single case of disease outbreak in a large population). Now                                models is known as the basic reproduction number R0 . It is
~~~

## Page 6

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                              6




                                       γ                                      Example 3. In the SIR model (8), if we replace r(t) = 1 −
                   µ∗                                                         s(t) − i(t) from (7), the model reduces to:
                             αi             β
                    s              i              r                                      di(t)
                                                                                               = αs(t)i(t) − βi(t)
                        µs             µi             µr                                  dt                                                (20)
                                                                                         ds(t)
                                                                                               = −αs(t)i(t) + γ[1 − s(t) − i(t)]
Fig. 4. The susceptible-infected-recovered (SIR) model with birth and death               dt
rates                                                                         Therefore,
                                                                                                                                        
                                                                                      αs(t)i(t)                       −βi(t)
                                                                               F=                 , V=
defined as the average number of secondary infections due                                 0                −αs(t)i(t) + γ[1 − s(t) − i(t)]
to an infected individual hosted by a completely susceptible                                                                            (21)
population [20]–[22], [1, Ch. 7]. The R0 during epidemic                      and at the fixed-point x = (0, 1)
outbreak is generally greater than the average infections (R)
                                                                                                             
                                                                                                  αs(t) αi(t)
at any other time other than the outbreak.                                        ∇x F (x∗ ) =
                                                                                                    0      0 i(t)=0,s(t)=1
   From the mathematical modeling perspective, a formal                                         
                                                                                                      −β            0
                                                                                                                          
definition of R0 was first presented in [23]. Consider the                        ∇x V(x ) =
                                                                                           ∗
                                                                                                  −αs(t) − γ −αi(t) − γ i(t)=0,s(t)=1
general dynamic representation of a compartmental model:                                                                                (22)
                                                                              which results in the reproduction number:
                              ẋ(t) = f (x(t))                        (16)
                                                                                                                       α
                                                                                                   R0 = ρ(−FV−1 ) =                     (23)
where x(t) = [x1 (t), x2 (t), . . . , xp (t), xp+1 (t), . . . , xn (t)]T                                               β
is the state vector (compartment variables), such that                        where we can see that the epidemic stability condition R0 < 1
x1 (t), . . . , xp (t) correspond to the infected compartments (ex-           is identical to the stability condition α < β, found for the SIR
posed, infected, etc.), and xp+1 (t), . . . , xn (t) are all the other        model in Section II-D1.
variables (susceptibles, recovered, passed-away, etc.). We next
partition each row of f (·) as follows:                                          Comparing (23) and (14) we notice that although the
                                                                              epidemic stability condition found from R0 is related to the
                    f (x(t)) = F (x(t)) + V(x(t))                     (17)    outbreak exponent (slope of infection during outbreak), but
                                                                              they are not the same quantities.
where F (·) groups all the terms of f (x(t)), which correspond                   In fact, a major drawback of the conventional definition
to new infections (the portion of the population, which are                   of R0 using the NGM is that the discretization time (or
either susceptible or had fully recovered, but are becoming                   generation period) is discarded in its definition and therefore,
exposed or infected due to contact with the exposed or                        there is no direct analogy between the discrete-time and
infected). On the other hand, V(·) groups all the other terms                 continuous-time outbreak behavior of the epidemic. Motivated
of the equations, including removals from the infected groups                 by this fact and based on the analogy between the discrete-
and other compartmental transitions.                                          time and continuous-time models presented in Section II-B,
   The Jacobian of F (·) and V(·) are next calculated at the no               we hereby propose an alternative definition of the reproduction
infection fixed-point x∗ = [0, 0, . . . , 0, x∗p+1 , . . . , x∗n ]T :         number:
                                                                              Proposition: An alternative definition of the repro-
                 F 0                   V                   0                      duction number is
     ∇x F (x ) =
               ∗
                       , ∇x V(x∗ ) =                                  (18)
                 0 0                  J3                   J4
                                                                                                       R̃0 = eλ1 ∆                   (24)
Finally, the reproduction number is defined as the spectral                       where λ1 is the real-part of the dominant eigenvalue
radius (leading eigenvalue) of the negative of the so-called                      of the dynamic model’s Jacobian evaluated at the
next generation matrix (NGM) FV−1 :                                               fixed-point of interest, and ∆ is the generation time
                                                                                  unit (or discretization period). Accordingly, for an
                             R0 = ρ(−FV−1 )                           (19)        irreducible dynamic model, R̃0 < 1 (or λ1 < 0)
                                                                                  and R̃0 > 1 (or λ1 > 0) correspond to stable and
which is proved to have the biological properties of the
                                                                                  unstable epidemic conditions, respectively.
reproduction number for epidemic studies.
   In fact, while the threshold between stability and instability                It is clear that for small generation time units ∆ (small as
of an epidemic can be defined in various forms, only the                      compared with the compartmental model “rate of variations”
definition based on R0 is biologically popular [22]. In [23],                 in time), we have:
it is also shown how different partitionings of the state-space                                        R̃0 ≈ 1 + λ1 ∆                   (25)
model can lead to different spectral radii; however, only the
choice described in (17) leads to the biologically meaningful                 The major advantage of the above definition for the reproduc-
definition of R0 .                                                            tion number is that the time unit between generations appears
                                                                              in the definition. Therefore, the R̃0 of different epidemics that
~~~

## Page 7

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                7


                                                                                                  s                   γ
have been experimentally obtained from real-world data ac-                                                    ρ
quired with different generation time units become comparable                       αe e + αi i
with one another. Moreover, our studies on various epidemic                                             κ                 β
                                                                                                  e               i                r
models shows that the stability condition λ1 < 0 (or R̃0 < 1)
is exactly equivalent to the R0 < 1 condition obtained from                                                            µ
the common definition of the basic reproduction number using                                                                       p
the NGM. The mathematical proof of equivalence of the two
conditions remains as future work.                                      Fig. 5. Proposed Model I: the fatal susceptible-exposed-infected-recovered
                                                                        (SEIR) model for Coronavirus modeling with a unique recovery group

             III. P ROPOSED E PIDEMIC M ODEL I
   Many infectious diseases are characterized by an incuba-               In (27), similar to the classical SIR model, the interpretation
tion period between exposure and the outbreak of clinical               of the nonlinear terms including s(t)e(t) and s(t)i(t) is that
symptoms. Subjects exposed to the infection are much more               the rate of exposure to the virus is proportional the population
dangerous for the public as compared to the subjects showing            of both the susceptible and exposed/infected subjects.
clinical symptoms. The condition becomes more and more                    Note that the system closure constraint (26) gives an excess
dangerous, with the increase of the isncubation rate. A well-           degree of freedom, which can be used to reduce the model
known case is the HIV virus in its clinical latency stage.              order by replacing s(t) = 1 − e(t) − i(t) − r(t) − p(t). This
The experience of the COVID-19 shows that a two-week                    simplifies the compartmental model as follows:
incubation period can spread a virus worldwide and almost                   de(t)
at any level of the society. Remember that any two of us                          = [1 − e(t) − i(t) − r(t) − p(t)][αe e(t) + αi i(t)]
                                                                             dt
are only six handshakes apart!2 For this reason, an additional                    − κe(t) − ρe(t)
compartment is added between the susceptibility and infection               di(t)
stages of the SIR model, which accounts for the asymptomatic                      = κe(t) − βi(t) − µi(t)
                                                                             dt
exposed subjects. Moreover, since we are also interested in                 dr(t)
minimizing the mortality rate of the disease, a termination                       = βi(t) + ρe(t) − γr(t)
                                                                             dt
compartment is dedicated to the passed-away population. The                 dp(t)
variables of the model are therefore:                                             = µi(t)
                                                                             dt
1) s(t): The susceptible population fraction (the number of                                                                         (28)
   individuals in danger of being infected, divided by the total
   population).                                                         A. Measurements model
2) e(t): The exposed population fraction (the number of indi-             Among the state variables of the proposed model, all
   viduals exposed to the virus but without having symptoms,            except e(t) are directly measurable (with potential errors). The
   divided by the total population).                                    measurements can be formulated in matrix form as follows:
3) i(t): The infected population fraction (the number of
                                                                                                         e(t)
                                                                                                                
   infected individuals with symptoms, divided by the total
                                                                                                                          
                                                                               I(t)         0 1 0 0  i(t)             vi (t)
   population).
                                                                             R(t) =  0 0 1 0                 +  vr (t)       (29)
                                                                                                                         
4) r(t): The recovered population fraction (the number of                                                   r(t)
                                                                              P (t)         0   0  0  1                 vp (t)
   recovered individuals, divided by the total population).                                                  p(t)
5) p(t): The number of individuals that pass away due to the
   disease, divided by the total population).                           where I(t) is the fraction of reported infections, R(t) is
                                                                        the fraction of reported recoveries (both symptomatic and
Keeping in mind that
                                                                        asymptomatic), P (t) is the fraction of reported death tolls,
              s(t) + e(t) + i(t) + r(t) + p(t) = 1              (26)    and v(t) = [vi (t), vr (t), vp (t)]T is measurement noise. The
                                                                        evident sources of measurement noises include: unavailable
the proposed model and its compartmental representation are             information regrading the exact population, intentional and
shown in equations (27) and Fig. 5.                                     unintentional misreported values, mis-classified reasons of
                                                                        death (especially for the elderly or subjects suffering from
    Model I:                                                            multiple health issues), and the marginal cases that may be
    ds(t)                                                               unknown or misclassified for the healthcare system. Equation
          = −αe s(t)e(t) − αi s(t)i(t) + γr(t)
     dt                                                                 (29) can be written in more compact form as follows:
    de(t)
          = αe s(t)e(t) + αi s(t)i(t) − κe(t) − ρe(t)                                            y(t) = Cx(t) + v(t)                         (30)
     dt
    di(t)                                                       (27)
          = κe(t) − βi(t) − µi(t)                                       where x(t) = [e(t), i(t), r(t), p(t)]T is the reduced state-
     dt
    dr(t)                                                               vector. Although the variable e(t) is not directly measurable
          = βi(t) + ρe(t) − γr(t)
     dt                                                                 from the available public data, we will show in Section V
    dp(t)
          = µi(t)                                                         2 Cf. https://en.wikipedia.org/wiki/Six degrees   of separation
     dt
~~~

## Page 8

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                       8



that under certain conditions, e(t) can be estimated from the             noted 99.75% percentage as the target infection drop-out
measurements.                                                             threshold, and advised 14 days of quarantine for the whole
   Note that in the above measurement model, it is assumed                population. In that case, we can select κ = 6/14 = 0.43
that R(t) is the total recovery fraction of both the symptomatic          (inverse days) in our model. Apparently, there is a lot of
and asymptomatic cases, assuming that the asymptomatic re-                simplifications in this discussion; the age range, the subject-
coveries are measurable by (random or systematic) public tests            specific body immune system features, the severeness of
over the population, such as the antibody tests that have been            the virus and many more factors have been neglected. But
conducted by some nations during the COVID-19 outbreak.                   it gives an idea about how the parameters can be tuned
In Section IV, the model is modified to a more practical case,            in practice, up to a reasonable order of magnitude. With
in which only the recoveries due to the symptomatic cases are             this background, we now explain the interpretation of each
measured.                                                                 parameter of the model.
                                                                          We should add that wide screening policies adopted by
                                                                          certain countries are external factors that can significantly
B. Model assumptions and level of abstraction
                                                                          accelerate the identification of the infected cases. In this
  The simplifying assumptions behind the proposed model                   case, screening is a factor that increases κ.
are:                                                                    • αi : The contagion factor between the infected and suscepti-
1) The model variables are assumed to be continuous in both               ble populations, which is related to the contagiousness of the
   amplitude and time.                                                    virus and social factors such as personal hygiene, population
2) Birth and natural deaths have been neglected. Therefore,               density and level of human interactions. In order to find the
   other parameters leading to changes in the population are              range (or order of magnitude) of this parameter, we can start
   not considered. Neglecting the birth rate is also supported            with the contagion factors of more known viruses, such as
   by the current findings that babies are not susceptible to             flu and influenza, which are more or less influenced by the
   this virus and to the best of our knowledge, no congenital             same spreading factors.
   transmissions of the virus from mothers to fetuses have              • αe : The contagion factor between the exposed and suscepti-
   been reported.                                                         ble populations. This parameter is logically far greater than
3) In the current study, we do not distinguish between male               αi , since in ordinary conditions (before lockdowns and quar-
   and female subjects; although the current global toll of the           antine), people rarely avoid contact with an asymptomatic
   virus suggests that men have been more vulnerable to the               individual; nor does the individual itself avoid interaction
   virus than women.                                                      with others.
4) Age ranges have not been considered; although we known               • γ: The reinfection rate, or the rate of returning from the
   that higher aged subjects are more vulnerable to the virus             recovered group to the susceptible group. This happens for
   and countries have different population pyramids.                      the cases that the body does not develop lifetime immunity
5) Moreover, in this primary version, we have not yet consid-             after recovery, or the virus itself starts to mutate over
   ered the possibility of vaccination.                                   time. This parameter is the inverse of the immunity rate
6) Geopolitical factors such as distance, country borders and             of the virus. It is currently too early to comment about the
   continental differences have also been ignored. But con-               immunity characteristics of the Coronavirus3. Although at
   sidering that different countries have adopted customized              least one case of reinfection soon after recovery has been
   countermeasures against the virus spread, the model pa-                reported, preliminary research have suggested short-term
   rameters are fitted over country-level data.                           immunity of up to four months.
                                                                        • β: The recovery rate of the infected cases. By considering
                                                                          the fourth equation in (27), we can denote the change in
C. Model parameters
                                                                          the number of hospitalized recoveries (or under control
   Having formed the model, we now explain its parameters                 in any form, e.g., under home-care) by rh , resulting in
and their relationship with real-world factors and clinical               rh (t + ∆) − rh (t) ≈ ∆βi(t), where ∆ is the time unit of
protocols. The techniques for estimating and fitting these                approximation (for example 1 day). Therefore, the parameter
parameters on real data is later detailed in Section VI.                  β can be approximated by dividing the daily recovery count
   Note that all the model parameters have the dimension of               of the population under study, by the total infected cases
inverse time, to balance the left and right side dimensions               in the same day. In the real world, apart from the body
of (27), and that the studied model is essentially based on               strength of the infected subject in resisting against the virus,
an exponential law assumption, as detailed in Section II-B.               this parameter depends on the healthcare infrastructure of a
Therefore, we can find rules of thumb for selecting the model             country (hospitalization facilities, availability of medication,
parameters based on clinical facts and protocols.                         number of intensive care units, etc.).
• κ: The rate at which symptoms appear in exposed cases,                • ρ: The recovery rate of the exposed cases (the cases that
  resulting in transition from the exposed to the infected                are exposed, but recover without any symptoms). This
  population. The selection of this parameter is according to
  the exponential law detailed in Section II-B. Assume that we             3 Refer to:
  are dealing with an extremely contagious disease for which            https://www.who.int/docs/default-source/coronaviruse/
  the healthcare decision makers have agreed on the above               who-china-joint-mission-on-covid-19-final-report.pdf
~~~

## Page 9

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                 9



  parameter is not directly measurable from pure observations              E. Model analysis during outbreak
  and requires lab-based experiments. However, we logically                   Let us study the model during the initial outbreak of the
  expect this parameter to be of the same order or greater than            epidemic, when the infection toll is still much smaller than
  the parameter β (the recovery rate of the infected population            the total population. For instance, suppose that a country
  with symptoms).                                                          has 100,000 of exposed or infected cases, which is indeed
• µ: The mortality rate of the infected cases. By approximat-              significant for any country, as it is far beyond the available
  ing the last equation in (27) by p(t + ∆) − p(t) ≈ ∆µi(t),               number of intensive care unit beds of even the most developed
  where ∆ is the time unit of approximation (for example                   countries4 . But for a 100 million population country, such an
  1 day), the parameter µ can be approximated by dividing                  exposure/infection toll is only 0.1% of the total population.
  the daily death toll by the total infected cases in the same             Therefore, during the primary phases of the disease spread,
  day. As with β, the mortality of the virus itself, the immune            the model can be simplified by assuming that the susceptible
  system of the subjects, and the medical infrastructure are               population is almost constant (s(t) ≈ 1) and ds(t)/dt ≈ 0, re-
  important factors that influence the parameter.                          gardless of the other parameters of the model. This assumption
• e0 : The initial exposed population (seed).                              practically implies that the total population is not important
   By studying the above factors, we can see that the only                 during an epidemic outbreak (in low percentages of infection),
parameters of the model that can be changed in the short-                  resulting in
term (before the development of long-term solutions such
                                                                                Result 1. In low percentages of infection, the per-
as vaccination, medication, improvement of hospitalization
                                                                                formance of epidemic control policies of states,
facilities, etc.), is to reduce the infection rates by minimizing
                                                                                countries, and regions should not be evaluated by
human contacts (social distancing), or to apply public screen-
                                                                                normalizing the infection/recovery/death tolls to their
ing. These are the two policies, which have been adopted
                                                                                total population; but rather the net values should be
worldwide.
                                                                                compared.

                                                                              This result has also been approved in previous research
D. Fixed-point analysis                                                    based on model fitting on data from several epidemic diseases,
   As with the basic SIR model presented in Example II-D1,                 showing that the disease spread is considerably independent
the fixed-point(s) of the model can be sought by letting the left          of the total population size [20].
hand sides of all equations in (27) equal to zero. Accordingly,               Under this assumption, (27) is simplified to the linear set
assuming that all the model parameters are nonzero, the only               of equations:
fixed-point is the no-disease case (i(t) = e(t) = r(t) = 0):                    de(t)
                                                                                     
                                                                               dt                                               e(t)
  (s∗ (t), e∗ (t), i∗ (t), r∗ (t), p∗ (t)) = (1 − p0 , 0, 0, 0, p0) (31)       di(t)       αe − κ − ρ         αi        0 0
                                                                                     
                                                                                                                                    i(t)
                                                                                                   κ        −β − µ 0 0 
                                                                                     
                                                                               dt  
                                                                                      ≈                                               
where 0 ≤ p0 ≤ 1 is the steady-state total death fraction. The                 dr(t)  
                                                                              
                                                                                                   ρ            β        −γ 0   r(t)
                                                                                                                                         
stability of this fixed-point can be addressed by perturbing the                                   0            µ         0 0
                                                                                     
                                                                               dt                                                  p(t)
fixed-point with a minor exposure ǫ (which can correspond to                  
                                                                                dp(t)
                                                                                      
a single new exposed case in the real world):                                    dt
                                                                                                                                         (34)
   (s(t), e(t), i(t), r(t), p(t)) = (1 − p0 − ǫ, ǫ, 0, 0, p0)      (32)    Defining x(t) = [e(t), i(t), r(t), p(t)]T , (34) can be written in
                                                                           matrix form:
                                                                                                   d
Putting this point in the state dynamics (27), we find:                                               x(t) = Ax(t)                       (35)
                                                                                                   dt
 ds(t)                                                                     where A is the 4×4 state matrix on the right hand side of (34).
        = −αe (1 − p0 − ǫ)ǫ ≈ −αe (1 − p0 )ǫ < 0                           Equation (35) can be solved for an arbitrary initial condition,
   dt
 de(t)                                                                     such as x(0) = (e0 , 0, 0, 0). The characteristic function of this
        = αe (1 − p0 − ǫ)ǫ − κǫ − ρǫ ≈ (αe − αe p0 − κ − ρ)ǫ               linear system is:
   dt
 di(t)                                                                     |λI − A| = λ(λ + γ)[λ2 + (β + µ − δ)λ − δ(β + µ) − καi ] = 0
        = κǫ > 0
   dt                                                                                                                               (36)
 dr(t)                                                                              ∆
                                                                           where δ = (αe − κ − ρ). Therefore the system’s eigenvalues
        = ρǫ > 0
   dt                                                                      are:
 dp(t)                                                                                              p
        =0                                                                             δ − β − µ + (δ + β + µ)2 + 4καi
   dt                                                                             λ1 =
                                                           (33)                                     p 2
which is unstable, i.e., the system’s dynamics drives it away                          δ − β − µ − (δ + β + µ)2 + 4καi              (37)
                                                                                  λ2 =
from the fixed-point in the direction of reducing the healthy                                           2
cases, resulting in further infection. A more rigorous study of                   λ3 = 0, λ4 = −γ
the system stability conditions is presented in the following                 4 See for example:
sections using eigenanalysis.                                              https://link.springer.com/article/10.1007/s00134-012-2627-8/tables/2
~~~

## Page 10

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                10



which are all real-valued. Moreover, it is straightforward to                Result 2. During an exponential outbreak of an
check that λ1 > δ > λ2 . The eigenvectors corresponding to                   epidemic (λ1 > 0), the system is unstable and with-
each eigenvalue are:                                                         out enforcing temporary lockdowns, social distancing
                                                                             and quarantine of the infected cases (resulting in the
               λ1 − δ ραi + β(λ1 − δ) µ(λ1 − δ) T                            model parameter changes), the exponential increase
   v1 = k1 [1,           ,                  ,        ]
                  αi       αi (λ1 + γ)         αi λ1                         in the number of infected subjects continues to a
               λ2 − δ ραi + β(λ2 − δ) µ(λ2 − δ) T               (38)         point where a significant percentage of the popula-
   v2 = k2 [1,           ,                  ,        ]
                  αi       αi (λ2 + γ)         αi λ2                         tion is infected.
   v3 = [0, 0, 0, k3 ]T , v4 = [0, 0, k4 , 0]T
                                                                          Using the method detailed in Section II-E, we can further
where k1 , k2 , k3 and k4 are arbitrary constants. The general          show that for the epidemic model (27), the reproduction
form of the solution of the compartmental variables is a                number (spectral radius of the NGM) is equal to:
summation of exponential terms with the above exponential
rates and eivenvectors:                                                                               αe (β + µ) + καi
                                                                                              R0 =                                            (42)
                                                                                                       (κ + ρ)(β + µ)
                               4
                                                                        Apparently, R0 < 1 exactly simplifies to the stability condition
                               X
                      x(t) =         ak eλk t vk                (39)
                               k=1                                      in (41), when λ1 < 0.

Specifically, after some algebraic simplifications, we can cal-              Result 3. Under countermeasures, the model eigen-
culate the infected and exposed populations as follows:                      values change and λ1 (the dominant eigenvalue of the
                                                                             linearized dynamic model) is the single parameter
          e0 (λ1 − δ)(δ − λ2 )                                               that can be tracked as a score for evaluating how
  i(t) =                       [exp (λ1 t) − exp (λ2 t)]                     good countermeasures such as social distancing and
              αi (λ1 − λ2 )
              e0                                                             quarantine are performing.
   e(t) =          [(λ1 − δ) exp (λ2 t) + (δ − λ2 ) exp (λ1 t)]
           λ1 − λ2
                                                             (40)          Considering that the death toll p(t) is composed of the same
From the last equation in (27), it is clear that the death toll         exponential terms as the infected cases in (40), the above result
will not stop before i(t) = 0. Also from (40), we can see that          is indeed disturbing.
since λ1 is the dominant eigenvalue, the steady-state behavior             It is also interesting to observe from (40 ) that the population
and whether or not i(t) and e(t) diverge from or converge to            of the different compartments of the model is only linearly
zero, depends on the sign of λ1 . The necessary and sufficient          proportional to the initial exposed population size e0 5 . There-
condition for the linearized system’s stability (stopping the           fore, for a large population (at the level of a populated city or
death doll) is λ1 < 0, which simplifies to καi + δ(β + µ) < 0,          country), the initial infected seed size is not as important as the
or:                                                                     other model parameters that influence the exponential behavior
                  καi < (κ + ρ − αe )(β + µ)                    (41)    of the model (such as the social contact rates). Therefore:

                                                                             Result 4. The initial seed size is not the most critical
A sufficient condition that guarantees this property is when                 parameter for epidemic management. Regions with
αi = αe = 0. The condition αi = 0 implies that the                           smaller initial seeds of infected/exposed cases may
susceptible group avoids contact with the infected ones. How-                end up with a higher infected and death toll depend-
ever, the second condition (αe = 0) is difficult to fulfill                  ing on their infection rates, defined by factors such
in the real-world, since the exposed group do not have any                   as human-contact rate and personal hygiene.
symptoms. This is why social distancing is required to enforce
αe ≈ 0 and to permit all the exposed subjects to move to the              Another interesting property is to check the ratio between
infected group without infecting new individuals, after which           the number of infected (which is measurable in the real world)
the asymptomatic group can be all considered clear of the               and the number of exposed (which is not directly measurable).
disease. Another practical case is when αi ≈ 0 (healthy people          From (40), we can find6 :
avoid contact with the infected) and κ + ρ > αe (the rate of
recovery of the exposed or the appearance of their symptoms                        i(t)          exp(λ̃1 t) − exp(−λ̃2 t)
is faster than the rate of new exposures). This condition is                            =                                                     (43)
                                                                                   e(t)   αi [λ̃1 exp(λ̃1 t) + λ̃−1
                                                                                                −1
                                                                                                                 2 exp(−λ̃2 t)]
fulfilled by social distancing and lockdown (isolation of even
the asymptomatic cases for a certain period).                                        ∆                        ∆
                                                                        where λ̃1 = λ1 − δ and λ̃2 = δ − λ2 are both positive.
   However, if none of the above conditions are fulfilled and           Therefore, when the terms containing exp(−λ̃2 t), which is
λ1 > 0, the number of exposed and infected cases increases              a decaying exponential, vanish and the epidemic model is still
exponentially at a rate of λ1 . In this case, with fixed system
parameters, the infection rate rises exponentially up to a point          5 Note that the COVID-19 is believed to have started from a single case.
at which the linear approximation does no longer hold. This                6 The numerator and denominator of (43) have been multiplied by exp(−δt)
practically translates into:                                            to obtain the simplified form.
~~~

## Page 11

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                          11



in its linear phase (i(t) ≪ s(t) or s(t) ≈ 1), the ratio can be         observed and reported by the healthcare units. The dynamic
approximated by:                                                        system corresponding to this model is:

           i(t)   λ̃1                                                       Model II:
                →            for t ≫ λ̃−1
                                       2 and i(t) ≪ s(t)        (44)
           e(t)   αi                                                        ds(t)
                                                                                    = −αe s(t)e(t) − αi s(t)i(t) + γe re (t) + γi ri (t)
                                                                              dt
which gives the following practical result:                                 de(t)
                                                                                    = αe s(t)e(t) + αi s(t)i(t) − κe(t) − ρe(t)
                                                                              dt
     Result 5. During the primary phases of an epidemic                     di(t)
                                                                                    = κe(t) − βi(t) − µi(t)
     outbreak (when the number of contaminated cases                          dt
                                                                            dre (t)
     has an exponential growth, but the percentage of                                = ρe(t) − γe re (t)
     the infected individuals to the total population is                       dt
                                                                            dri (t)
     still small), the number of exposed subjects can be                             = βi(t) − γi ri (t)
                                                                               dt
     approximated by e(t) ≈ αi λ̃−1 1 i(t), permitting its                  dp(t)
     estimation from i(t).                                                          = µi(t)
                                                                               dt
                                                                                                                                        (45)
                                                                        subject to s(t)+e(t)+i(t)+re (t)+ri (t)+p(t) = 1, which can
F. Repeated waves of epidemic                                           again be used to reduce the model order by omitting one of
                                                                        the model variables (e.g., s(t)). In the latter case, we assume
   The peaks of the infected group population, and its potential        that the observed variables are I(t), Ri (t) and P (t), resulting
repetition in time, is important from the strategic viewpoint           in the following observation model:
[24]. These points correspond to local or global extremums of                                                         
i(t), which mathematically correspond to where di(t)/dt = 0                                                       e(t)
in (27), i.e., where i(t) = κe(t)/(β + µ). It can be shown
                                                                                                                               
                                                                              I(t)                                i(t)       vi (t)
                                                                                                             
                                                                                          0 1 0 0 0 
that this leads to a reduced order set of nonlinear dynamic                                                           
                                                                           Ri (t) =  0 0 0 1 0             re (t) +  vr (t) (46)
                                                                                                                                
equations, which can be solved for the remaining variables
                                                                             P (t)        0 0 0 0 1            ri (t)
                                                                                                                       
                                                                                                                             vp (t)
[s(t), e(t), r(t), p(t)]T . The simulations demonstrated in the
sequel, show that the infected population can have multiple                                                       p(t)
local peaks over time, with recurrent behaviors, proving that:
                                                                        which can be written in compact form, as in (30).
     Result 6. The epidemic disease can repeat pseudo-                     Similar to the first model, under the assumption of low
     periodically over time (in later seasons or years)                 fraction of infection (during epidemic outbreak) and omitting
     and turn into a persistent disease in the long term.               the variable s(t), (45) simplifies to:
     The amplitude and time gap of the infection peaks                   
                                                                            de(t)
                                                                                   
     depends on the model parameters.                                     dt                                                            
                                                                          di(t)                                                    e(t)
                                                                                                                                
   This behavior has been observed in previous pandemics,                            αe − κ − ρ        αi    0          0    0 
                                                                          dt                                                     i(t)
                                                                                                                                           
such as the 1918 pandemic influenza, known as the Spanish flu,                             κ           −β − µ  0          0    0 
                                                                          dre (t)  
                                                                                                                                      
                                                                                   ≈     ρ             0    −γe         0    0 
                                                                                                                                   re (t)
                                                                                                                                          
where three pandemic waves of infection have been observed               
                                                                          dt  
                                                                                           0             β     0         −γi   0  ri (t)
                                                                                                                                   
within an interval of a few months7 . A mathematical study
                                                                                                                                 
                                                                          dri (t) 
                                                                                                                                         
                                                                                           0             µ     0          0    0
                                                                                                                                      p(t)
                                                                                  
of sustained oscillations of similar compartmental models has             dt 
                                                                            dp(t)
                                                                                  
been studied in previous research [19], [25].
                                                                             dt
                                                                                                                                         (47)
                                                                        Defining the state vector x(t) = [e(t), i(t), re (t), ri (t), p(t)]T ,
              IV. P ROPOSED E PIDEMIC M ODEL II
                                                                        (47) can be written in a matrix form similar to (35), where
   The proposed model can be extended from various aspects.             A is now the 5×5 state matrix on the right hand side of (47)
One such extension is to separate the recoveries from expo-             and solved for an arbitrary initial condition. The characteristic
sure from the recoveries from infection. The advantage of               function of this linear system is:
this separation is that in practice, the subjects that recover
without any symptoms may only be identified by broad public             |λI−A| = λ(λ+γe )(λ+γi )[λ2 +(β+µ−δ)λ−δ(β+µ)−καi ]
screening, which is not very practical for a large population.                                                                    (48)
                                                                                                      ∆
While the infected individuals that recover are already known           where as in the first model δ = (αe − κ − ρ), resulting in the
for the healthcare system and are easy to monitor. Based on             following eigenvalues:
this idea, the proposed extension of the model is as shown                                        p
                                                                                     δ − β − µ + (δ + β + µ)2 + 4καi
in Fig. 6. Accordingly, the variables i(t), p(t) and ri (t)                    λ1 =
(the recoveries from infection) are the variables that can be                                     p 2
                                                                                     δ − β − µ − (δ + β + µ)2 + 4καi              (49)
                                                                               λ2 =
  7 Cf. https://en.wikipedia.org/wiki/Spanish flu
                                                                                                       2
                                                                               λ3 = 0, λ4 = −γe , λ5 = −γi
~~~

## Page 12

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                    12


                 γe        re
                                                                        If O k has rank n (the number of state variables, in either of
                          ρ                                             the proposed models), all the state variables of the linearized
                                  κ              µ                      models (34) and (47) are observable at the outputs, which
        s                     e          i             p
            αe e + αi i                                                 means that they can be estimated from the observations in
                                             β                          finite time. It is straightforward to numerically calculate (51)
                                         ri                             for arbitrary choices of the model parameters of Model I and
                          γi                                            Model II, and to check that none of its columns are linearly
Fig. 6. Proposed Model II: an extension of the fatal SEIR model for
                                                                        dependent8. Therefore, all the state variables, including e(t),
Coronavirus modeling, with separate recovery groups from exposure and   are observable and may be estimated using state estimation
infection                                                               techniques such as the Kalman filter (as the optimal linear
                                                                        estimator).
In this case, the eigenvectors corresponding to each eigenvalue
are:                                                                    B. Observability in the general case
                λ1 − δ        ρ     β(λ1 − δ) µ(λ1 − δ) T                  In the general case, where the number of exposed/infected
   v1 = k1 [1,           ,        ,              ,         ]            cases exceeds several percents of the population, the variations
                   αi      λ1 + γe αi (λ1 + γi )     αi λ1
                λ2 − δ        ρ     β(λ2 − δ) µ(λ2 − δ) T               in s(t) is no longer negligible and one should refer to the
    v2 = k2 [1,          ,        ,              ,         ]            original nonlinear compartmental models (27) and (45). In
                   αi      λ2 + γe αi (λ2 + γi )     αi λ2
                          T
    v3 = [0, 0, 0, 0, k3] , v4 = [0, 0, k4 , 0, 0] T                    this case, the observability rank test (51) can be checked for
    v5 = [0, 0, 0, k5 , 0]T                                             the matrix pair (A(t), C), where the matrix C is similar
                                                             (50)       to the linearized case in (29) and A(t) is the Jacobian
where k1 , k2 , k3 , k4 and k5 are arbitrary constants. The             of the nonlinear model (28), with respect to the entries of
first three eigenvalues are identical to Model I. Therefore, the        the reduced state-vector x(t) = [e(t), i(t), r(t), p(t)]T . The
outbreak properties such as exposure/infection rates, stability         entries of the Jacobian have been listed in Appendix A; some
conditions and reproduction number are exactly the same as              of which are time-dependent. Due to the non-evident form of
the first model, as derived in (40), (41), and (42).                    the observability matrix of this case, the proof of observability
                                                                        of the matrix pair (A(t), C) in its general case is cumbersome.
                                                                        However, it is simple to check this property numerically for
V. E PIDEMIC TREND ESTIMATION , MODEL OBSERVABILITY                     arbitrary values of the model parameters. We have tested this
                          AND CONTROL
                                                                        property for our later shown simulated results, as part of the
   The ability to estimate the future trend of the epidemic             source codes provided online at [7]. Therefore, we can state the
pattern is extremely important from the strategic perspective.          following result in both the general and linear approximated
This requires the accurate estimation of the compartmental              case:
model variables from reported statistics of the virus spread.
                                                                              Result 7. Although the number of exposed cases
The trend estimation requirements are addressed in the sequel
                                                                              of the population is not directly measurable, if the
for both the linearized and general form of both of the
                                                                              model parameters are known (or accurately esti-
proposed models. As noted before, these results can be used
                                                                              mated), the number of exposed cases can also be
to design an estimation scheme, based on for example a
                                                                              estimated from the other observations.
Kalman filter, for estimation and prediction of the current
and future trends, in presence of inaccurate infection tolls.
Note that although the variable e(t) is not directly measurable         C. Epidemic control and model controllability
from the available public data, one may seek whether of                    The proposed Models I and II, do not have external inputs.
not this variable can be indirectly estimated from the other            Therefore, without changing the model parameters, there is no
measurements (assuming that the other model parameters are              control mechanism for the epidemic and one may only verify
known).                                                                 the conditions under which the system is internally stable,
                                                                        i.e., the effect of epidemic outbreaks would vanish, remain
A. Observability during outbreak (low fraction of infection)            bounded, or result in an exponential outbreak. However, in-
                                                                        terventions such as social distancing, quarantine, medication,
   During the epidemic outbreak (in the low fraction of infec-          vaccination, etc., can be considered as control inputs that
tion case), the linearized versions of Model I and Model II,            change the model parameters.
namely (34) and (47) hold, respectively. Using the notion of
observability from system theory [26], [27], for the model
                                                                          VI. M ODEL PARAMETER IDENTIFICATION IN FIXED AND
matrix pair (A, C) the observability matrix is defined as
                                                                                         SOCIALLY CONFINED SCENARIOS
follows:                              
                                 Ck                                       An important step in making the proposed model useful
                              Ck Ak                                   in practice is to fit its parameters on real data. As noted
                      Ok =                               (51)
                                      
                                   ..  
                                   .                                     8 Matlab has a function called obsv for calculating the observability matrix,

                                  Ck Akn−1                              from the matrix pair (A, C).
~~~

## Page 13

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                         13



before, the general compartmental model in (5) depends on               presumed dynamics and to estimate them at the same time
the parameter vector θ(t), which is generally time dependent            or in parallel with the original state vector. For this, let
(relies on social contact, hygiene, etc.). In order to fit the model    us assume that all the parameters of our base epidemic
parameters various methods are available in the literature. We          model (27) are time-variant, resulting in the parameter vector
study two approaches, which can be applied to our problem               θ(t) = [αi (t), αe (t), κ(t), β(t), ρ(t), µ(t), γ(t)]T , that should
of interest.                                                            be estimated from real-world epidemic data. From the mod-
                                                                        eling perspective, this vector can have some deterministic or
A. Constrained least squares parameter estimation                       stochastic fluctuations. For example, let us assume that the
                                                                        model parameters are a simple Wiener process (Brownian mo-
   A general formulation for parameter identification is to             tion) plus deterministic inputs to model social interventions:
use constrained weighted least squares (CWLS) estimation.
This approach becomes equivalent to the maximum likelihood                   dαi (t)                       dαe (t)
estimate, if the measurement noises belong to specific families                      = uαi (t) + wi (t)            = uαe (t) + we (t)
                                                                               dt                            dt
of probability distributions (such as the Gaussian distribution).            dκ(t)                         dβ(t)
                                                                                    = uκ (t) + wκ (t)             = uβ (t) + wβ (t)
Nevertheless, the CWLS is more generic as it only attempts                    dt                            dt
in finding the parameter vector that minimizes a quadratic                   dρ(t)                         dµ(t)
                                                                                    = uρ (t) + wρ (t)             = uµ (t) + wµ (t)
error cost function between the model and measurements                        dt                            dt
                                                                             dγ(t)
(without any probabilistic priors on the origin of the model                        = uγ (t) + wγ (t)
                                                                              dt
or measurement noises). We can specifically refer to the                                                                               (54)
CWLS formulation proposed in [28] and other prior research,             where w(t) = [wi (t), we (t), wκ (t), wβ (t), wρ (t), wµ (t), wγ (t)]T
which have been specifically developed for nonlinear dynamic            is zero-mean white noise acting as process noise, and
models. Accordingly, for the general dynamic model (5), if we           uαi (t) and uαe (t) are the deterministic inputs due to social
define the modeling error function                                      intervention that change the level of social contact (considered
                         ∆                                              for modeling the effect of social distancing and quarantine).
                 e(t) = y(t) − g(x(t); θ(t), t),                (52)    For example, the effect of lockdown applied at time t = t0
assuming temporarily that the model parameters θ(t) = θ                 can be modeled by combinations of functions of the form:
are fixed, the problem of parameter identification can be                             uαi (t) = ai − bi e−ci (t−t0 ) u(t − t0 )
formulated as follows:                                                                                                                  (55)
                                                                                      uαe (t) = ae − be e−ce (t−t0 ) u(t − t0 )
                                            T
            θ̂ = argmin tr E[e(t)We(t) ]
                     θ                                                  where ci and ce define the speed of lockdown application,
            subject to:                                         (53)    and ai , bi , ae and be define the range of lockdown effect. The
            θmin ≤ θ ≤ θmax ,                                           effect of lockdown termination can be modeled in a similar
            ẋ(t) = f (x(t), w(t); θ, t),   x(0) = x0                   manner. In any case, as detailed in Appendix A, the above
                                                                        dynamics can be state augmented with the compartmental
Where E(·) denotes averaging over time, tr(·) denotes matrix
                                                                        model dynamics in (27) and (29) to form an augmented model,
trace, θmin and θmax define the lower and upper bounds of
                                                                        which can be tracked using an extended Kalman filter (EKF).
the model parameters dictated by physical constraints, and W
                                                                        The implementation of an EKF requires the Jacobian matrix
is the inverse of the covariance matrix of the measurement
                                                                        of the state augmented model with respect to all the elements
noise vector v(t) (if available; otherwise can be set to identity                                             ∆
for an unweighted version). This problem is in the form                 of the augmented state vector x̃(t) = [x(t); θ(t)] (where ; de-
of nonlinear CWLS for which a variety of stable numerical               notes column-wise stacking), as detailed in the appendix. The
solvers exist. Refer to [28] for a survey of methods and [29,           details of the EKF is beyond the scope of the current study,
Ch. 5] for methods specific to dynamic systems. In (53), since          which is focused on the modeling aspects of the problem.
the temporal averaging is performed over all time samples,              Nevertheless, the algorithmic steps of the discretized version
the procedure is only applicable to offline model fitting. Now          of the compartmental model are presented in Appendix B.
if θ(t) is time variant, an adaptive version of the above               An implementation of the EKF for epidemic model parameter
algorithm can be used, by averaging the error cost function             and state vector tracking will be provided online in the Git
over t0 ≤ τ ≤ t, resulting in a sample-wise updates of the              repository of the project [7]. The interested reader is referred
parameter vector. In the following subsection, we propose an            to classical textbooks for the required signal processing and
alternative approach for the time variant case, which is more           algorithmic details of the EKF and its extensions [30, Ch. 5
flexible, does not require nonlinear least-squares solvers, and         and 6], [17], [31, P. 191], [32, Appendix 9.A and 9.B].
simultaneously estimates the model state variables.                        Note that a great advantage of using the EKF for estimat-
                                                                        ing the model states and parameters is that in addition to
                                                                        estimating the values, it also provides confidence intervals
B. An extended Kalman filter for joint parameter and variable           for the estimates (which is an advantage of all Bayesian
estimation                                                              inference/estimation methods). In other words, under the given
  A well-known method for adaptive estimation of dynamic                assumptions on the process and measurement noise statistics,
system parameters is to consider the (possibly) time-varying            one can for example determine how accurate the number
parameters of the model as additional state variables with              of infected and exposed cases have been estimated. In the
~~~

## Page 14

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                                                                      14



context of interest, such confidence intervals permit healthcare
                                                                                                                       1
strategists to have an idea about the accuracy of the estimated
values and appropriate timing for lockdown and quarantine                                                             0.8                                                                 S(t)




                                                                                                   Population Ratio
management.                                                                                                                                                                               E(t)
                                                                                                                      0.6                                                                 I(t)
                                                                                                                                                                                          R(t)
                                  VII. S IMULATED RESULTS                                                                                                                                 P(t)
                                                                                                                      0.4
   We have carried-out several simulations with different sets
of parameters, resulting in the different scenarios explained in
                                                                                                                      0.2
previous sections.
Example 4 (Life-time immune case). The first scenario is                                                               0
                                                                                                                            0                 50                     100                         150
illustrated in Fig. 7, where we have considered a single virus                                                                                         days
outbreak in a 84 million population, with constant parameters                                                                                 (a) in five months
αe = 0.65, αi = 0.005, κ = 0.05, ρ = 0.08, β = 0.1, µ =
0.02 and γ = 0, simulated over one year. The assumption γ =
                                                                                                                      1
0 implies that the disease has been assumed to develop lifetime                                                                                S(t)    E(t)       I(t)      R(t)          P(t)
immunity, therefore there is no return from the recovered to                                                  0.8




                                                                                           Population Ratio
the susceptible compartment. In Fig. 7, we can observe the
constant ratio between i(t) and e(t) during the exponential                                                   0.6
outbreak (when i(t) ≪ s(t) and before reaching the nonlinear
phase of the model), which approves the relationship derived                                                  0.4
in (44).
                                                                                                              0.2
Example 5 (Recurrent epidemic). The second scenario is
illustrated in Fig. 8. All the model parameters are identical                                                         0
                                                                                                                          0            1000           2000               3000               4000
to Example 4, except for the re-susceptibility rate (loss of                                                                                          days
immunity) that is now γ = 0.001. It is interesting to see that
                                                                                                                                               (b) in ten years
in this scenario, the model has recurrent decaying peaks over
time, similar to the aforementioned 1918 Spanish flu.
                                                                                                         0.05
                                                                                                                                                                                          I(t)
Example 6 (Short lockdown period). The next scenario is                                                                                                                                   E(t)
illustrated in Fig. 9. This scenario corresponds to the case                                             0.04
                                                                                      Population ratio




where a one month lockdown is applied by the government
                                                                                                         0.03
to identify the exposed and infected cases. The parameters
of the model before quarantine are αe = 0.6, αi = 0.005,                                                 0.02
κ = 0.05, ρ = 0.08, β = 0.1, µ = 0.02 and γ = 0.001. In the
30th day after the initial outbreak, the one month lockdown is                                           0.01

applied, during which αe and αi are reduced to 0.1 and 0.001,
                                                                                                                      0
respectively, while keeping the other parameters unchanged.                                                                     500   1000    1500    2000    2500       3000      3500      4000
After one month, αi remains 0.001 (people keep distance with                                                                                          days

the infected ones), but αe is increased to 0.4 (much more                                                                              (c) I(t) and E(t) in ten years
than the quarantine period, but two-third of the original social
                                                                                    Fig. 8. Scenario B: Simulation of the fatal SEIR model with parameters αe
                                                                                    = 0.65, αi = 0.005, κ = 0.05, ρ = 0.08, β = 0.1, µ = 0.02, γ = 0.001, in (a)
                                                                                    five months and (b, c) ten years
                    1


                   0.8                        I(t)/E(t)                S(t)
Population Ratio




                                    0.2                                E(t)
                                                                       I(t)
                   0.6                                                 R(t)
                                    0.1                                P(t)
                   0.4
                                     0
                   0.2                    0      20         40
                                                                                    contact factor). We can see that with this scenario, which
                    0
                                                                                    corresponds to an insufficient quarantine period, the population
                         0   50       100     150         200    250          300   of the infected and exposed peaks have decreased; but the
                                              days                                  quarantine does not significantly change the mortality toll after
                                                                                    five months. But why? Because, after the quarantine period,
Fig. 7. Scenario A: Simulation of the fatal SEIR model with parameters
αe = 0.65, αi = 0.005, κ = 0.05, ρ = 0.08, β = 0.1, µ = 0.02                        there is still a minor fraction of the population that is exposed,
and γ = 0, over 10 months. Notice the constant i(t)/e(t) ratio during the           and this very small seed can re-initiate the virus spread. We
exponential outbreak, which is approximately equal to αi λ̃−1
                                                           1 = 0.078.               therefore come to the following result:
~~~

## Page 15

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                                                                            15



          Result 8. Imposing quarantines is effective in de-                                   and tracking, due to the smoothness and differentiability of the
          laying and reducing the infection population peaks;                                  hyperbolic tangent function.
          but is insufficient in the long term. Social distancing                                A simulation of this scenario is illustrated in Fig. 10. The
          and other measures should remain for a long period                                   parameters of the model are αe = 0.6, αi = 0.005, κ = 0.05,
          after the initial quarantine, to make the number of                                  ρ = 0.08, and γ = 0.001. The healthcare system breakdown
          contaminated subjects equal to “zero.”                                               parameters are β0 = 0.1, µ0 = 0.02, βs = 0.01, µs = 0.2,
                                                                                               σ = 1, i0 = 0.1 (although in reality, the healthcare system is
                                                                                               expected to reach its breakpoint far below this infection rate).
                                                                                               We can observe how the death rate significantly increases as
                               0.5                                                             the system reaches its break-point.
                                                                              I1(t)
                               0.4                                            E1(t)                                              0.15
            Population ratio




                                                                                                    Population ratio
                                                                              I2(t)                                                                                                            i1(t)
                                                       Quarantine             E2(t)                                                                                                            i2(t)
                               0.3       Quarantine
                                                            ends                                                                             0.1
                                             starts
                                                                                                                                                                                 Healthcare system
                               0.2                                                                                               0.05                                      breakdown infection level


                               0.1                                                                                                             0
                                                                                                                                               1




                                                                                                         Population ratio Population ratio
                                0                                                                                                                      r1(t)
                                     0                50            100           150                                                                  r2(t)
    Population ratio




                                                                                                                                             0.5
                       0.05

                                                                              P1(t)                                                            0
                                                                              P2(t)
                                0                                                                                                            0.2       p1(t)
                                     0                50            100           150                                                                  p2(t)
                                                             days                                                                            0.1

Fig. 9. Scenario C: Simulation of the fatal SEIR model with a quarantine                                                                      0
period between day 30 and 60. E1(t), I1(t) and P 1(t) correspond to the                                                                            0           50          100                         150
case without quarantine and E2(t), I2(t) and P 2(t) correspond to the case                                                                                          days
with quarantine. Refer to the text for further details and the switching of the
parameters.                                                                                    Fig. 10. Scenario D: Simulation of the fatal SEIR model when the healthcare
                                                                                               system reaches its breakdown point at i(t) = 0.1. The curves i1(t), r1(t),
                                                                                               and p1(t) are the non-saturated cases and i2(t), r2(t), and p2(t) correspond
Example 7 (Healthcare system saturation). Our next scenario                                    to the saturated cases.
corresponds to the case where the healthcare system reaches
its maximum capacity or break-point, due to limited test                                         Based on the simulations of this section, we can propose a
kits, medication, hospitalization, excessive fatigue or mortality                              protocol that can be effective in practice:
of the healthcare personnel, economic breakdowns, etc. This
phenomenon is the worst feared case for pandemic strategists                                   Algorithm 1 Proposed protocol for effective epidemic disease
and it can be modeled at various levels. Suppose that we                                       control
model it in its simplest form and assume that the recovery                                      1: Apply maximum lockdown of the entire population and
and mortality rates of the model change as functions of the                                        quarantine of the infected cases, as soon as possible.
number of infected cases:                                                                       2: Estimate the number of exposed subjects and the level of
                                                                                                   confidence of the estimate.
                                              β(t) = (βs − β0 )h(i(t)) + β0                     3: Keep the maximal lockdown until as many of all the
                                                                                        (56)
                                              µ(t) = (µs − µ0 )h(i(t)) + µ0                        number of estimated exposed subjects are identified at a
where β0 and µ0 are the recovery and mortality rate parameters                                     very high level of confidence.
before healthcare system saturation, βs (βs ≪ β0 ) and µs                                       4: Switch from lockdown to strict social distancing and
(µs ≫ µ0 ) are the recovery and mortality rates after saturation,                                  personal hygiene protocols.
and h(i(t)) is a saturation function such that h(0) ≈ 0 and                                     5: Switch to normal life only when no new cases have been
h(∞) ≈ 1. For example, the hyperbolic tangent with a slope                                         reported for a long period.
parameter σ is a reasonable and common choice for modeling
such phenomena:
                                                                                                         VIII. C ONCLUSION AND F UTURE W ORK
                                                     1            i − i0
                                               h(i) = [1 + tanh (        )]             (57)     In this study we considered some of the properties of
                                                     2              σ                          epidemic diseases from a mathematical and signal processing
where i0 is the infection break-point of the healthcare system.                                perspective, by using a compartmental model for the propa-
The above choice is also beneficial for parameter optimization                                 gation of the epidemic disease. It was shown that the model
~~~

## Page 16

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                   16



is not stable around its fixed-point (the no-infection case). We        with the following non-zero entries (we have dropped the time
should indeed be proactively worried about the instability of           index of all variables and parameters for better readability):
our societies to such epidemic outbreaks; since a fatal virus
with an initial seed as small as a single subject worldwide can           A1,1 = αe [1 − 2e − i − r − p] − αi i − κ − ρ
trigger the avalanche of pandemic waves, killing many people              A1,2 = αi [1 − e − 2i − r − p] − αe e
worldwide, as the COVID-19 Coronavirus has shown. Note                    A1,3 = −[αe e + αi i] A1,4 = −[αe e + αi i]
however that from the modeling and dynamics perspective,                  A1,5 = i[1 − e − i − r − p] A1,6 = e[1 − e − i − r − p]
there is nothing specific to the Coronavirus, apart from its              A1,7 = −e A1,9 = −e
specific parameters. In fact, humans have always been living in           A2,1 = κ A2,2 = −β − µ
such a metastable condition and researchers from all domains              A2,7 = e A2,8 = −i A2,10 = −i
need to synergize to think a way through this condition.                  A3,1 = ρ A3,2 = β A3,3 = −γ
                                                                          A3,8 = i A3,9 = e A3,11 = −r
   The research will be continued and extended from var-                  A4,2 = µ A4,10 = i
ious aspects in the future versions. Specifically, by fitting                                                                 (61)
the model over real data, the prediction of infection and
mortality rates under quarantine and vaccination, and the study
of the recurrent pattern of the epidemic disease over time.             B. The extended Kalman filter algorithm
Non-exponential law infection distributions have also been                  Official epidemic data are commonly reported on a daily or
considered in the literature [14]. This can be an interesting           weekly bases. Therefore, the measurements used for model
track of research for the study of epidemic diseases, including         variable and parameter estimation are discrete time, while
the family of Coronaviruses.                                            the compartmental model proposed throughout this work is
                                                                        continuous. As a result two approaches are available for
                                                                        implementing an EKF: 1) to use continuous-discrete Kalman
                                                                        filters, which mix continuous state equations with discrete
                            A PPENDIX                                   measurement equations, or 2) to discretize the dynamic model
                                                                        of the system and to implement a discrete EKF. The formula-
A. Compartmental Model Jacobians                                        tion for the latter approach is detailed in Algorithm 2.

   Following (28) and the Wiener process model for the model            Algorithm 2 An extended Kalman filter for simultaneous
parameters presented in (54), the most general form of the              compartment variable and model parameter tracking
proposed compartmental model with time-varying parameters               Input: Noisy measurements (regular reports) of the
is as follows                                                              epidemic spread yk
                                                                        Input: Initial conditions: Q, R, x̂+    +
                                                                                                           0 , P0
                                                                                   +
  de(t)                                                                 Output: x̂k (vector of state and model parameter estimates)
         = [1 − e(t) − i(t) − r(t) − p(t)][αe (t)e(t) + αi (t)i(t)]
   dt
            −κ(t)e(t) − ρ(t)e(t)                                          1: for k = 0 · · · T do
  di(t)                                                                   2:  State prediction:
        = κ(t)e(t) − β(t)i(t) − µ(t)i(t)                                      x̂−           +        +
   dt                                                                     3:    k+1 = f (x̂k , w̄; θ̂k , k∆)
  dr(t)                                                                          −        + + +T
         = β(t)i(t) + ρ(t)e(t) − γ(t)r(t)                                4:   Pk+1 = Ak Pk Ak + Q
   dt                                                                         Measurement update:
  dp(t)                                                                       Kk = P−       −T     − − −T
         = µ(t)i(t)                                                      5:             k Ck [Ck Pk Ck       + R]−1
    dt                                                                   6:
                                                                                −         −   −
                                                                              ŷk = g(x̂k ; θ̂k , k∆)
  dαi (t)    dui                  dαe (t)    due
          =      (t) + wi (t)             =      (t) + we (t)            7:   ik = yk − ŷk−
    dt        dt                    dt        dt
  dκ(t)                dβ(t)                dρ(t)                        8:   σ̂k+ = σ̂k− + Kk ik
         = wκ (t)             = wβ (t)             = wρ (t)                   P+                 −     −
    dt                   dt                   dt                         9:      k = [I − Kk Ck ]Pk
  dµ(t)                dγ(t)                                            10:   Check and enforce variable and parameter ranges
          = wµ (t)            = wγ (t)
    dt                   dt                                                   using hard-constraints
                                                             (58)
                                                                        11:   Performance monitoring
If we define the variable and parameter augmented state vector:
                                                                        12: end for

          ∆
    x(t) = [e(t), i(t), r(t), p(t),                             (59)
           αi (t), αe (t), κ(t), β(t), ρ(t), µ(t), γ(t)]T
                                                                                               ACKNOWLEDGMENT

which can be written in the compact state-space form (5). The              This article has been drafted in March 2020, in the midst
Jacobian of this form is defined                                        of the COVID-19 Coronavirus outbreak. The author would
                                                                        like to sincerely thank Professor Christian Jutten, Emeritus
                                                                        Professor of Université Grenoble Alpes, Grenoble, France, for
                           ∆ ∂f (·)
                    A(t) =            ∈ R11×11                  (60)    his insightful and motivating comments throughout this study.
                               ∂x
~~~

## Page 17

~~~text
DRAFT VERSION, SUBJECT TO MODIFICATION. FOLLOW THE UPDATES FROM: https://arxiv.org/abs/2003.11371                                                         17



                              R EFERENCES                                        [28] A. Gábor and J. R. Banga, “Robust and efficient parameter estimation
                                                                                      in dynamic models of biological systems,” BMC systems biology, vol. 9,
 [1] O. Diekmann, H. Heesterbeek, and T. Britton, Mathematical tools for              no. 1, p. 74, 2015.
     understanding infectious disease dynamics. Princeton University Press,      [29] D. P. Moeller, Mathematical and computational modeling and simula-
     2012, vol. 7.                                                                    tion. Springer, 2003.
 [2] F. Brauer, C. Castillo-Chavez, and C. Castillo-Chavez, Mathematical         [30] S. Haykin, Ed., Kalman Filtering and Neural Networks. John Wiley
     models in population biology and epidemiology. Springer, 2012, vol. 2.           & Sons Inc., 2001.
                                                                                 [31] A. Gelb, Ed., Applied Optimal Estimation. MIT Press, 1974.
 [3] J. Haefner, Modeling Biological Systems: Principles and Applications.
                                                                                 [32] A. Jazwinski, Stochastic Processes and Filtering Theory, ser. Mathemat-
     Springer, 2005.
                                                                                      ics in Science and Engineering. Elsevier Science, 1970.
 [4] G. de Vries, T. Hillen, M. Lewis, B. Schõnfisch, and J. Muller, A Course
     in Mathematical Biology: Quantitative Modeling with Mathematical and
     Computational Methods, ser. Monographs on Mathematical Modeling
     and Computation. Society for Industrial and Applied Mathematics,
     2006.
 [5] W. Yang, A. Karspeck, and J. Shaman, “Comparison of filtering methods
     for the modeling and retrospective forecasting of influenza epidemics,”
     PLoS computational biology, vol. 10, no. 4, 2014.
 [6] A. Azar, Control Applications for Biomedical Engineering Systems.
     Elsevier Science, 2020.
 [7] R. Sameni, Mathematical Modeling of Epidemic Diseases, 2020.
     [Online]. Available: https://github.com/rsameni/EpidemicModeling.git
 [8] J. Ottesen, M. Olufsen, and J. Larsen, Applied Mathematical Models
     in Human Physiology, ser. Monographs on Mathematical Modeling and
     Computation. Society for Industrial and Applied Mathematics, 2004.
 [9] K. P. Burnham and D. R. Anderson, “Multimodel inference: understand-
     ing aic and bic in model selection,” Sociological methods & research,
     vol. 33, no. 2, pp. 261–304, 2004.
[10] F. De Ridder, R. Pintelon, J. Schoukens, and D. P. Gillikin, “Modified
     aic and mdl model selection criteria for short data records,” IEEE
     Transactions on Instrumentation and Measurement, vol. 54, no. 1, pp.
     144–150, 2005.
[11] T. Britton, “Stochastic epidemic models: a survey,” Mathematical bio-
     sciences, vol. 225, no. 1, pp. 24–35, 2010.
[12] L. Pellis, F. Ball, and P. Trapman, “Reproduction numbers for epidemic
     models with households and other social structures. I. Definition and
     calculation of R0,” Mathematical biosciences, vol. 235, no. 1, pp. 85–
     97, 2012.
[13] J. C. Miller, “Distribution of outbreak sizes for sir disease in finite
     populations,” arXiv preprint arXiv:1907.05138, 2019.
[14] Z. Feng, D. Xu, and H. Zhao, “Epidemiological models with non-
     exponentially distributed disease stages and applications to disease
     control,” Bulletin of mathematical biology, vol. 69, no. 5, pp. 1511–
     1536, 2007.
[15] V. C. Rideout, Mathematical and Computer Modeling of Physiological
     Systems. Prentice Hall, 1991.
[16] B. Ingalls, An Introduction to Mathematical Modelling in Molecular
     Systems Biology. Department of Applied Mathematics, University of
     Waterloo, 2012.
[17] M. S. Grewal and A. P. Andrews, Kalman Filtering: Theory and Practice
     Using Matlab, 2nd ed. John Wiley & Sons, Inc., 2001.
[18] R. M. Anderson and R. M. May, “Population biology of infectious
     diseases: Part i,” Nature, vol. 280, no. 5721, pp. 361–367, 1979.
[19] R. M. May and R. M. Anderson, “Population biology of infectious
     diseases: Part ii,” Nature, vol. 280, no. 5722, pp. 455–461, 1979.
[20] H. W. Hethcote, “The mathematics of infectious diseases,” SIAM review,
     vol. 42, no. 4, pp. 599–653, 2000.
[21] K. Dietz, “Transmission and control of arbovirus diseases,” Epidemiol-
     ogy, vol. 104, pp. 104–121, 1975.
[22] J. C. Kamgang and G. Sallet, “Computation of threshold conditions
     for epidemiological models and global stability of the disease-free
     equilibrium (dfe),” Mathematical biosciences, vol. 213, no. 1, pp. 1–
     12, 2008.
[23] P. Van den Driessche and J. Watmough, “Reproduction numbers and
     sub-threshold endemic equilibria for compartmental models of disease
     transmission,” Mathematical biosciences, vol. 180, no. 1-2, pp. 29–48,
     2002.
[24] Z. Feng, “Final and peak epidemic sizes for seir models with quarantine
     and isolation,” Mathematical Biosciences & Engineering, vol. 4, no. 4,
     p. 675, 2007.
[25] S. Gonçalves, G. Abramson, and M. F. Gomes, “Oscillations in sirs
     model with distributed delays,” The European Physical Journal B,
     vol. 81, no. 3, p. 363, 2011.
[26] T. Kailath, Linear Systems. Prentice Hall, 1980.
[27] W. J. Terrell, Stability and stabilization: an introduction. Princeton
     University Press, 2009.
~~~
