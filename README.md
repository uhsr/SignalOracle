# SignalOracle: Decentralized Data Aggregation for Smart Contracts

SignalOracle provides a secure and reliable mechanism for bringing off-chain data onto blockchain networks. This Python-based project facilitates the aggregation of data from multiple external sources, allowing smart contracts to make informed decisions based on real-world information. By employing a modular architecture and cryptographic verification techniques, SignalOracle ensures data integrity and resistance to manipulation, thereby enhancing the robustness and trustworthiness of decentralized applications.

This repository contains the core components for setting up and running a SignalOracle node. The project is designed to be flexible and adaptable, allowing developers to integrate it seamlessly into various blockchain ecosystems. SignalOracle aims to address the oracle problem by providing a decentralized, transparent, and auditable solution for data feeds. It leverages a combination of API polling, data normalization, and consensus mechanisms to deliver accurate and timely information to smart contracts. The system is designed to handle diverse data types, from financial market data to weather conditions, making it a versatile tool for a wide range of applications.

SignalOracle utilizes a layered approach to data acquisition and delivery. First, data is fetched from designated APIs based on predefined configurations. This data is then normalized and validated to ensure consistency and accuracy. The validated data is then aggregated from multiple sources, mitigating the risk of a single point of failure or data manipulation. Finally, the aggregated data is signed cryptographically and made available to smart contracts through a designated on-chain interface. The project is built with scalability in mind, allowing for the addition of new data sources and consensus mechanisms as the network grows.

## Key Features

*   **Decentralized Data Aggregation:** Employs a peer-to-peer network to aggregate data from multiple sources, reducing reliance on centralized oracles and mitigating single points of failure.
*   **Cryptographic Verification:** Utilizes digital signatures and hashing algorithms to ensure the integrity and authenticity of data, preventing manipulation and ensuring trust. Specifically, nodes sign the aggregated data using their private keys, allowing smart contracts to verify the data's origin using their corresponding public keys, registered on-chain.
*   **Configurable Data Sources:** Allows users to define custom data sources and data formats through configuration files, providing flexibility and adaptability to different data requirements. The configuration files specify the API endpoints, data parsing rules (using libraries such as `jsonpath_ng` or custom Python functions), and validation criteria for each data source.
*   **API Polling and Data Normalization:** Automatically polls specified APIs at regular intervals, normalizes the data into a consistent format, and performs data validation to ensure accuracy. Data normalization includes converting data types, standardizing units of measurement, and handling missing or erroneous data.
*   **On-Chain Data Delivery:** Provides a mechanism for delivering aggregated and verified data to smart contracts via a secure on-chain interface. This typically involves writing the data to a smart contract that acts as a data feed for other contracts. The project supports integration with various blockchain platforms, including Ethereum and Polygon.
*   **Modular Architecture:** Designed with a modular architecture that allows for easy extension and customization, enabling developers to add new data sources, consensus mechanisms, and blockchain integrations. The core components (data fetching, normalization, aggregation, and on-chain delivery) are decoupled and can be modified or replaced independently.

## Technology Stack

*   **Python:** The core programming language for the SignalOracle project, providing a versatile and widely supported platform for development.
*   **Requests:** A Python library for making HTTP requests to external APIs, facilitating data retrieval from various sources.
*   **JSON:** Used for parsing and manipulating data received from APIs.
*   **Cryptography:** Used for implementing cryptographic functions such as digital signatures and hashing, ensuring data integrity and security.
*   **Web3.py (or equivalent):** A Python library for interacting with blockchain networks, enabling on-chain data delivery. Provides the necessary tools to interact with smart contracts, send transactions, and retrieve data from the blockchain.
*   **Flask/FastAPI (Optional):** Used for creating an API endpoint for external applications to interact with the SignalOracle node.

## Installation

1.  Clone the repository:
    git clone https://github.com/uhsr/SignalOracle.git
    cd SignalOracle
2.  Create a virtual environment:
    python3 -m venv venv
3.  Activate the virtual environment:
    source venv/bin/activate
4.  Install the required dependencies:
    pip install -r requirements.txt
5.  Install your desired blockchain library(web3.py):
    pip install web3

## Configuration

1.  Create a `.env` file in the root directory.
2.  Define the following environment variables:
    *   `NODE_PRIVATE_KEY`: The private key of the SignalOracle node.
    *   `BLOCKCHAIN_RPC_URL`: The URL of the blockchain node (e.g., Infura, Alchemy).
    *   `CONTRACT_ADDRESS`: The address of the data feed smart contract.
    *   `DATA_SOURCES_CONFIG`: The path to the JSON file containing the data source configurations.

   A sample `DATA_SOURCES_CONFIG` file might look like this:
   {
   "source1": {
   "url": "https://api.example.com/data",
   "path": "$.price",
   "type": "float"
   },
   "source2": {
   "url": "https://anotherapi.com/data",
   "path": "$.value",
   "type": "int"
   }
   }

## Usage

1.  Run the SignalOracle node:
    python main.py

   This will start the node, which will periodically fetch data from the configured sources, aggregate it, sign it, and send it to the data feed smart contract.

   Example code snippet of updating blockchain:
   from web3 import Web3
   w3 = Web3(Web3.HTTPProvider(os.getenv("BLOCKCHAIN_RPC_URL")))
   contract = w3.eth.contract(address=os.getenv("CONTRACT_ADDRESS"), abi=CONTRACT_ABI)
   tx_hash = contract.functions.updateData(aggregated_data, signature).transact({'from': w3.eth.account.from_key(os.getenv("NODE_PRIVATE_KEY")).address})

   This code demonstrates how to use web3.py to interact with a smart contract to update the data. The `aggregated_data` and `signature` would be generated by the oracle's data aggregation and signing processes.

## Contributing

We welcome contributions to the SignalOracle project. Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write tests for your code.
4.  Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/SignalOracle/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to acknowledge the contributions of the open-source community to the development of this project.