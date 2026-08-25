# ContentItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssetName** | **string** |  | 
**Id** | Pointer to **NullableString** |  | [optional] 
**LocalizedNames** | Pointer to **map[string]string** |  | [optional] 
**Name** | **string** |  | 

## Methods

### NewContentItem

`func NewContentItem(assetName string, name string, ) *ContentItem`

NewContentItem instantiates a new ContentItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentItemWithDefaults

`func NewContentItemWithDefaults() *ContentItem`

NewContentItemWithDefaults instantiates a new ContentItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssetName

`func (o *ContentItem) GetAssetName() string`

GetAssetName returns the AssetName field if non-nil, zero value otherwise.

### GetAssetNameOk

`func (o *ContentItem) GetAssetNameOk() (*string, bool)`

GetAssetNameOk returns a tuple with the AssetName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetName

`func (o *ContentItem) SetAssetName(v string)`

SetAssetName sets AssetName field to given value.


### GetId

`func (o *ContentItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ContentItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ContentItem) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *ContentItem) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *ContentItem) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *ContentItem) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetLocalizedNames

`func (o *ContentItem) GetLocalizedNames() map[string]string`

GetLocalizedNames returns the LocalizedNames field if non-nil, zero value otherwise.

### GetLocalizedNamesOk

`func (o *ContentItem) GetLocalizedNamesOk() (*map[string]string, bool)`

GetLocalizedNamesOk returns a tuple with the LocalizedNames field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLocalizedNames

`func (o *ContentItem) SetLocalizedNames(v map[string]string)`

SetLocalizedNames sets LocalizedNames field to given value.

### HasLocalizedNames

`func (o *ContentItem) HasLocalizedNames() bool`

HasLocalizedNames returns a boolean if a field has been set.

### SetLocalizedNamesNil

`func (o *ContentItem) SetLocalizedNamesNil(b bool)`

 SetLocalizedNamesNil sets the value for LocalizedNames to be an explicit nil

### UnsetLocalizedNames
`func (o *ContentItem) UnsetLocalizedNames()`

UnsetLocalizedNames ensures that no value is present for LocalizedNames, not even an explicit nil
### GetName

`func (o *ContentItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ContentItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ContentItem) SetName(v string)`

SetName sets Name field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


