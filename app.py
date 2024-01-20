import aws_cdk as cdk

from constructs_package.constants import AwsAccountId
from constructs_package.constants import AwsRegion
from constructs_package.constants import AwsStage
from infra.stack import PlatformStack


app = cdk.App()

PlatformStack(
    scope=app,
    id=f"Platform-{AwsStage.SANDBOX}",
    env=cdk.Environment(
        account=AwsAccountId.SANDBOX, region=AwsRegion.US_EAST_1
    ),
)

PlatformStack(
    scope=app,
    id=f"Platform-{AwsStage.STAGING}",
    env=cdk.Environment(
        account=AwsAccountId.STAGING, region=AwsRegion.US_EAST_1
    ),
)

PlatformStack(
    scope=app,
    id=f"Platform-{AwsStage.PRODUCTION}",
    env=cdk.Environment(
        account=AwsAccountId.PRODUCTION, region=AwsRegion.US_EAST_1
    ),
)

app.synth()
