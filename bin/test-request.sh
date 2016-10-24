#!/bin/sh

# Set the below variables via environment variables
# crucibleBaseUrl - should be of the form: https://www.crucibleserver.com
# crucibleRestKey - key from Crucible Administration -> Authentication -> Rest API Token

curl -v -X PUT -H "X-Api-Key: $crucibleRestKey" -H "Content-Type: application/json" -m 20 $crucibleBaseUrl/rest-service-fecru/admin/repositories/Athena/incremental-index
