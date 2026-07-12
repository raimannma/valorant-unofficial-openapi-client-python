# henrikdev_api_client.api.PremiumApi

## Load the API package
```dart
import 'package:henrikdev_api_client/api.dart';
```

All URIs are relative to *https://api.henrikdev.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addWebhookUser**](PremiumApi.md#addwebhookuser) | **POST** /public/v1/premium/webhook/users | Add premium webhook user
[**deleteWebhookUser**](PremiumApi.md#deletewebhookuser) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user
[**getWebhookSettings**](PremiumApi.md#getwebhooksettings) | **GET** /public/v1/premium/webhook | Get premium webhook settings
[**updateWebhookUser**](PremiumApi.md#updatewebhookuser) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user


# **addWebhookUser**
> PremiumWebhookUserMutationResponse addWebhookUser(premiumWebhookUserAddRequest)

Add premium webhook user

### Example
```dart
import 'package:henrikdev_api_client/api.dart';
// TODO Configure API key authorization: api_key_query
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKeyPrefix = 'Bearer';
// TODO Configure API key authorization: api_key_header
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKeyPrefix = 'Bearer';

final api_instance = PremiumApi();
final premiumWebhookUserAddRequest = PremiumWebhookUserAddRequest(); // PremiumWebhookUserAddRequest | 

try {
    final result = api_instance.addWebhookUser(premiumWebhookUserAddRequest);
    print(result);
} catch (e) {
    print('Exception when calling PremiumApi->addWebhookUser: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **premiumWebhookUserAddRequest** | [**PremiumWebhookUserAddRequest**](PremiumWebhookUserAddRequest.md)|  | 

### Return type

[**PremiumWebhookUserMutationResponse**](PremiumWebhookUserMutationResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteWebhookUser**
> PremiumWebhookDeleteResponse deleteWebhookUser(id)

Delete premium webhook user

### Example
```dart
import 'package:henrikdev_api_client/api.dart';
// TODO Configure API key authorization: api_key_query
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKeyPrefix = 'Bearer';
// TODO Configure API key authorization: api_key_header
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKeyPrefix = 'Bearer';

final api_instance = PremiumApi();
final id = id_example; // String | Tracked user id

try {
    final result = api_instance.deleteWebhookUser(id);
    print(result);
} catch (e) {
    print('Exception when calling PremiumApi->deleteWebhookUser: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Tracked user id | 

### Return type

[**PremiumWebhookDeleteResponse**](PremiumWebhookDeleteResponse.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getWebhookSettings**
> getWebhookSettings()

Get premium webhook settings

### Example
```dart
import 'package:henrikdev_api_client/api.dart';
// TODO Configure API key authorization: api_key_query
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKeyPrefix = 'Bearer';
// TODO Configure API key authorization: api_key_header
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKeyPrefix = 'Bearer';

final api_instance = PremiumApi();

try {
    api_instance.getWebhookSettings();
} catch (e) {
    print('Exception when calling PremiumApi->getWebhookSettings: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateWebhookUser**
> updateWebhookUser(id, premiumWebhookUserUpdateRequest)

Update premium webhook user

### Example
```dart
import 'package:henrikdev_api_client/api.dart';
// TODO Configure API key authorization: api_key_query
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_query').apiKeyPrefix = 'Bearer';
// TODO Configure API key authorization: api_key_header
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('api_key_header').apiKeyPrefix = 'Bearer';

final api_instance = PremiumApi();
final id = id_example; // String | Tracked user id
final premiumWebhookUserUpdateRequest = PremiumWebhookUserUpdateRequest(); // PremiumWebhookUserUpdateRequest | 

try {
    api_instance.updateWebhookUser(id, premiumWebhookUserUpdateRequest);
} catch (e) {
    print('Exception when calling PremiumApi->updateWebhookUser: $e\n');
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Tracked user id | 
 **premiumWebhookUserUpdateRequest** | [**PremiumWebhookUserUpdateRequest**](PremiumWebhookUserUpdateRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

