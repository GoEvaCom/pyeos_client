# pyeos_client

[![Documentation Status](https://readthedocs.org/projects/pyeos-client/badge/?version=latest)](http://pyeos-client.readthedocs.io/en/latest/?badge=latest)

This is a non official python library build around the eosd Chain & Wallet RPC API.
This library will allow you to easily interact with EOSIO node through REST API.

## Installation
~~~
 pip install pyeos-client
~~~

## Getting Started
```python
from pyeos_client.NodeosConnect import RequestHandlerAPI
from pyeos_client.EOSChainApi import ChainAPI



connection  = RequestHandlerAPI(base_url='http://nodeos-server:8888', headers={"Accept": "application/json"})
chainapi = ChainAPI(connection)
print(chainapi.get_info().json())
```
###### results

~~~
{
  "server_version": "b2eb1667",
  "head_block_num": 259590,
  "last_irreversible_block_num": 259573,
  "head_block_id": "0003f60677f3707f0704f16177bf5f007ebd45eb6efbb749fb1c468747f72046",
  "head_block_time": "2017-12-10T17:05:36",
  "head_block_producer": "initp",
  "recent_slots": "1111111111111111111111111111111111111111111111111111111111111111",
  "participation_rate": "1.00000000000000000"
}
~~~

#### Authors

- [@Merouane_Benth](https://twitter.com/Merouane_Benth)

#### License
This project is licensed under the MIT License - see the LICENSE file for details

## Official documentation
 - [RPC Interface EOS](https://eosio.github.io/eos/group__eosiorpc.html#v1walletlock)
 - [Library documentation](https://pyeos-client.readthedocs.io)

### Contributing

- Fork it (https://github.com/EvaCoop/pyeos_client.git)
- Create your feature branch (git checkout -b feature/fooBar)
- Commit your changes (git commit -am 'Add some fooBar')
- Push to the branch (git push origin feature/fooBar)
- Create a new Pull Request