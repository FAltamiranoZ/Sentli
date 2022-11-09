#Creamos las variables del entorno necesarias para el ejemplo
from iroha import IrohaCrypto
import Comandos as cmd

iroha = cmd.irohaObject('admin@domain')
ADMIN_PRIVATE_KEY = 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70'
pablo_private_key = '622e124e078333c58c644f5d107ac8a5c0002aeee222104411355ab10fc0faa8'
ivana_private_key = '116eac80e88983cabb0b47bcf2be1c0a25222e6aa30ec43bd5dcc3144eaf4c60'
money_administrator_private_key = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
pablo_public_key = IrohaCrypto.derive_public_key(pablo_private_key)
ivana_public_key = IrohaCrypto.derive_public_key(ivana_private_key)
money_administrator_public_key = IrohaCrypto.derive_public_key(money_administrator_private_key)
money_administrator_iroha = cmd.irohaObject('money_administrator@domain')
cmd.create_account('money_administrator', 'domain', money_administrator_public_key, iroha, ADMIN_PRIVATE_KEY)
money_administrator_iroha = cmd.irohaObject('money_administrator@domain')
cmd.create_account('ivana', 'domain', ivana_public_key, iroha, ADMIN_PRIVATE_KEY)
ivana_iroha = cmd.irohaObject('ivana@domain')

#Pablo crea su cuenta y confirmamos que se haya guardado la información
cmd.create_account('pablo', 'domain', pablo_public_key, iroha, ADMIN_PRIVATE_KEY)
cmd.userone_grants_to_admin_set_account_detail_permission('pablo@domain', 'admin@domain', pablo_iroha, pablo_private_key)
cmd.set_detail_to_account('pablo@domain', 'edad', '30', iroha, ADMIN_PRIVATE_KEY)
cmd.set_detail_to_account('pablo@domain', 'CURP', 'PORA950712EI1', iroha, ADMIN_PRIVATE_KEY)
cmd.set_detail_to_account('pablo@domain', 'email', 'pora30@gmail.com', iroha, ADMIN_PRIVATE_KEY)
cmd.set_detail_to_account('pablo@domain', 'codigoPostal', '05322', iroha, ADMIN_PRIVATE_KEY)
cmd.set_detail_to_account('pablo@domain', 'estado', 'Veracruz', iroha, ADMIN_PRIVATE_KEY)
cmd.set_detail_to_account('pablo@domain', 'municipio', 'Alvarado', iroha, ADMIN_PRIVATE_KEY)
cmd.get_account_details('pablo@domain', iroha, ADMIN_PRIVATE_KEY)

#Pablo abona dinero a su cuenta para conseguir 100 Sentli y confirmamos que la transferencia es correcta
cmd.transfer_asset_from_account_one_to_account_two('money_administrator@domain', 'pablo@domain', 'sentli#domain', 'Funding of the account Pablo', '100.00', money_administrator_iroha, money_administrator_private_key)
cmd.get_account_assets('pablo@domain', pablo_iroha, pablo_private_key)

#Pablo le paga a Ivana su fruta y confirmamos el nuevo balance en ambas cuentas
cmd.transfer_asset_from_account_one_to_account_two('pablo@domain', 'ivana@domain', 'sentli#domain', 'Pago de fruta', '74.00', pablo_iroha, pablo_private_key)
cmd.get_account_assets('pablo@domain', pablo_iroha, '622e124e078333c58c644f5d107ac8a5c0002aeee222104411355ab10fc0faa8')
cmd.get_account_assets('ivana@domain', ivana_iroha, '116eac80e88983cabb0b47bcf2be1c0a25222e6aa30ec43bd5dcc3144eaf4c60')





