# 여러 MCP 서버 Streamable HTTP 배포 예제

## 주요 파일 설명

- `puppeteer`: Puppeteer MCP 서버를 위한 폴더입니다. 로컬로 배포할 때와 컨테이너로 배포할 때의 내부 `server.py` 파일의 인자가 다릅니다.
- `server`: 각 서버 형태를 구현한 폴더입니다.
- `shared`: 하위 MCP 서버가 공유할 파일을 저장하는 폴더입니다.
- `__main__.py`: 서버 실행 파일입니다. `uv`를 통해 실행할 수 있으며 `if __name__ == "__main__":` 부분에 원하는 형태의 서버로 설정할 수 잇습니다.
- `server_test.py`: 서버 테스트를 위한 클라이언트 파일입니다.
- `entrypoint.sh`: 컨테이너 빌드 시 Entrypoint가 되는 파일입니다.

## 컨테이너 배포

### 빌드

Docker로 빌드할 경우 아래 명령어로 이미지를 생성하세요:

```sh
docker build -f=Containerfile -t=multi-mcp-server-http:latest .
```

### 실행

Docker로 실행할 경우 아래 명령어로 실행할 수 있습니다:

```
docker run -p 8000:8000 --name multi-mcp-server-http --privileged multi-mcp-server-http:latest
```

- `--privileged`는 컨테이너 내에서 Docker 호출을 위해 필요합니다.
