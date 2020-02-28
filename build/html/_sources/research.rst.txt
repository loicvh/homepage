Research
========

Research Interests
~~~~~~~~~~~~~~~~~~

- Modeling and Simulation


Preprint
~~~~~~~~

- L. Van Hoorebeeck, P.-.A Absil and A. Papavasiliou,
  "**Global Solution of Economic Dispatch with Valve Point Effects and Transmission Constraints**,"
  2020 Power Systems Computation Conference (PSCC), Porto, Portugal, 2020. (Submitted,
  :download:`preprint <data/PSCC_2020.pdf>`,
  `code <https://gitlab.com/Loicvh/apla>`_)


Refereed conference papers
~~~~~~~~~~~~~~~~~~~~~~~~~~

- (2019) L. Van Hoorebeeck, P.-.A Absil and A. Papavasiliou,
  "**MILP-Based Algorithm for the Global Solution of Dynamic Economic Dispatch Problems with Valve-Point Effects**,"
  2019 IEEE Power & Energy Society General Meeting (PESGM), Atlanta, GA, USA, 2019, pp. 1-5. (:download:`preprint <data/PES_2019.pdf>`,
  `IEEE Xplore <https://ieeexplore.ieee.org/document/8973631>`_)

- (2019)  L. Van Hoorebeeck, J. Cavillot, H. Bui-Van, F. Glineur, C. Craeye and E. de Lera Acedo,
  "**Near-field calibration of SKA-Low stations using unmanned aerial vehicles**,"
  13th European Conference on Antennas and Propagation (EuCAP), Krakow, Poland, 2019, pp. 1-5. (:download:`preprint <data/PES_2019.pdf>`,
  `IEEE Xplore <https://ieeexplore.ieee.org/document/8739380>`__)


Thesis
~~~~~~

- "**Calibration of the SKA-low antenna array using drones**", Master Thesis, June 2018.
  (Advisers: C. Craeye and F. Glineur, `pdf <https://dial.uclouvain.be/memoire/ucl/fr/object/thesis%3A14813>`_)

Research Problems
~~~~~~~~~~~~~~~~~

I am currently interested in the **economic dispatch problem (EDP)**, this problem consists in the optimal allocation of the committed [#f1]_ generating units to meet the system load at lower cost. The objective function is the sum of each unit :math:`g \in G` fuel cost at each time step :math:`t \in T`. Mathematically it reads, 


.. math:: 
   :label: obj

    \min \sum_{t \in T} \sum_{g \in G} f_g (p_{gt}),

of course I need to specify the cost functions. In my case, I want to model a physical effect, *the valve point loading effect* (VPE) which naturally occurs in large gaz power plant such as combined cycle gas turbines (CCGT): when a turbine is loaded *at* a valve point, that is just before the next valve is opened, the production is optimal, but when a turbine is loaded *off* a valve point, that is just after the opening of the valve, then the throttling losses increase. This sudden changes in the objective raises computational challenges. Here we model this effect with the following objective function

.. math::
   :label: obj_VPE

   f_g (p_{gt}) = A_g p_{gt}^2 + B_g p_{gt} + C_g + D_g \left | \sin E_g (p_{gt} - p^{\min}_{gt}) \right |  .

This function is the sum of a smooth quadratic part and a nonsmooth and nonconvex rectified sine, and the devil lies in the later. Since the function is nonconvex, it is really difficult to prove the optimality of a point that we think is optimal and because of the nonsmoothness, we lose the vast amount of methods using first and second order information. Basically, the best algorithms and convergence theorems in optimization start with the sentence: 

.. pull-quote::
   Given a smooth convex function :math:`f`...

Basically, we will need some tricks to tackle this problem. This will be explained soon, but first let's look at the constraints.

.. rst-class:: center

.. image:: data/images/pg_0001.png
    :align: center  
    :alt: Illustration of the VPE.

Feasible Set
------------

.. image:: data/images/algo_gif.gif
    :align: center  
    :alt: Illustration of the VPE.

.. rubric:: Footnotes

.. [#f1] A *committed* generator is simply a generator which has been scheduled to produce power. Hence, we expect every generator to produce. This makes the EDP much simpler than its cousin, the *unit commitment*, which has to take every combination of committed unit into account.
