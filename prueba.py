from web3 import Web3,EthereumTesterProvider
import solcx
import json
import pv


web3 = Web3(Web3.HTTPProvider("https://polygon-mumbai.infura.io/v3/75e8f476b65c449f92055cc1d25a2404"))

with open("mamut.sol","r") as f:
    archivo = f.read()


compiled_solidity = solcx.compile_standard({
    "language":"Solidity",
    "sources": {"mamut.sol":{
        "content":archivo
    }},
    "settings": {
        "outputSelection": {
            "*": {"*":
            ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    }
}, solc_version = "0.8.12")

with open("compiled_json.json", "w") as file:
    json.dump(compiled_solidity,file)

abi = compiled_solidity["contracts"]["mamut.sol"]["mamut"]["abi"]
bytecode = compiled_solidity["contracts"]["mamut.sol"]["mamut"]["evm"]["bytecode"]["object"]

NFT= web3.eth.contract(abi = abi,bytecode = bytecode)
MyWallet = "0xBa4d7EcA65E4CBAA6E400bAdB123c30909f14999"
transaction_hash = NFT.constructor().transact()
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
print(transaction_hash)



















'''nonce = web3.eth.get_transaction_count(MyWallet)

transaction = SimpleNumbere.constructor().build_transaction(
    {
        "gasPrice": web3.eth.gas_price,
        "chainId": 80001,
        "from": MyWallet,
        "nonce": nonce,
    }

)
signed_transaction = web3.eth.account.sign_transaction(transaction,private_key = pv.pv)
transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)

contract_instance = web3.eth.contract(address = transaction_receipt.contractAddress, abi = abi)
update_number_transaction= contract_instance.functions.updateStoredNumber(9).build_transaction(
    {
        "gasPrice": web3.eth.gas_price,
        "chainId": 80001,
        "from": MyWallet,
        "nonce": nonce + 1,
    }
)
signed_transaction = web3.eth.account.sign_transaction(update_number_transaction,private_key = pv.pv)
transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)


print(contract_instance.functions.getStoredNumber().call())'''