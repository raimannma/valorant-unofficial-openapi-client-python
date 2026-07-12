# PremiumWebhookUserAddRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Enabled** | Pointer to **bool** |  | [optional] 
**Events** | Pointer to [**[]PremiumWebhookEvent**](PremiumWebhookEvent.md) |  | [optional] 
**Name** | Pointer to **NullableString** |  | [optional] 
**Puuid** | Pointer to **NullableString** |  | [optional] 
**Tag** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewPremiumWebhookUserAddRequest

`func NewPremiumWebhookUserAddRequest() *PremiumWebhookUserAddRequest`

NewPremiumWebhookUserAddRequest instantiates a new PremiumWebhookUserAddRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPremiumWebhookUserAddRequestWithDefaults

`func NewPremiumWebhookUserAddRequestWithDefaults() *PremiumWebhookUserAddRequest`

NewPremiumWebhookUserAddRequestWithDefaults instantiates a new PremiumWebhookUserAddRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEnabled

`func (o *PremiumWebhookUserAddRequest) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *PremiumWebhookUserAddRequest) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *PremiumWebhookUserAddRequest) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.

### HasEnabled

`func (o *PremiumWebhookUserAddRequest) HasEnabled() bool`

HasEnabled returns a boolean if a field has been set.

### GetEvents

`func (o *PremiumWebhookUserAddRequest) GetEvents() []PremiumWebhookEvent`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *PremiumWebhookUserAddRequest) GetEventsOk() (*[]PremiumWebhookEvent, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *PremiumWebhookUserAddRequest) SetEvents(v []PremiumWebhookEvent)`

SetEvents sets Events field to given value.

### HasEvents

`func (o *PremiumWebhookUserAddRequest) HasEvents() bool`

HasEvents returns a boolean if a field has been set.

### GetName

`func (o *PremiumWebhookUserAddRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PremiumWebhookUserAddRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PremiumWebhookUserAddRequest) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PremiumWebhookUserAddRequest) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *PremiumWebhookUserAddRequest) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *PremiumWebhookUserAddRequest) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetPuuid

`func (o *PremiumWebhookUserAddRequest) GetPuuid() string`

GetPuuid returns the Puuid field if non-nil, zero value otherwise.

### GetPuuidOk

`func (o *PremiumWebhookUserAddRequest) GetPuuidOk() (*string, bool)`

GetPuuidOk returns a tuple with the Puuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPuuid

`func (o *PremiumWebhookUserAddRequest) SetPuuid(v string)`

SetPuuid sets Puuid field to given value.

### HasPuuid

`func (o *PremiumWebhookUserAddRequest) HasPuuid() bool`

HasPuuid returns a boolean if a field has been set.

### SetPuuidNil

`func (o *PremiumWebhookUserAddRequest) SetPuuidNil(b bool)`

 SetPuuidNil sets the value for Puuid to be an explicit nil

### UnsetPuuid
`func (o *PremiumWebhookUserAddRequest) UnsetPuuid()`

UnsetPuuid ensures that no value is present for Puuid, not even an explicit nil
### GetTag

`func (o *PremiumWebhookUserAddRequest) GetTag() string`

GetTag returns the Tag field if non-nil, zero value otherwise.

### GetTagOk

`func (o *PremiumWebhookUserAddRequest) GetTagOk() (*string, bool)`

GetTagOk returns a tuple with the Tag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTag

`func (o *PremiumWebhookUserAddRequest) SetTag(v string)`

SetTag sets Tag field to given value.

### HasTag

`func (o *PremiumWebhookUserAddRequest) HasTag() bool`

HasTag returns a boolean if a field has been set.

### SetTagNil

`func (o *PremiumWebhookUserAddRequest) SetTagNil(b bool)`

 SetTagNil sets the value for Tag to be an explicit nil

### UnsetTag
`func (o *PremiumWebhookUserAddRequest) UnsetTag()`

UnsetTag ensures that no value is present for Tag, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


