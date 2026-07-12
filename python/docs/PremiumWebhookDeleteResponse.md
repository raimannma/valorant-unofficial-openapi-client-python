# PremiumWebhookDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PremiumWebhookDeleteData**](PremiumWebhookDeleteData.md) |  | 

## Example

```python
from henrikdev_api_client.models.premium_webhook_delete_response import PremiumWebhookDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookDeleteResponse from a JSON string
premium_webhook_delete_response_instance = PremiumWebhookDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookDeleteResponse.to_json())

# convert the object into a dict
premium_webhook_delete_response_dict = premium_webhook_delete_response_instance.to_dict()
# create an instance of PremiumWebhookDeleteResponse from a dict
premium_webhook_delete_response_from_dict = PremiumWebhookDeleteResponse.from_dict(premium_webhook_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


