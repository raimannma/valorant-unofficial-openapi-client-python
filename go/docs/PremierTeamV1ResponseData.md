# PremierTeamV1ResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Customization** | [**PremierTeamV1ResponseDataCustomization**](PremierTeamV1ResponseDataCustomization.md) |  | 
**Enrolled** | **bool** |  | 
**Id** | **string** |  | 
**Member** | [**[]PremierTeamMember**](PremierTeamMember.md) |  | 
**Name** | **string** |  | 
**Placement** | [**PremierTeamV1ResponseDataPlacement**](PremierTeamV1ResponseDataPlacement.md) |  | 
**Ranked** | **bool** |  | 
**Stats** | [**PremierTeamV1ResponseDataStats**](PremierTeamV1ResponseDataStats.md) |  | 
**Tag** | **string** |  | 

## Methods

### NewPremierTeamV1ResponseData

`func NewPremierTeamV1ResponseData(customization PremierTeamV1ResponseDataCustomization, enrolled bool, id string, member []PremierTeamMember, name string, placement PremierTeamV1ResponseDataPlacement, ranked bool, stats PremierTeamV1ResponseDataStats, tag string, ) *PremierTeamV1ResponseData`

NewPremierTeamV1ResponseData instantiates a new PremierTeamV1ResponseData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPremierTeamV1ResponseDataWithDefaults

`func NewPremierTeamV1ResponseDataWithDefaults() *PremierTeamV1ResponseData`

NewPremierTeamV1ResponseDataWithDefaults instantiates a new PremierTeamV1ResponseData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCustomization

`func (o *PremierTeamV1ResponseData) GetCustomization() PremierTeamV1ResponseDataCustomization`

GetCustomization returns the Customization field if non-nil, zero value otherwise.

### GetCustomizationOk

`func (o *PremierTeamV1ResponseData) GetCustomizationOk() (*PremierTeamV1ResponseDataCustomization, bool)`

GetCustomizationOk returns a tuple with the Customization field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomization

`func (o *PremierTeamV1ResponseData) SetCustomization(v PremierTeamV1ResponseDataCustomization)`

SetCustomization sets Customization field to given value.


### GetEnrolled

`func (o *PremierTeamV1ResponseData) GetEnrolled() bool`

GetEnrolled returns the Enrolled field if non-nil, zero value otherwise.

### GetEnrolledOk

`func (o *PremierTeamV1ResponseData) GetEnrolledOk() (*bool, bool)`

GetEnrolledOk returns a tuple with the Enrolled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnrolled

`func (o *PremierTeamV1ResponseData) SetEnrolled(v bool)`

SetEnrolled sets Enrolled field to given value.


### GetId

`func (o *PremierTeamV1ResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PremierTeamV1ResponseData) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PremierTeamV1ResponseData) SetId(v string)`

SetId sets Id field to given value.


### GetMember

`func (o *PremierTeamV1ResponseData) GetMember() []PremierTeamMember`

GetMember returns the Member field if non-nil, zero value otherwise.

### GetMemberOk

`func (o *PremierTeamV1ResponseData) GetMemberOk() (*[]PremierTeamMember, bool)`

GetMemberOk returns a tuple with the Member field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMember

`func (o *PremierTeamV1ResponseData) SetMember(v []PremierTeamMember)`

SetMember sets Member field to given value.


### GetName

`func (o *PremierTeamV1ResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PremierTeamV1ResponseData) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PremierTeamV1ResponseData) SetName(v string)`

SetName sets Name field to given value.


### GetPlacement

`func (o *PremierTeamV1ResponseData) GetPlacement() PremierTeamV1ResponseDataPlacement`

GetPlacement returns the Placement field if non-nil, zero value otherwise.

### GetPlacementOk

`func (o *PremierTeamV1ResponseData) GetPlacementOk() (*PremierTeamV1ResponseDataPlacement, bool)`

GetPlacementOk returns a tuple with the Placement field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlacement

`func (o *PremierTeamV1ResponseData) SetPlacement(v PremierTeamV1ResponseDataPlacement)`

SetPlacement sets Placement field to given value.


### GetRanked

`func (o *PremierTeamV1ResponseData) GetRanked() bool`

GetRanked returns the Ranked field if non-nil, zero value otherwise.

### GetRankedOk

`func (o *PremierTeamV1ResponseData) GetRankedOk() (*bool, bool)`

GetRankedOk returns a tuple with the Ranked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRanked

`func (o *PremierTeamV1ResponseData) SetRanked(v bool)`

SetRanked sets Ranked field to given value.


### GetStats

`func (o *PremierTeamV1ResponseData) GetStats() PremierTeamV1ResponseDataStats`

GetStats returns the Stats field if non-nil, zero value otherwise.

### GetStatsOk

`func (o *PremierTeamV1ResponseData) GetStatsOk() (*PremierTeamV1ResponseDataStats, bool)`

GetStatsOk returns a tuple with the Stats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStats

`func (o *PremierTeamV1ResponseData) SetStats(v PremierTeamV1ResponseDataStats)`

SetStats sets Stats field to given value.


### GetTag

`func (o *PremierTeamV1ResponseData) GetTag() string`

GetTag returns the Tag field if non-nil, zero value otherwise.

### GetTagOk

`func (o *PremierTeamV1ResponseData) GetTagOk() (*string, bool)`

GetTagOk returns a tuple with the Tag field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTag

`func (o *PremierTeamV1ResponseData) SetTag(v string)`

SetTag sets Tag field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


