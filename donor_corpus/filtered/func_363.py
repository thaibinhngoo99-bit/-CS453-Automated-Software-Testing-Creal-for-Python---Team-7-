def plot_polynomial_regression():
    rng = np.random.RandomState(0)
    x = 2 * rng.rand(100) - 1
    f = lambda t: 1.2 * t ** 2 + 0.1 * t ** 3 - 0.4 * t ** 5 - 0.5 * t ** 9
    y = f(x) + 0.4 * rng.normal(size=100)
    x_test = np.linspace(-1, 1, 100)
    pl.figure()
    pl.scatter(x, y, s=4)
    X = np.array([x ** i for i in range(5)]).T
    X_test = np.array([x_test ** i for i in range(5)]).T
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    pl.plot(x_test, regr.predict(X_test), label='4th order')
    X = np.array([x ** i for i in range(10)]).T
    X_test = np.array([x_test ** i for i in range(10)]).T
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    pl.plot(x_test, regr.predict(X_test), label='9th order')
    pl.legend(loc='best')
    pl.axis('tight')
    pl.title('Fitting a 4th and a 9th order polynomial')
    pl.figure()
    pl.scatter(x, y, s=4)
    pl.plot(x_test, f(x_test), label='truth')
    pl.axis('tight')
    pl.title('Ground truth (9th order polynomial)')