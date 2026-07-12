# PremiumWebhookUserMutationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PremiumWebhookUserMutationData**](PremiumWebhookUserMutationData.md) |  | 

## Example

```python
from henrikdev_api_client.models.premium_webhook_user_mutation_response import PremiumWebhookUserMutationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookUserMutationResponse from a JSON string
premium_webhook_user_mutation_response_instance = PremiumWebhookUserMutationResponse.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookUserMutationResponse.to_json())

# convert the object into a dict
premium_webhook_user_mutation_response_dict = premium_webhook_user_mutation_response_instance.to_dict()
# create an instance of PremiumWebhookUserMutationResponse from a dict
premium_webhook_user_mutation_response_from_dict = PremiumWebhookUserMutationResponse.from_dict(premium_webhook_user_mutation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


