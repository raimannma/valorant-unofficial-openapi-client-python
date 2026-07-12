# PremiumWebhookUserAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**events** | [**List[PremiumWebhookEvent]**](PremiumWebhookEvent.md) |  | [optional] 
**name** | **str** |  | [optional] 
**puuid** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from henrikdev_api_client.models.premium_webhook_user_add_request import PremiumWebhookUserAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookUserAddRequest from a JSON string
premium_webhook_user_add_request_instance = PremiumWebhookUserAddRequest.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookUserAddRequest.to_json())

# convert the object into a dict
premium_webhook_user_add_request_dict = premium_webhook_user_add_request_instance.to_dict()
# create an instance of PremiumWebhookUserAddRequest from a dict
premium_webhook_user_add_request_from_dict = PremiumWebhookUserAddRequest.from_dict(premium_webhook_user_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


