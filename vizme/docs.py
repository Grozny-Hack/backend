from blacksheep.server.openapi.common import ContentInfo, EndpointDocs, ResponseInfo
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

# TODO: JWT auth handler

# class MyOpenAPIHandler(OpenAPIHandler):
#     def on_docs_generated(self, docs: OpenAPI) -> None:
#         docs.security = Security([SecurityRequirement("basic", [])])
#         assert docs.components is not None
#         docs.components.security_schemes = {"basic_auth": HTTPSecurity("basic")}


# TODO: autogenerate example from faker
def docs_wrapper(response_model: type):
    return EndpointDocs(
        responses={
            200: ResponseInfo(
                "Profile",
                content=[
                    ContentInfo(
                        response_model,
                        examples=[...],  # TODO:
                    )
                ],
            )
        }
    )


docs = OpenAPIHandler(
    info=Info(title="VizMe API", version="0.0.1"),
    ui_path="/api/docs",
    json_spec_path="/api/openapi.json",
)
