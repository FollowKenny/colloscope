from ortools.math_opt.python import mathopt


def main():
    # Build the model.
    model = mathopt.Model(name="getting_started_lp")
    x = model.add_variable(lb=-1.0, ub=1.5, name="x")
    y = model.add_variable(lb=0.0, ub=1.0, name="y")
    model.add_linear_constraint(x + y <= 1.5)
    model.maximize(x + 2 * y)


if __name__ == "__main__":
    main()
