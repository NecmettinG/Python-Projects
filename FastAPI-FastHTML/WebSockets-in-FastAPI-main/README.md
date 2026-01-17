# WebSockets-in-FastAPI

This repository demonstrates the implementation of WebSockets in a FastAPI application. It includes examples of managing WebSocket connections, broadcasting messages, and handling real-time communication.

## Features

- **WebSocket Connection Management**: Handle multiple WebSocket connections efficiently.
- **Broadcasting Messages**: Send messages to all connected clients in real-time.
- **FastAPI Integration**: Leverage the power of FastAPI for building WebSocket-based applications.

## Files in the Repository

- `WebSocket.py`: Contains the main implementation of WebSocket connection management and broadcasting.
- `index.html`: A simple HTML file to test WebSocket connections.
- `mermaid.md`: A Mermaid diagram representing the `ConnectionManager` class and its methods.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (for running the FastAPI application)

## Installation

1. Clone the repository:
bash
git clone https://github.com/DrMohammedhbi/WebSockets-in-FastAPI.git
cd WebSockets-in-FastAPI
2. Create a virtual environment and activate it:
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
bash
pip install fastapi uvicorn

## Usage

1. Run the FastAPI application:
   https://www.youtube.com/watch?v=CdENaxFNQiY
   
bash
uvicorn WebSocket:app --reload
3. Open `index.html` in your browser to test the WebSocket functionality.

4. Use the WebSocket client to send and receive messages in real-time.

## How It Works

- The `ConnectionManager` class in `WebSocket.py` manages active WebSocket connections.
- Clients can connect to the WebSocket endpoint, and messages can be broadcasted to all connected clients.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.


## Contact

For any questions or suggestions, feel free to reach out to the repository owner.

---

Happy coding!
