# flags: --preview
XpressDirect._addCols = lambda self, prob, objx, mstart, mrwind, dmatval, bdl, bdu, names, types: prob.addcols(objx, mstart, mrwind, dmatval, bdl, bdu, names, types)
result = lambda value: calculate(value, additional_positional_argument, another_positional_argument)

# output
XpressDirect._addCols = (
    lambda self, prob, objx, mstart, mrwind, dmatval, bdl, bdu, names, types: (
        prob.addcols(objx, mstart, mrwind, dmatval, bdl, bdu, names, types)
    )
)
result = lambda value: calculate(
    value, additional_positional_argument, another_positional_argument
)
