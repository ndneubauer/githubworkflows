from aws_cdk import core as cdk
import aws_cdk.aws_ssm as ssm

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ssm.StringParameter(self, "Parameter",
                            allowed_pattern=".*",
                            description="The value Foo",
                            parameter_name="FooParameter",
                            string_value="Foo",
                            tier=ssm.ParameterTier.ADVANCED
                            )
