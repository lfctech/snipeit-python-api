#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
API_KEY_FILE="$SCRIPT_DIR/api_key.txt"
API_URL="http://localhost:${APP_PORT:-8000}/api/v1/users/me"
TIMEOUT=120

compose_logs() {
    service=$1
    (cd "$SCRIPT_DIR" && docker compose logs "$service") || true
}

fail_for_directory() {
    if [ -d "$API_KEY_FILE" ]; then
        echo "ERROR: docker/api_key.txt is a directory, not a file. Run 'make docker-down' to reset."
        compose_logs seeder
        exit 1
    fi
}

echo "Waiting for docker/api_key.txt (up to ~${TIMEOUT}s)..."
i=0
while [ "$i" -lt "$TIMEOUT" ]; do
    fail_for_directory
    if [ -f "$API_KEY_FILE" ] && [ -s "$API_KEY_FILE" ]; then
        break
    fi
    sleep 1
    i=$((i + 1))
done

fail_for_directory
if [ ! -f "$API_KEY_FILE" ] || [ ! -s "$API_KEY_FILE" ]; then
    echo "Timed out waiting for docker/api_key.txt."
    compose_logs seeder
    exit 1
fi

TOKEN=$(cat "$API_KEY_FILE")
echo "Waiting for Snipe-IT API to accept authenticated requests (up to ~${TIMEOUT}s)..."
i=0
code=000
while [ "$i" -lt "$TIMEOUT" ]; do
    code=$(curl -s -o /dev/null -w "%{http_code}" -m 5 \
        -H "Authorization: Bearer $TOKEN" \
        -H "Accept: application/json" \
        "$API_URL" 2>/dev/null || true)
    if [ "$code" = "200" ]; then
        echo "API is ready (HTTP 200 on /users/me)"
        exit 0
    fi
    sleep 1
    i=$((i + 1))
done

echo "Timed out waiting for Snipe-IT API. Last status: ${code:-000}."
compose_logs app
exit 1
