"""Verifica as rotas HTTP do exercício contra uma instância recém-iniciada."""
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, build_opener, ProxyHandler

BASE_URL = "http://localhost:5206"
opener = build_opener(ProxyHandler({}))
results = []


def check(method, path, expected_status, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    request = Request(BASE_URL + path, data=data, method=method)
    request.add_header("Accept", "application/json")
    if data is not None:
        request.add_header("Content-Type", "application/json")
    try:
        response = opener.open(request, timeout=10)
    except HTTPError as error:
        response = error
    with response:
        status = response.code
        raw_body = response.read().decode("utf-8")
        payload = json.loads(raw_body) if raw_body else None
        location = response.headers.get("Location")
    assert status == expected_status, (method, path, status, payload)
    results.append({
        "method": method, "path": path, "status": status,
        "response": payload, "location": location, "passed": True,
    })
    print(f"PASS {method} {path}: {status}")
    return payload, location


def main():
    weather, _ = check("GET", "/weatherforecast", 200)
    assert len(weather) == 5
    pizzas, _ = check("GET", "/pizza", 200)
    assert len(pizzas) == 2
    pizza, _ = check("GET", "/pizza/1", 200)
    assert pizza["name"] == "Classic Italian"
    check("GET", "/pizza/99999", 404)

    created, location = check("POST", "/pizza", 201, {
        "name": "Hawaii", "isGlutenFree": False,
    })
    pizza_id = created["id"]
    assert location and location.endswith(f"/Pizza/{pizza_id}")
    retrieved, _ = check("GET", f"/pizza/{pizza_id}", 200)
    assert retrieved == created

    updated = {"id": pizza_id, "name": "Hawaii sem gluten", "isGlutenFree": True}
    check("PUT", f"/pizza/{pizza_id}", 204, updated)
    retrieved, _ = check("GET", f"/pizza/{pizza_id}", 200)
    assert retrieved == updated

    check("PUT", f"/pizza/{pizza_id}", 400, {
        "id": pizza_id + 1, "name": "ID divergente", "isGlutenFree": False,
    })
    check("PUT", "/pizza/99999", 404, {
        "id": 99999, "name": "Inexistente", "isGlutenFree": False,
    })
    check("DELETE", f"/pizza/{pizza_id}", 204)
    check("GET", f"/pizza/{pizza_id}", 404)
    check("DELETE", f"/pizza/{pizza_id}", 404)
    check("GET", "/pizza/abc", 400)

    report = {
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "base_url": BASE_URL, "sdk": "10.0.300", "framework": "net10.0",
        "checks_passed": len(results), "results": results,
    }
    output = Path(__file__).parent / "evidencias" / "verificacao-api.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(results)} verificações passaram. Relatório: {output}")


if __name__ == "__main__":
    main()

