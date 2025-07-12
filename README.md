# SignalOracle: Decentralized Crypto-Price Anomaly Detection

SignalOracle is a serverless, decentralized system for detecting and reporting anomalous crypto-price movements in real-time. It leverages WebSockets for price data ingestion, Bloom filters for efficient anomaly detection, and on-chain data oracles to trigger notifications based on predefined thresholds and deviation metrics. The system aims to provide a robust and trustless alternative to centralized anomaly detection services.

The project utilizes a combination of off-chain computation and on-chain verification to achieve its goals. Real-time price data from various cryptocurrency exchanges is streamed via WebSockets and processed by anomaly detection algorithms. These algorithms identify significant deviations from expected price behavior based on historical data and user-defined parameters. When an anomaly is detected, a notification trigger is generated. This trigger, along with relevant price data, is then submitted to a smart contract on a blockchain, enabling on-chain verification and event logging, ensuring transparency and preventing manipulation. The system is designed to be serverless, leveraging cloud functions for computation, minimizing infrastructure costs and maximizing scalability.

SignalOracle differentiates itself by prioritizing decentralization and transparency. By verifying anomaly detections on-chain, we eliminate the reliance on trusted third parties and provide verifiable proof of price anomalies. This approach is particularly valuable for decentralized finance (DeFi) applications where reliable and unbiased price data is crucial. Furthermore, the serverless architecture allows for easy deployment and maintenance, while the use of Bloom filters enables efficient anomaly detection without storing large amounts of historical data, optimizing resource utilization. The system's modular design allows for easy integration of new cryptocurrency exchanges, anomaly detection algorithms, and notification mechanisms.

The primary benefit of using SignalOracle is its ability to provide reliable, decentralized, and verifiable crypto-price anomaly detection. This information can be used by traders, DeFi protocols, and other applications to mitigate risk, identify arbitrage opportunities, and improve decision-making.

## Key Features

*   **Real-time Price Data Ingestion:** Uses WebSockets to consume live price feeds from multiple cryptocurrency exchanges (e.g., Binance, Coinbase) in JSON format.
*   **Bloom Filter-Based Anomaly Detection:** Implements Bloom filters to efficiently identify price deviations from expected ranges. The filter parameters (e.g., false positive rate, filter size) are configurable.
*   **Configurable Anomaly Thresholds:** Allows users to define custom thresholds for price deviations based on percentage change, standard deviation, or other metrics. These thresholds are stored in a configuration file and can be updated dynamically.
*   **On-Chain Verification:** Submits anomaly detection triggers and relevant price data to a smart contract on a specified blockchain (e.g., Ethereum, Polygon). The smart contract verifies the data and emits an event if the anomaly is confirmed.
*   **Serverless Architecture:** Deployed as a collection of cloud functions (e.g., AWS Lambda, Google Cloud Functions) for cost-effectiveness and scalability.
*   **Flexible Notification System:** Supports multiple notification channels, including email, SMS, and Webhooks. Notifications are triggered by on-chain events.
*   **Modular Design:** Allows for easy integration of new cryptocurrency exchanges, anomaly detection algorithms, and notification mechanisms. The system is designed with interfaces and abstract classes to promote code reusability and extensibility.

## Technology Stack

*   **Python:** The core programming language used for the project's logic and algorithms.
*   **WebSockets:** Used for real-time data streaming from cryptocurrency exchanges. The `websockets` library is used for handling WebSocket connections.
*   **Bloom Filters:** Employed for efficient anomaly detection. The `pybloomfiltermmap` library is used for creating and managing Bloom filters.
*   **Solidity:** Used for writing the smart contract that verifies anomaly detections on-chain.
*   **Web3.py:** A Python library for interacting with Ethereum-compatible blockchains. Used for submitting transactions to the smart contract.
*   **Cloud Functions (AWS Lambda/Google Cloud Functions):** Used for deploying the system as a serverless application.
*   **Environment Variables:** Used for storing sensitive information such as API keys and blockchain credentials.

## Installation

1.  Clone the repository:

    `git clone https://github.com/uhsr/SignalOracle.git`

2.  Navigate to the project directory:

    `cd SignalOracle`

3.  Create a virtual environment:

    `python3 -m venv venv`

4.  Activate the virtual environment:

    `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)

5.  Install the required dependencies:

    `pip install -r requirements.txt`

6.  Install the solidity compiler:
    `npm install -g solc`

7.  Compile and deploy the Solidity smart contract to your desired blockchain network. Make sure to configure the `web3.py` provider with the correct network endpoint and account credentials.

## Configuration

The system relies on environment variables for configuration. Create a `.env` file in the project root and add the following variables:



`EXCHANGE_API_KEY` and `EXCHANGE_API_SECRET` are the API credentials for your chosen cryptocurrency exchange. `BLOOM_FILTER_SIZE` and `BLOOM_FILTER_FALSE_POSITIVE_RATE` control the Bloom filter's performance. `ANOMALY_THRESHOLD_PERCENTAGE` defines the percentage change that triggers an anomaly alert. `BLOCKCHAIN_NETWORK_ENDPOINT` is the URL of the blockchain node (e.g., Infura, Alchemy). `BLOCKCHAIN_PRIVATE_KEY` is the private key of the account that will submit transactions to the smart contract. `CONTRACT_ADDRESS` is the address of the deployed smart contract.

## Usage

1. Run the data ingestion script to start streaming price data:

   `python data_ingestion.py`

2. Run the anomaly detection script to identify and report anomalies:

   `python anomaly_detection.py`

These scripts will connect to the configured cryptocurrency exchange, ingest real-time price data, and identify anomalies based on the defined thresholds and Bloom filter. When an anomaly is detected, a transaction will be submitted to the smart contract on the blockchain, triggering the appropriate notifications.

## Contributing

We welcome contributions to SignalOracle! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Ensure your code adheres to PEP 8 style guidelines.
*   Write unit tests for any new code.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/SignalOracle/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to acknowledge the contributions of the open-source community to the libraries and tools used in this project. Special thanks to the developers of `websockets`, `pybloomfiltermmap`, and `web3.py`.