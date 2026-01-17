# WebSocket Chat Application Architecture

```mermaid
sequenceDiagram
    participant Client as Chat Client (chat.html)
    participant Server as WebSocket Server (WebSocket.py)
    participant Manager as Connection Manager

    Note over Client,Server: Connection Establishment
    Client->>Server: WebSocket Connection Request
    Server->>Manager: Connect(websocket)
    Manager-->>Server: Add to active_connections
    Server-->>Client: Connection Accepted

    Note over Client,Server: Normal Message Flow
    Client->>Server: Send Message
    Server->>Server: Parse JSON Message
    Server->>Server: Add timestamp & client_id
    Server->>Manager: Broadcast Message
    Manager-->>Client: Send to all connected clients

    Note over Client,Server: Disconnect Handling
    Client->>Server: Connection Closed
    Server->>Manager: Disconnect(websocket)
    Manager-->>Server: Remove from active_connections
    Server->>Manager: Broadcast disconnect message
    Manager-->>Client: Notify other clients

```

```mermaid
graph TB
    subgraph Client Side
        A[Chat Interface] -->|User Input| B[WebSocket Client]
        B -->|Display Messages| A
    end

    subgraph Server Side
        C[FastAPI Server] -->|Manages| D[Connection Manager]
        D -->|Broadcasts| C
        C -->|Handles| E[WebSocket Endpoints]
    end

    B <-->|WebSocket Protocol| E

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#dfd,stroke:#333,stroke-width:2px
    style D fill:#fdd,stroke:#333,stroke-width:2px
    style E fill:#ddf,stroke:#333,stroke-width:2px
```

```mermaid
classDiagram
    class ConnectionManager {
        - List~WebSocket~ active_connections
        - int connection_count
        + __init__()
        + connect(websocket: WebSocket)
        + disconnect(websocket: WebSocket)
        + broadcast(message: str)
    }

    class WebSocket {
        + accept()
        + send_text(message: str)
    }

    ConnectionManager --> WebSocket : uses
```

```mermaid
classDiagram
    class ConnectionManager {
        +List[WebSocket] active_connections
        +int connection_count
        +connect(websocket)
        +disconnect(websocket)
        +broadcast(message)
    }

    class FastAPI {
        +get("/")
        +websocket("/ws/{client_id}")
    }

    class WebSocketEndpoint {
        +websocket_endpoint(websocket, client_id)
        +handle_message(data)
        +handle_disconnect()
    }

    class ChatClient {
        +WebSocket connection
        +String clientId
        +connect()
        +sendMessage(message)
        +displayMessage(data)
        +handleDisconnect()
    }

    FastAPI --> ConnectionManager : uses
    FastAPI --> WebSocketEndpoint : defines
    WebSocketEndpoint --> ConnectionManager : uses
    ChatClient --> WebSocketEndpoint : connects to