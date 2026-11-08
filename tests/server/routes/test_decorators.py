"""Tests for route handler decorators."""

from aiohttp import web

from supernote.server.routes.decorators import interactive_session_only, public_route


def test_route_decorators_set_handler_attributes() -> None:
    """Verify @public_route and @interactive_session_only attach declarative attributes."""

    @public_route
    async def open_handler(request: web.Request) -> web.StreamResponse:
        return web.Response(text="ok")

    @interactive_session_only
    async def session_handler(request: web.Request) -> web.StreamResponse:
        return web.Response(text="ok")

    assert getattr(open_handler, "is_public", False) is True
    assert getattr(open_handler, "interactive_session_only", False) is False

    assert getattr(session_handler, "interactive_session_only", False) is True
    assert getattr(session_handler, "is_public", False) is False
