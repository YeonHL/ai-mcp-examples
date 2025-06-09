# Puppeteer MCP 서버 Stdio 배포 예제

## 주요 파일 설명

- `__main__.py`: 서버 실행 파일입니다. `uv`를 통해 실행할 수 있습니다.
- `fastmcp_server.py`: MCP 서버를 작성한 파일입니다.
- `server_test.py`: 서버 테스트를 위한 클라이언트 파일입니다.
- `transports.py`: Docker Stdio Transport를 구현한 파일입니다.
- `entrypoint.sh`: 컨테이너 빌드 시 Entrypoint가 되는 파일입니다.

## 컨테이너 배포

### 빌드

Docker로 빌드할 경우 아래 명령어로 이미지를 생성하세요:

```sh
docker build -f=Containerfile -t=puppeteer-mcp-server:latest .
```

### 실행

Docker로 실행할 경우 아래 명령어로 실행할 수 있습니다:

```
docker run -p 8000:8000 --name puppeteer-mcp-server --privileged puppeteer-mcp-server:latest
```

- `--privileged`는 컨테이너 내에서 Docker 호출을 위해 필요합니다.
