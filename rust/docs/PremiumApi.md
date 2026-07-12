# \PremiumApi

All URIs are relative to *https://api.henrikdev.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook_user**](PremiumApi.md#add_webhook_user) | **POST** /public/v1/premium/webhook/users | Add premium webhook user
[**delete_webhook_user**](PremiumApi.md#delete_webhook_user) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user
[**get_webhook_settings**](PremiumApi.md#get_webhook_settings) | **GET** /public/v1/premium/webhook | Get premium webhook settings
[**update_webhook_user**](PremiumApi.md#update_webhook_user) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user



## add_webhook_user

> models::PremiumWebhookUserMutationResponse add_webhook_user(premium_webhook_user_add_request)
Add premium webhook user

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**premium_webhook_user_add_request** | [**PremiumWebhookUserAddRequest**](PremiumWebhookUserAddRequest.md) |  | [required] |

### Return type

[**models::PremiumWebhookUserMutationResponse**](PremiumWebhookUserMutationResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_webhook_user

> models::PremiumWebhookDeleteResponse delete_webhook_user(id)
Delete premium webhook user

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | Tracked user id | [required] |

### Return type

[**models::PremiumWebhookDeleteResponse**](PremiumWebhookDeleteResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_webhook_settings

> get_webhook_settings()
Get premium webhook settings

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## update_webhook_user

> update_webhook_user(id, premium_webhook_user_update_request)
Update premium webhook user

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | Tracked user id | [required] |
**premium_webhook_user_update_request** | [**PremiumWebhookUserUpdateRequest**](PremiumWebhookUserUpdateRequest.md) |  | [required] |

### Return type

 (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

