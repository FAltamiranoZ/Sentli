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

cmd.create_account('money_administrator', 'domain', money_administrator_public_key, iroha, ADMIN_PRIVATE_KEY)
cmd.set_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)
cmd.create_account('userone', 'domain', user_public_key, iroha, ADMIN_PRIVATE_KEY)
cmd.create_account('usertwo', 'domain', user_public_key2, iroha, ADMIN_PRIVATE_KEY)