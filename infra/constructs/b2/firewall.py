from aws_cdk import aws_ssm as ssm
from constructs import Construct
from infra.constructs.l2 import waf


class B2CloudfrontFirewall(Construct):
    """Cloudfront Firewall"""

    def __init__(self, scope: Construct, id: str) -> None:
        super().__init__(scope, id)

        web_acl = waf.WebAcl(
            scope=self,
            id="WebAcl",
            metric_name="cloudfront",
            web_acl_scope=waf.WebAclScope.CLOUDFRONT,
            default_action=waf.WebAclAction.ALLOW,
            rules=[
                waf.WebAclCustomRule(
                    name="Throttle",
                    priority=0,
                    statement=waf.ThrottleStatement(rate_limit=2000),
                ),
                waf.WebAclAwsRule(
                    name=waf.AwsManagedRule.IP_REPUTATION_LIST,
                    priority=1,
                ),
                waf.WebAclAwsRule(
                    name=waf.AwsManagedRule.COMMON_RULE_SET,
                    priority=2,
                ),
                waf.WebAclAwsRule(
                    name=waf.AwsManagedRule.KNOWN_BAD_INPUTS_RULE_SET,
                    priority=3,
                ),
                waf.WebAclAwsRule(
                    name=waf.AwsManagedRule.SQLI_RULE_SET,
                    priority=4,
                ),
            ],
        )

        ssm.StringParameter(
            scope=self,
            id="WebAclArn",
            string_value=web_acl.web_acl_arn,
            description="Web Acl Arn for Cloudfront Waf with 2k rate limit",
            parameter_name="/firewall/cloudfront-web-acl/arn",
        )
