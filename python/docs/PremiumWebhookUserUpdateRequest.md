# PremiumWebhookUserUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[PremiumWebhookEvent]**](PremiumWebhookEvent.md) |  | [optional] 

## Example

```python
from henrikdev_api_client.models.premium_webhook_user_update_request import PremiumWebhookUserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookUserUpdateRequest from a JSON string
premium_webhook_user_update_request_instance = PremiumWebhookUserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookUserUpdateRequest.to_json())

# convert the object into a dict
premium_webhook_user_update_request_dict = premium_webhook_user_update_request_instance.to_dict()
# create an instance of PremiumWebhookUserUpdateRequest from a dict
premium_webhook_user_update_request_from_dict = PremiumWebhookUserUpdateRequest.from_dict(premium_webhook_user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


