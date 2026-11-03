# Appendix B. Technical Listings and Reproduction Material


The following extracts supplemented the transaction-boundary discussion in Chapter 5. They demonstrated several ICT document forms without claiming to compose a runnable service.

All addresses, image names and identifiers were examples. The thesis pipeline displayed the listings but did not execute the deployment or load commands.

## Payload, Client and Deployment Examples


The payload carried a tenant-scoped logical identity and simple event content. The JavaScript client retained the same event ID for a replay; generating a new ID for each attempt would evade the intended deduplication boundary.

The configuration illustrated where telemetry and database endpoints would be supplied. It omitted credentials, health checks and production hardening and therefore was not a deployable manifest.

```json caption="Illustrative event payload."
{
  "tenant_id": "campus-demo",
  "event_id": "E42",
  "event_type": "equipment.ready",
  "payload": {"device_id": "demo-7"}
}
```

```javascript caption="Client extract preserving logical event identity."
async function submitEvent(event) {
  const response = await fetch("/events", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(event)
  });
  return {status: response.status, body: await response.json()};
}
```

```yaml caption="Illustrative service configuration; example image only."
services:
  api:
    image: example.invalid/campus-events:demo
    environment:
      DB_HOST: database
      OTEL_SERVICE_NAME: campus-events-demo
  database:
    image: postgres:18
```

The client extract omitted retry timing and authentication. The deployment fragment only illustrated configuration syntax and did not contain the service implementation or database initialization.

## Protocol and Additional Language Boundaries


A real reproduction protocol would pin all revisions, validate the environment and archive raw output. The Bash extract showed command structure only; the referenced benchmark program was hypothetical and was not included or executed.

The Java and C++ extracts illustrated a shared boundary rule for nonempty event identifiers. They were optional interoperability examples rather than independently evaluated components of the artifact.

```bash caption="Unexecuted reproduction command structure."
# Illustrative only: benchmark program is not supplied.
docker compose up -d
curl --fail http://localhost:8080/health
python benchmark.py --seed 42 --events 1000 --retries 200
# Archive raw results and check database invariants separately.
```

```java caption="Optional Java identifier boundary example."
public boolean validEventId(String eventId) {
    return eventId != null && !eventId.trim().isEmpty();
}
```

```cpp caption="Optional edge-client identifier boundary example."
#include <string>
bool valid_event_id(const std::string& id) {
    return id.find_first_not_of(" ") != std::string::npos;
}
```

The two identifier checks were intentionally minimal and did not establish equivalent Unicode whitespace handling or a full validation policy. A real interoperability claim would require a shared specification and boundary tests.
