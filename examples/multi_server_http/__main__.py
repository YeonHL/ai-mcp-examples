import click
from server.fastapi_server import app as fastapi_app
from server.fastmcp_server import app as fastmcp_app


@click.command()
@click.option("--host", default="0.0.0.0", help="서버 호스트 주소")
@click.option("--port", default=8000, help="서버 포트 번호")
def run_fastmcp_server(host: str, port: int) -> int:
    fastmcp_app.run(transport="streamable-http", host=host, port=port, path="/mcp")
    return 0


@click.command()
@click.option("--host", default="0.0.0.0", help="서버 호스트 주소")
@click.option("--port", default=8000, help="서버 포트 번호")
@click.option("--dev", is_flag=True, help="개발 모드 활성화 (reload=True, workers=1)")
@click.option("--workers", default=1, help="워커 프로세스 수 (개발 모드에서는 무시됨)")
def run_fastapi_server(host: str, port: int, dev: bool, workers: int) -> int:
    import uvicorn

    uvicorn.run(
        fastapi_app,
        host=host,
        port=port,
        reload=dev,
        workers=1 if dev else workers,
    )
    return 0


if __name__ == "__main__":
    run_fastmcp_server()
