import aws_cdk as cdk

from constructs_package.constants import AwsAccountId
from constructs_package.constants import AwsRegion
from constructs_package.constants import AwsStage
from infra.stack import FirewallStack


app = cdk.App()

# We only need Firewall in production. All other envs are in a private subnet.
FirewallStack(
    scope=app,
    id=f"Firewall-{AwsStage.PRODUCTION}",
    env=cdk.Environment(account=AwsAccountId.PRODUCTION, region=AwsRegion.US_EAST_1),
)

app.synth()
