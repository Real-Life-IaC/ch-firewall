import aws_cdk as cdk

from constructs import Construct
from constructs_package.constants import AwsStage
from infra.constructs.b2.access_logs import B2AccessLogs
from infra.constructs.b2.alarms import B2Alarms
from infra.constructs.b2.cloudtrail import B2Cloudtrail
from infra.constructs.b2.dns import B2PrivateHostedZones
from infra.constructs.b2.dns import B2PublicHostedZones
from infra.constructs.b2.email import B2EmailServices
from infra.constructs.b2.firewall import B2CloudfrontFirewall
from infra.constructs.b2.github_oidc import B2GithubOidc
from infra.constructs.b2.network import B2Network


class PlatformStack(cdk.Stack):
    """Create the AWS foundational resources"""

    def __init__(
        self,
        scope: Construct,
        id: str,
        stage: AwsStage,
        cidr_block: str,
        max_azs: int,
        nat_gateways: int,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        B2GithubOidc(
            scope=self,
            id="GithubOidc",
            stage=stage,
        )

        B2Cloudtrail(
            scope=self,
            id="CloudTrail",
        )

        B2Network(
            scope=self,
            id="Network",
            cidr_block=cidr_block,
            max_azs=max_azs,
            nat_gateways=nat_gateways,
        )

        B2AccessLogs(
            scope=self,
            id="AccessLogs",
        )

        B2Alarms(
            scope=self,
            id="Alarms",
            stage=stage,
        )

        # Add tags to everything in this stack
        cdk.Tags.of(self).add(key="owner", value="Platform")
        cdk.Tags.of(self).add(key="repo", value="ch-platform-repo")
        cdk.Tags.of(self).add(key="stack", value=self.stack_name)
