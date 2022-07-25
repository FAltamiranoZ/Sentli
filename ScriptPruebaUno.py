from iroha import IrohaCrypto
import Comandos as cmd

iroha = cmd.irohaObject('admin@domain')
ADMIN_PRIVATE_KEY = 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70'
user_private_key = '622e124e078333c58c644f5d107ac8a5c0002aeee222104411355ab10fc0faa8'
user_private_key2 = '116eac80e88983cabb0b47bcf2be1c0a25222e6aa30ec43bd5dcc3144eaf4c60'
money_administrator_private_key = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
user_public_key = IrohaCrypto.derive_public_key(user_private_key)
user_public_key2 = IrohaCrypto.derive_public_key(user_private_key2)
money_administrator_public_key = IrohaCrypto.derive_public_key(money_administrator_private_key)

# A continuación se ejecutarán todas los comandos y consultas disponibles en el sistema, para comprobar el correcto funcionamiento de cada una de ellas.
print('\n Testing create_account command: \n')
cmd.create_account('money_administrator', 'domain', money_administrator_public_key, iroha, ADMIN_PRIVATE_KEY)
money_administrator_iroha = cmd.irohaObject('money_administrator@domain')

print('\n Testing set_role command \n')
cmd.set_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing detach_role command \n')
cmd.detach_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)

print('\n Variable setting for testing \n')
cmd.set_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)
cmd.create_account('userone', 'domain', user_public_key, iroha, ADMIN_PRIVATE_KEY)
cmd.create_account('usertwo', 'domain', user_public_key2, iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_roles query \n')
cmd.get_roles(iroha, ADMIN_PRIVATE_KEY)

print('\n Testing set_detail_to_account command \n')
cmd.set_detail_to_account('userone@domain', 'age', '18', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_account_details query \n')
cmd.get_account_details('userone@domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing create_domain command \n')
cmd.create_domain('testDomain','user', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing create_asset command \n')
cmd.create_asset('testDomain', 'testcoin', 2, iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_asset_info query \n')
cmd.get_asset_info('testCoin@testDomain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_account_transactions query \n')
cmd.get_account_transactions('admin@domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing add_assets command \n')
cmd.add_assets('sentli#domain', '1000.00', money_administrator_iroha, money_administrator_private_key)

print('\n Testing transfer_asset_from_account_one_to_account_two command \n')
cmd.transfer_asset_from_account_one_to_account_two('money_administrator@domain', 'userone@domain', 'sentli#domain', 'Funding of the account userone', '2.00', money_administrator_iroha, money_administrator_private_key)

print('\n Testing get_account_assets query \n')
cmd.get_account_assets('userone@domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_account_asset_transactions query \n')
cmd.get_account_asset_transactions('money_administrator@domain', 'sentli#domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing add_signatory command \n')
cmd.add_signatory('money_administrator@domain', user_public_key, money_administrator_iroha, money_administrator_private_key)

print('\n Testing get_signatories query \n')
cmd.get_signatories('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_transaction_data query \n')
transactionHash=['5c019229bb83602acf1db3973079d0d1f774b1573bd0c0f2451551c388ad9e75']
cmd.get_transaction_data(transactionHash, iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_transactions_data query \n')
transactionHashes=['5c019229bb83602acf1db3973079d0d1f774b1573bd0c0f2451551c388ad9e75',
                   '121a45cea5b7310895c17e4988634b4aee308f1ec3a3413cff060baeb95edcb8']
cmd.get_transactions_data(transactionHashes, iroha, ADMIN_PRIVATE_KEY)

print('\n Testing add_peer command \n')
cmd.add_peer('admin@domain', '201.137.130.149:10001', 'bddd58404d1315e0eb27902c5d7c8eb0602c16238f005773df406bc191308928', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing get_peers query \n')
cmd.get_peers('admin@domain', iroha, ADMIN_PRIVATE_KEY)

print('\n Testing remove_peer command \n')
cmd.remove_peer('bddd58404d1315e0eb27902c5d7c8eb0602c16238f005773df406bc191308928', iroha, ADMIN_PRIVATE_KEY)




