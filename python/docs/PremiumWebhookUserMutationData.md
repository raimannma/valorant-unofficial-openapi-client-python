# PremiumWebhookUserMutationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**user** | [**PremiumWebhookUserResponse**](PremiumWebhookUserResponse.md) |  | 

## Example

```python
from henrikdev_api_client.models.premium_webhook_user_mutation_data import PremiumWebhookUserMutationData

# TODO update the JSON string below
json = "{}"
# create an instance of PremiumWebhookUserMutationData from a JSON string
premium_webhook_user_mutation_data_instance = PremiumWebhookUserMutationData.from_json(json)
# print the JSON string representation of the object
print(PremiumWebhookUserMutationData.to_json())

# convert the object into a dict
premium_webhook_user_mutation_data_dict = premium_webhook_user_mutation_data_instance.to_dict()
# create an instance of PremiumWebhookUserMutationData from a dict
premium_webhook_user_mutation_data_from_dict = PremiumWebhookUserMutationData.from_dict(premium_webhook_user_mutation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


