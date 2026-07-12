# OpenAPI\Client\PremiumApi

Premium account and webhook endpoints

All URIs are relative to https://api.henrikdev.xyz, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addWebhookUser()**](PremiumApi.md#addWebhookUser) | **POST** /public/v1/premium/webhook/users | Add premium webhook user |
| [**deleteWebhookUser()**](PremiumApi.md#deleteWebhookUser) | **DELETE** /public/v1/premium/webhook/users/{id} | Delete premium webhook user |
| [**getWebhookSettings()**](PremiumApi.md#getWebhookSettings) | **GET** /public/v1/premium/webhook | Get premium webhook settings |
| [**updateWebhookUser()**](PremiumApi.md#updateWebhookUser) | **PUT** /public/v1/premium/webhook/users/{id} | Update premium webhook user |


## `addWebhookUser()`

```php
addWebhookUser($premium_webhook_user_add_request): \OpenAPI\Client\Model\PremiumWebhookUserMutationResponse
```

Add premium webhook user

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\PremiumApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$premium_webhook_user_add_request = new \OpenAPI\Client\Model\PremiumWebhookUserAddRequest(); // \OpenAPI\Client\Model\PremiumWebhookUserAddRequest

try {
    $result = $apiInstance->addWebhookUser($premium_webhook_user_add_request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PremiumApi->addWebhookUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **premium_webhook_user_add_request** | [**\OpenAPI\Client\Model\PremiumWebhookUserAddRequest**](../Model/PremiumWebhookUserAddRequest.md)|  | |

### Return type

[**\OpenAPI\Client\Model\PremiumWebhookUserMutationResponse**](../Model/PremiumWebhookUserMutationResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `deleteWebhookUser()`

```php
deleteWebhookUser($id): \OpenAPI\Client\Model\PremiumWebhookDeleteResponse
```

Delete premium webhook user

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\PremiumApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Tracked user id

try {
    $result = $apiInstance->deleteWebhookUser($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling PremiumApi->deleteWebhookUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Tracked user id | |

### Return type

[**\OpenAPI\Client\Model\PremiumWebhookDeleteResponse**](../Model/PremiumWebhookDeleteResponse.md)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getWebhookSettings()`

```php
getWebhookSettings()
```

Get premium webhook settings

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\PremiumApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);

try {
    $apiInstance->getWebhookSettings();
} catch (Exception $e) {
    echo 'Exception when calling PremiumApi->getWebhookSettings: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateWebhookUser()`

```php
updateWebhookUser($id, $premium_webhook_user_update_request)
```

Update premium webhook user

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure API key authorization: api_key_query
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('api_key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('api_key', 'Bearer');

// Configure API key authorization: api_key_header
$config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKey('Authorization', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = OpenAPI\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Authorization', 'Bearer');


$apiInstance = new OpenAPI\Client\Api\PremiumApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$id = 'id_example'; // string | Tracked user id
$premium_webhook_user_update_request = new \OpenAPI\Client\Model\PremiumWebhookUserUpdateRequest(); // \OpenAPI\Client\Model\PremiumWebhookUserUpdateRequest

try {
    $apiInstance->updateWebhookUser($id, $premium_webhook_user_update_request);
} catch (Exception $e) {
    echo 'Exception when calling PremiumApi->updateWebhookUser: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **id** | **string**| Tracked user id | |
| **premium_webhook_user_update_request** | [**\OpenAPI\Client\Model\PremiumWebhookUserUpdateRequest**](../Model/PremiumWebhookUserUpdateRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

[api_key_query](../../README.md#api_key_query), [api_key_header](../../README.md#api_key_header)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
