# PremierTeamLiteResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | **str** |  | 
**conference** | **str** |  | 
**customization** | [**PremierTeamV1ResponseDataCustomization**](PremierTeamV1ResponseDataCustomization.md) |  | 
**division** | **int** |  | 
**id** | **str** |  | 
**losses** | **int** |  | 
**name** | **str** |  | 
**ranked** | **bool** |  | 
**ranking** | **int** |  | 
**region** | **str** |  | 
**score** | **int** |  | 
**tag** | **str** |  | 
**updated_at** | **str** |  | 
**wins** | **int** |  | 

## Example

```python
from henrikdev_api_client.models.premier_team_lite_response_data import PremierTeamLiteResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PremierTeamLiteResponseData from a JSON string
premier_team_lite_response_data_instance = PremierTeamLiteResponseData.from_json(json)
# print the JSON string representation of the object
print(PremierTeamLiteResponseData.to_json())

# convert the object into a dict
premier_team_lite_response_data_dict = premier_team_lite_response_data_instance.to_dict()
# create an instance of PremierTeamLiteResponseData from a dict
premier_team_lite_response_data_from_dict = PremierTeamLiteResponseData.from_dict(premier_team_lite_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


