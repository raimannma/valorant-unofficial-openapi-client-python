# PremiumWebhookUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**enabled** | **bool** |  | 
**events** | [**List[PremiumWebhookEvent]**](PremiumWebhookEvent.md) |  | 
**id** | **str** |  | 
**last_checked_at** | **int** |  | [optional] 
**last_match** | **str** |  | [optional] 
**last_mmr** | **int** |  | [optional] 
**puuid** | **str** |  | 
**region** | **str** |  | 
**updated_at** | **int** |  | 

## Example

```python
from henrikdev_api_client.models.premium_webhook_user_response import PremiumWebhookUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookUserResponse from a JSON string
premium_webhook_user_response_instance = PremiumWebhookUserResponse.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookUserResponse.to_json())

# convert the object into a dict
premium_webhook_user_response_dict = premium_webhook_user_response_instance.to_dict()
# create an instance of PremiumWebhookUserResponse from a dict
premium_webhook_user_response_from_dict = PremiumWebhookUserResponse.from_dict(premium_webhook_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


