# SafeAPIPython
Example of querying the Safe API using Python

Uses https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/ to count the number of
“WalletConnect transactions” made with this Safe.
“WalletConnect transactions” are those that contain the word “WalletConnect” in the “origin” field of the response. A description of the return data form can be
found here: endpoint. It’s the endpoint called “safes_multisig-transactions_list”.
