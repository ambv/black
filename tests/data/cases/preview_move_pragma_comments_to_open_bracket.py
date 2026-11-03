# flags: --preview

# Issue #2843: Pragma comments on wrapped statements should move to opening bracket
asdf = namedtuple("nameoftuplegoeshere", "fieldsgohere andnoather andanother morehere")  # pylint: disable=invalid-name

# noqa directive with and without code
call_noqa_code(argument_number_one_goes_here, argument_number_two_goes_here)  # noqa: E501
call_noqa_bare(arg_one_goes_here_and_it_is_long, arg_two_goes_here_and_it_is_long)  # noqa

# pyright directive
asm_client: SecretsManagerClient = boto3.client("secretsmanager_very_long_service_name_here")  # pyright: ignore[reportUnknownMemberType]

# ruff directive
call_ruff(arg_one_goes_here_and_it_is_long, arg_two_goes_here_and_it_is_long)  # ruff: noqa

# coverage pragma
call_pragma(argument_number_one_goes_here, argument_number_two_goes_here)  # pragma: no cover

# Nested call in argument / lambda
check_call(
    program,
    lambda: lib._some_private_module(param1, param2, to_make_it_long),  # pylint: disable=protected-access
    arg2,
)

# Import statement
from module import very_long_name_that_is_so_long_it_forces_a_split, another_long_name  # noqa: F401

# Function definition
def my_func(arg1_that_is_very_long, arg2_that_is_very_long, arg3_that_is_very_long):  # pylint: disable=too-many-arguments
    pass

# Narrative / non-pragma comments should NOT move to opening bracket
asdf = namedtuple("nameoftuplegoeshere", "fieldsgohere andnoather andanother morehere")  # this is a normal comment

# Chained calls with tokens on tail should NOT move to opening bracket
result = some_long_call_expression(arg1, arg2, arg3, arg4, arg5, arg6).method()  # pylint: disable=no-member

# output

# Issue #2843: Pragma comments on wrapped statements should move to opening bracket
asdf = namedtuple(  # pylint: disable=invalid-name
    "nameoftuplegoeshere", "fieldsgohere andnoather andanother morehere"
)

# noqa directive with and without code
call_noqa_code(  # noqa: E501
    argument_number_one_goes_here, argument_number_two_goes_here
)
call_noqa_bare(  # noqa
    arg_one_goes_here_and_it_is_long, arg_two_goes_here_and_it_is_long
)

# pyright directive
asm_client: SecretsManagerClient = (
    boto3.client(  # pyright: ignore[reportUnknownMemberType]
        "secretsmanager_very_long_service_name_here"
    )
)

# ruff directive
call_ruff(  # ruff: noqa
    arg_one_goes_here_and_it_is_long, arg_two_goes_here_and_it_is_long
)

# coverage pragma
call_pragma(  # pragma: no cover
    argument_number_one_goes_here, argument_number_two_goes_here
)

# Nested call in argument / lambda
check_call(
    program,
    lambda: lib._some_private_module(  # pylint: disable=protected-access
        param1, param2, to_make_it_long
    ),
    arg2,
)

# Import statement
from module import (  # noqa: F401
    very_long_name_that_is_so_long_it_forces_a_split,
    another_long_name,
)


# Function definition
def my_func(  # pylint: disable=too-many-arguments
    arg1_that_is_very_long, arg2_that_is_very_long, arg3_that_is_very_long
):
    pass


# Narrative / non-pragma comments should NOT move to opening bracket
asdf = namedtuple(
    "nameoftuplegoeshere", "fieldsgohere andnoather andanother morehere"
)  # this is a normal comment

# Chained calls with tokens on tail should NOT move to opening bracket
result = some_long_call_expression(
    arg1, arg2, arg3, arg4, arg5, arg6
).method()  # pylint: disable=no-member
