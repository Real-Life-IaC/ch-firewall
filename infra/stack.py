import aws_cdk as cdk

from constructs import Construct
from infra.constructs.b2.firewall import B2CloudfrontFirewall


class FirewallStack(cdk.Stack):
    """Stack for firewall resources"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        B2CloudfrontFirewall(
            scope=self,
            id="CloudFrontFirewall",
        )

        # Add tags to everything in this stack
        cdk.Tags.of(self).add(key="owner", value="Platform")
        cdk.Tags.of(self).add(key="repo", value="ch-firewall")
        cdk.Tags.of(self).add(key="stack", value=self.stack_name)
