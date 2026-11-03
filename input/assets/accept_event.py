def accept_event(tx, tenant_id, event_id, digest, payload):
    # Pseudocode: the adapter must handle concurrent unique conflicts.
    with tx.atomic():
        previous = tx.find_event(tenant_id, event_id)
        if previous is not None:
            if previous.digest != digest:
                return {"status": 409, "outcome": "conflict"}
            return previous.response
        response = {"status": 201, "event_id": event_id}
        tx.insert_event(tenant_id, event_id, digest, response)
        tx.insert_outbox(tenant_id, event_id, payload)
        return response
