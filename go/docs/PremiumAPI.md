# \PremiumAPI

All URIs are relative to *https://api.henrikdev.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddWebhookUser**](PremiumAPI.md#AddWebhookUser) | **Post** /public/v1/premium/webhook/users | Add premium webhook user
[**DeleteWebhookUser**](PremiumAPI.md#DeleteWebhookUser) | **Delete** /public/v1/premium/webhook/users/{id} | Delete premium webhook user
[**GetWebhookSettings**](PremiumAPI.md#GetWebhookSettings) | **Get** /public/v1/premium/webhook | Get premium webhook settings
[**UpdateWebhookUser**](PremiumAPI.md#UpdateWebhookUser) | **Put** /public/v1/premium/webhook/users/{id} | Update premium webhook user



## AddWebhookUser

> PremiumWebhookUserMutationResponse AddWebhookUser(ctx).PremiumWebhookUserAddRequest(premiumWebhookUserAddRequest).Execute()

Add premium webhook user

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/raimannma/valorant-api-clients"
)

func main() {
	premiumWebhookUserAddRequest := *openapiclient.NewPremiumWebhookUserAddRequest() // PremiumWebhookUserAddRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PremiumAPI.AddWebhookUser(context.Background()).PremiumWebhookUserAddRequest(premiumWebhookUserAddRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PremiumAPI.AddWebhookUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddWebhookUser`: PremiumWebhookUserMutationResponse
	fmt.Fprintf(os.Stdout, "Response from `PremiumAPI.AddWebhookUser`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiAddWebhookUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **premiumWebhookUserAddRequest** | [**PremiumWebhookUserAddRequest**](PremiumWebhookUserAddRequest.md) |  | 

### Return type

[**PremiumWebhookUserMutationResponse**](PremiumWebhookUserMutationResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteWebhookUser

> PremiumWebhookDeleteResponse DeleteWebhookUser(ctx, id).Execute()

Delete premium webhook user

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/raimannma/valorant-api-clients"
)

func main() {
	id := "id_example" // string | Tracked user id

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PremiumAPI.DeleteWebhookUser(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PremiumAPI.DeleteWebhookUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteWebhookUser`: PremiumWebhookDeleteResponse
	fmt.Fprintf(os.Stdout, "Response from `PremiumAPI.DeleteWebhookUser`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Tracked user id | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteWebhookUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PremiumWebhookDeleteResponse**](PremiumWebhookDeleteResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetWebhookSettings

> GetWebhookSettings(ctx).Execute()

Get premium webhook settings

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/raimannma/valorant-api-clients"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PremiumAPI.GetWebhookSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PremiumAPI.GetWebhookSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebhookSettingsRequest struct via the builder pattern


### Return type

 (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateWebhookUser

> UpdateWebhookUser(ctx, id).PremiumWebhookUserUpdateRequest(premiumWebhookUserUpdateRequest).Execute()

Update premium webhook user

### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/raimannma/valorant-api-clients"
)

func main() {
	id := "id_example" // string | Tracked user id
	premiumWebhookUserUpdateRequest := *openapiclient.NewPremiumWebhookUserUpdateRequest() // PremiumWebhookUserUpdateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PremiumAPI.UpdateWebhookUser(context.Background(), id).PremiumWebhookUserUpdateRequest(premiumWebhookUserUpdateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PremiumAPI.UpdateWebhookUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Tracked user id | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateWebhookUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **premiumWebhookUserUpdateRequest** | [**PremiumWebhookUserUpdateRequest**](PremiumWebhookUserUpdateRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

