import dtlpy as dl

if dl.token_expired():
    dl.login()
# Define the Slot:
slot = [
    dl.PackageSlot(
        # Define the module
        module_name="default_module",
        # Define the desired function
        function_name="hello",
        # Define a display name for the UI
        display_name="my-hello-function",
        # Post Action Example - download the item that the function returns
        post_action=dl.SlotPostAction(type=dl.SlotPostActionType.DOWNLOAD),
        # Display Scopes Example - set the relevant resource for the function
        display_scopes=[
            dl.SlotDisplayScope(
                resource=dl.SlotDisplayScopeResource.ITEM,
                # Filter Example - only video items
                filters=dl.Filters(
                    resource="dl.FILTERS_RESOURCE_ITEM",
                    field="metadata.system.mimetype",
                    values="video*",
                ),
            )
        ],
    )
]


