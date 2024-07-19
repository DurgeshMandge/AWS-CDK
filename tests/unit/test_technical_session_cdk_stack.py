import aws_cdk as core
import aws_cdk.assertions as assertions

from technical_session_cdk.technical_session_cdk_stack import TechnicalSessionCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in technical_session_cdk/technical_session_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TechnicalSessionCdkStack(app, "technical-session-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
