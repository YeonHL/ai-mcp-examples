#!/bin/sh
echo "Starting entrypoint.sh"

IMAGE_LIST="mcp/puppeteer"

if [ -f "/usr/local/bin/entrypoint.sh" ]; then
    echo "Running entrypoint.sh in background..."
    /usr/local/bin/entrypoint.sh &
    sleep 5

    echo "Pulling specified Docker images..."
    for IMAGE in $IMAGE_LIST; do
        echo "Pulling image: $IMAGE"
        docker pull "$IMAGE"
        if [ $? -ne 0 ]; then
            echo "Warning: Failed to pull image $IMAGE"
            # 필요한 경우 여기서 오류 처리 (예: 스크립트 종료)
        fi
    done
else
    echo "entrypoint.sh not found at /usr/local/bin/. Assuming it's already running or not needed to be explicitly started here."
fi

echo "Starting uv application in background..."
uv run "$@"
