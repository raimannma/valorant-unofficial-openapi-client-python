# PremierTeamLiteResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Affinity** | **string** |  | 
**Conference** | **string** |  | 
**Customization** | [**PremierTeamV1ResponseDataCustomization**](PremierTeamV1ResponseDataCustomization.md) |  | 
**Division** | **int32** |  | 
**Id** | **string** |  | 
**Losses** | **int32** |  | 
**Name** | **string** |  | 
**Ranked** | **bool** |  | 
**Ranking** | **int32** |  | 
**Region** | **string** |  | 
**Score** | **int32** |  | 
**Tag** | **string** |  | 
**UpdatedAt** | **string** |  | 
**Wins** | **int32** |  | 

## Methods

### NewPremierTeamLiteResponseData

`func NewPremierTeamLiteResponseData(affinity string, conference string, customization PremierTeamV1ResponseDataCustomization, division int32, id string, losses int32, name string, ranked bool, ranking int32, region string, score int32, tag string, updatedAt string, wins int32, ) *PremierTeamLiteResponseData`

NewPremierTeamLiteResponseData instantiates a new PremierTeamLiteResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPremierTeamLiteResponseDataWithDefaults

`func NewPremierTeamLiteResponseDataWithDefaults() *PremierTeamLiteResponseData`

NewPremierTeamLiteResponseDataWithDefaults instantiates a new PremierTeamLiteResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAffinity

`func (o *PremierTeamLiteResponseData) GetAffinity() string`

GetAffinity returns the Affinity field if non-nil, zero value otherwise.

### GetAffinityOk

`func (o *PremierTeamLiteResponseData) GetAffinityOk() (*string, bool)`

GetAffinityOk returns a tuple with the Affinity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAffinity

`func (o *PremierTeamLiteResponseData) SetAffinity(v string)`

SetAffinity sets Affinity field to given value.


### GetConference

`func (o *PremierTeamLiteResponseData) GetConference() string`

GetConference returns the Conference field if non-nil, zero value otherwise.

### GetConferenceOk

`func (o *PremierTeamLiteResponseData) GetConferenceOk() (*string, bool)`

GetConferenceOk returns a tuple with the Conference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConference

`func (o *PremierTeamLiteResponseData) SetConference(v string)`

SetConference sets Conference field to given value.


### GetCustomization

`func (o *PremierTeamLiteResponseData) GetCustomization() PremierTeamV1ResponseDataCustomization`

GetCustomization returns the Customization field if non-nil, zero value otherwise.

### GetCustomizationOk

`func (o *PremierTeamLiteResponseData) GetCustomizationOk() (*PremierTeamV1ResponseDataCustomization, bool)`

GetCustomizationOk returns a tuple with the Customization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomization

`func (o *PremierTeamLiteResponseData) SetCustomization(v PremierTeamV1ResponseDataCustomization)`

SetCustomization sets Customization field to given value.


### GetDivision

`func (o *PremierTeamLiteResponseData) GetDivision() int32`

GetDivision returns the Division field if non-nil, zero value otherwise.

### GetDivisionOk

`func (o *PremierTeamLiteResponseData) GetDivisionOk() (*int32, bool)`

GetDivisionOk returns a tuple with the Division field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDivision

`func (o *PremierTeamLiteResponseData) SetDivision(v int32)`

SetDivision sets Division field to given value.


### GetId

`func (o *PremierTeamLiteResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PremierTeamLiteResponseData) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PremierTeamLiteResponseData) SetId(v string)`

SetId sets Id field to given value.


### GetLosses

`func (o *PremierTeamLiteResponseData) GetLosses() int32`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *PremierTeamLiteResponseData) GetLossesOk() (*int32, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *PremierTeamLiteResponseData) SetLosses(v int32)`

SetLosses sets Losses field to given value.


### GetName

`func (o *PremierTeamLiteResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PremierTeamLiteResponseData) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PremierTeamLiteResponseData) SetName(v string)`

SetName sets Name field to given value.


### GetRanked

`func (o *PremierTeamLiteResponseData) GetRanked() bool`

GetRanked returns the Ranked field if non-nil, zero value otherwise.

### GetRankedOk

`func (o *PremierTeamLiteResponseData) GetRankedOk() (*bool, bool)`

GetRankedOk returns a tuple with the Ranked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRanked

`func (o *PremierTeamLiteResponseData) SetRanked(v bool)`

SetRanked sets Ranked field to given value.


### GetRanking

`func (o *PremierTeamLiteResponseData) GetRanking() int32`

GetRanking returns the Ranking field if non-nil, zero value otherwise.

### GetRankingOk

`func (o *PremierTeamLiteResponseData) GetRankingOk() (*int32, bool)`

GetRankingOk returns a tuple with the Ranking field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRanking

`func (o *PremierTeamLiteResponseData) SetRanking(v int32)`

SetRanking sets Ranking field to given value.


### GetRegion

`func (o *PremierTeamLiteResponseData) GetRegion() string`

GetRegion returns the Region field if non-nil, zero value otherwise.

### GetRegionOk

`func (o *PremierTeamLiteResponseData) GetRegionOk() (*string, bool)`

GetRegionOk returns a tuple with the Region field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRegion

`func (o *PremierTeamLiteResponseData) SetRegion(v string)`

SetRegion sets Region field to given value.


### GetScore

`func (o *PremierTeamLiteResponseData) GetScore() int32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *PremierTeamLiteResponseData) GetScoreOk() (*int32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *PremierTeamLiteResponseData) SetScore(v int32)`

SetScore sets Score field to given value.


### GetTag

`func (o *PremierTeamLiteResponseData) GetTag() string`

GetTag returns the Tag field if non-nil, zero value otherwise.

### GetTagOk

`func (o *PremierTeamLiteResponseData) GetTagOk() (*string, bool)`

GetTagOk returns a tuple with the Tag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTag

`func (o *PremierTeamLiteResponseData) SetTag(v string)`

SetTag sets Tag field to given value.


### GetUpdatedAt

`func (o *PremierTeamLiteResponseData) GetUpdatedAt() string`

GetUpdatedAt returns the UpdatedAt field if non-nil, zero value otherwise.

### GetUpdatedAtOk

`func (o *PremierTeamLiteResponseData) GetUpdatedAtOk() (*string, bool)`

GetUpdatedAtOk returns a tuple with the UpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdatedAt

`func (o *PremierTeamLiteResponseData) SetUpdatedAt(v string)`

SetUpdatedAt sets UpdatedAt field to given value.


### GetWins

`func (o *PremierTeamLiteResponseData) GetWins() int32`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *PremierTeamLiteResponseData) GetWinsOk() (*int32, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *PremierTeamLiteResponseData) SetWins(v int32)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


