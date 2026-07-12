# PremiumWebhookUserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CreatedAt** | **int64** |  | 
**Enabled** | **bool** |  | 
**Events** | [**[]PremiumWebhookEvent**](PremiumWebhookEvent.md) |  | 
**Id** | **string** |  | 
**LastCheckedAt** | Pointer to **NullableInt64** |  | [optional] 
**LastMatch** | Pointer to **NullableString** |  | [optional] 
**LastMmr** | Pointer to **NullableInt32** |  | [optional] 
**Puuid** | **string** |  | 
**Region** | **string** |  | 
**UpdatedAt** | **int64** |  | 

## Methods

### NewPremiumWebhookUserResponse

`func NewPremiumWebhookUserResponse(createdAt int64, enabled bool, events []PremiumWebhookEvent, id string, puuid string, region string, updatedAt int64, ) *PremiumWebhookUserResponse`

NewPremiumWebhookUserResponse instantiates a new PremiumWebhookUserResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPremiumWebhookUserResponseWithDefaults

`func NewPremiumWebhookUserResponseWithDefaults() *PremiumWebhookUserResponse`

NewPremiumWebhookUserResponseWithDefaults instantiates a new PremiumWebhookUserResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCreatedAt

`func (o *PremiumWebhookUserResponse) GetCreatedAt() int64`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *PremiumWebhookUserResponse) GetCreatedAtOk() (*int64, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *PremiumWebhookUserResponse) SetCreatedAt(v int64)`

SetCreatedAt sets CreatedAt field to given value.


### GetEnabled

`func (o *PremiumWebhookUserResponse) GetEnabled() bool`

GetEnabled returns the Enabled field if non-nil, zero value otherwise.

### GetEnabledOk

`func (o *PremiumWebhookUserResponse) GetEnabledOk() (*bool, bool)`

GetEnabledOk returns a tuple with the Enabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnabled

`func (o *PremiumWebhookUserResponse) SetEnabled(v bool)`

SetEnabled sets Enabled field to given value.


### GetEvents

`func (o *PremiumWebhookUserResponse) GetEvents() []PremiumWebhookEvent`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *PremiumWebhookUserResponse) GetEventsOk() (*[]PremiumWebhookEvent, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *PremiumWebhookUserResponse) SetEvents(v []PremiumWebhookEvent)`

SetEvents sets Events field to given value.


### GetId

`func (o *PremiumWebhookUserResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PremiumWebhookUserResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PremiumWebhookUserResponse) SetId(v string)`

SetId sets Id field to given value.


### GetLastCheckedAt

`func (o *PremiumWebhookUserResponse) GetLastCheckedAt() int64`

GetLastCheckedAt returns the LastCheckedAt field if non-nil, zero value otherwise.

### GetLastCheckedAtOk

`func (o *PremiumWebhookUserResponse) GetLastCheckedAtOk() (*int64, bool)`

GetLastCheckedAtOk returns a tuple with the LastCheckedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastCheckedAt

`func (o *PremiumWebhookUserResponse) SetLastCheckedAt(v int64)`

SetLastCheckedAt sets LastCheckedAt field to given value.

### HasLastCheckedAt

`func (o *PremiumWebhookUserResponse) HasLastCheckedAt() bool`

HasLastCheckedAt returns a boolean if a field has been set.

### SetLastCheckedAtNil

`func (o *PremiumWebhookUserResponse) SetLastCheckedAtNil(b bool)`

 SetLastCheckedAtNil sets the value for LastCheckedAt to be an explicit nil

### UnsetLastCheckedAt
`func (o *PremiumWebhookUserResponse) UnsetLastCheckedAt()`

UnsetLastCheckedAt ensures that no value is present for LastCheckedAt, not even an explicit nil
### GetLastMatch

`func (o *PremiumWebhookUserResponse) GetLastMatch() string`

GetLastMatch returns the LastMatch field if non-nil, zero value otherwise.

### GetLastMatchOk

`func (o *PremiumWebhookUserResponse) GetLastMatchOk() (*string, bool)`

GetLastMatchOk returns a tuple with the LastMatch field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastMatch

`func (o *PremiumWebhookUserResponse) SetLastMatch(v string)`

SetLastMatch sets LastMatch field to given value.

### HasLastMatch

`func (o *PremiumWebhookUserResponse) HasLastMatch() bool`

HasLastMatch returns a boolean if a field has been set.

### SetLastMatchNil

`func (o *PremiumWebhookUserResponse) SetLastMatchNil(b bool)`

 SetLastMatchNil sets the value for LastMatch to be an explicit nil

### UnsetLastMatch
`func (o *PremiumWebhookUserResponse) UnsetLastMatch()`

UnsetLastMatch ensures that no value is present for LastMatch, not even an explicit nil
### GetLastMmr

`func (o *PremiumWebhookUserResponse) GetLastMmr() int32`

GetLastMmr returns the LastMmr field if non-nil, zero value otherwise.

### GetLastMmrOk

`func (o *PremiumWebhookUserResponse) GetLastMmrOk() (*int32, bool)`

GetLastMmrOk returns a tuple with the LastMmr field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastMmr

`func (o *PremiumWebhookUserResponse) SetLastMmr(v int32)`

SetLastMmr sets LastMmr field to given value.

### HasLastMmr

`func (o *PremiumWebhookUserResponse) HasLastMmr() bool`

HasLastMmr returns a boolean if a field has been set.

### SetLastMmrNil

`func (o *PremiumWebhookUserResponse) SetLastMmrNil(b bool)`

 SetLastMmrNil sets the value for LastMmr to be an explicit nil

### UnsetLastMmr
`func (o *PremiumWebhookUserResponse) UnsetLastMmr()`

UnsetLastMmr ensures that no value is present for LastMmr, not even an explicit nil
### GetPuuid

`func (o *PremiumWebhookUserResponse) GetPuuid() string`

GetPuuid returns the Puuid field if non-nil, zero value otherwise.

### GetPuuidOk

`func (o *PremiumWebhookUserResponse) GetPuuidOk() (*string, bool)`

GetPuuidOk returns a tuple with the Puuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPuuid

`func (o *PremiumWebhookUserResponse) SetPuuid(v string)`

SetPuuid sets Puuid field to given value.


### GetRegion

`func (o *PremiumWebhookUserResponse) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PremiumWebhookUserResponse) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PremiumWebhookUserResponse) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetUpdatedAt

`func (o *PremiumWebhookUserResponse) GetUpdatedAt() int64`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PremiumWebhookUserResponse) GetUpdatedAtOk() (*int64, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PremiumWebhookUserResponse) SetUpdatedAt(v int64)`

SetUpdatedAt sets UpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


