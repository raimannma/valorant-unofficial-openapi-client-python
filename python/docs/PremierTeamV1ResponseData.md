# PremierTeamV1ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customization** | [**PremierTeamV1ResponseDataCustomization**](PremierTeamV1ResponseDataCustomization.md) |  | 
**enrolled** | **bool** |  | 
**id** | **str** |  | 
**member** | [**List[PremierTeamMember]**](PremierTeamMember.md) |  | 
**name** | **str** |  | 
**placement** | [**PremierTeamV1ResponseDataPlacement**](PremierTeamV1ResponseDataPlacement.md) |  | 
**ranked** | **bool** |  | 
**stats** | [**PremierTeamV1ResponseDataStats**](PremierTeamV1ResponseDataStats.md) |  | 
**tag** | **str** |  | 

## Example

```python
from henrikdev_api_client.models.premier_team_v1_response_data import PremierTeamV1ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PremierTeamV1ResponseData from a JSON string
premier_team_v1_response_data_instance = PremierTeamV1ResponseData.from_json(json)
# print the JSON string representation of the object
print(PremierTeamV1ResponseData.to_json())

# convert the object into a dict
premier_team_v1_response_data_dict = premier_team_v1_response_data_instance.to_dict()
# create an instance of PremierTeamV1ResponseData from a dict
premier_team_v1_response_data_from_dict = PremierTeamV1ResponseData.from_dict(premier_team_v1_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


