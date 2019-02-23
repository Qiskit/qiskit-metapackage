.. _uncertainty-problems:

====================
Uncertainty Problems
====================

Uncertainty is present in most realistic applications, and often it is necessary to evaluate
the behavior of a system under uncertain data.
For instance, in finance, it is of interest to evaluate expected value or risk metrics of
financial products that depend on underlying stock prices, economic factors, or changing
interest rates. Classically, such problems are often evaluated using Monte Carlo simulation.
However, Monte Carlo simulation does not converge very fast, which implies that large numbers of
samples are required to achieve estimators of reasonable accuracy and confidence.
In quantum computing, *amplitude estimation* can be used instead, which can lead to a quadratic
speed-up. Thus, millions of classical samples could be replaced by a few thousand quantum samples.

*Amplitude estimation* is a derivative of *quantum phase estimation* applied to a particular
operator :math:`A`. :math:`A` is assumed to operate on (n+1) qubits (+ possible ancillas) where
the n qubits represent the uncertainty (random distribution :ref:`random_distribution`) and the
last qubit is used to represent the (normalized) objective value as its amplitude.
In other words, :math:`A` is constructed such that the probability of measuring a '1' in the
objective qubit is equal to the value of interest. An implementation of an uncertainty problem is
assumed to provide a dictionary with parameter, particularly containing the index of the qubit
used for the objective:

.. code:: python

    self._params = {
                ...
                'i_objective': i_objective
            }

Since the value of interest has to be normalized to lie in [0, 1], an uncertainty problem also
provides a function:

.. code:: python

    def value_to_estimator(self, value):
        return value

which is used to map the result of *amplitude estimation* to the range of interest.
The standard implementation is just the identity and can be overridden when needed.

In the following, we introduce the available implementations of this class.

--------------------
European Call Option
--------------------

.. topic:: Expected Value

    Suppose a European call option with strike price :math:`K` and an underlying asset whose spot price at maturity :math:`S_T`
    follows a given random distribution.
    The corresponding payoff function is defined as :math:`\max \{ S - K, 0 \}`.

    The *European call option - expected value* uncertainty problem takes the following input parameters:

    - univariate random distribution for spot price (:ref:`random_distribution`)
    - strike price :math:`K`
    - approximation scaling parameter :math:`c_{approx}` which specifies how well the objective function is approximated (needs to be synced with the number of evaluation qubits in amplitude estimation). For more details on the approximation, see https://arxiv.org/abs/1806.06893.

    .. code:: python

        # construct circuit factory for random distribution
        uncertainty_model = LogNormalDistribution(num_uncertainty_qubits, mu=mu, sigma=sigma, low=low, high=high)

        # set the strike price (should be within the low and the high value of the uncertainty)
        strike_price = 2

        # set the approximation scaling for the payoff function
        c_approx = 0.5

        # construct circuit factory for payoff function
        european_call = EuropeanCallExpectedValue(
            uncertainty_model,
            strike_price=strike_price,
            c_approx=c_approx
        )

.. topic:: Delta

    The $\Delta$, of an option is defines as the derivative of the expected payfoff (respectively the price) with respect to the spot price.
    For an European call option it can be defined as :math:`\Delta = P\left[ S_T \geq K \right]`.

    The *European call option - Delta* uncertainty problem takes the following input parameters:

    - univariate random distribution for spot price (:ref:`random_distribution`)
    - the strike price :math:`K`

    .. code:: python

        european_call_delta = EuropeanCallDelta(
            uncertainty_model,
            strike_price
        )

    Note that - in contrast to the expected value - the approximation scaling is not required here.

--------------------------
Fixed-Income Asset Pricing
--------------------------

.. topic:: Expected Value

    Here, we seek to price a fixed-income asset knowing the distributions describing the relevant interest rates.
    The cash flows :math:`c_t` of the asset and the dates at which they occur are known.
    The total value :math:`V` of the asset is thus the expectation value of:

    .. math::

        V = \sum_{t=1}^T \frac{c_t}{(1+r_t)^t}

    Each cash flow is treated as a zero coupon bond with a corresponding interest rate :math:`r_t` that depends on its maturity.
    The user must specify the distribution modelling the uncertainty in each :math:`r_t` (possibly correlated)
    as well as the number of qubits he wishes to use to sample each distribution.
    In this example we expand the value of the asset to first order in the interest rates :math:`r_t`.
    This corresponds to studying the asset in terms of its duration.

    The *Fixed-Income - Expected Value* uncertainty problem takes the following parameters:

    - multivariate random distribution: :math:`u`
    - affine map from the random distribution to interest rates (e.g. from a principal component analysis): :math:`A`, :math:`b`
    - cash flow: :math:`c`
    - approximation scaling parameter :math:`c_{approx}` which specifies how well the objective function is approximated (needs to be synced with the number of evaluation qubits in amplitude estimation). For more details on the approximation, see https://arxiv.org/abs/1806.06893.

    .. code:: python

        # construct corresponding distribution
        u = MultivariateNormalDistribution(num_qubits, low, high, mu, sigma)

        # can be used in case a principal component analysis has been done to derive the random distribution,
        # ignored in this example
        A = np.eye(2)
        b = np.zeros(2)

        # specify cash flow
        cf = [1.0, 2.0]

        # specify approximation factor
        c_approx = 0.5

        # get fixed income circuit appfactory
        fixed_income = FixedIncomeExpectedValue(u, A, b, cf, c_approx)
