#!/usr/bin/env python3
#
# Copyright Soramitsu Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
#


# Iroha python library consists of 3 parts: Iroha, IrohaCrypto and IrohaGrpc
import os
import binascii
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc
from iroha.primitive_pb2 import can_set_my_account_detail
from iroha import primitive_pb2
import sys

if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

# Connection to Iroha network. It uses the address and port of the node it wishes to send the transaction to.
IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '192.168.1.83')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')
#IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '201.137.130.149')
#IROHA_PORT = os.getenv('IROHA_PORT', '50051')
net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))

# Here we retrieve the admin@domain account created on the genesis block, we need it to create the iroha object for this account.
# os.getenv(par1, par2) gets the value of par1, if it doesnt exist, then it assigns the value of par2. This is why we use os.getenv insted of: ADMIN_ACCOUNT_ID = 'admin@domain'
ADMIN_ACCOUNT_ID = os.getenv('ADMIN_ACCOUNT_ID', 'admin@domain')

# This creates a new private key
# print(IrohaCrypto.private_key())
ADMIN_PRIVATE_KEY = os.getenv(
    'ADMIN_PRIVATE_KEY', 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70')

# The Iroha object allows us to use the Iroha library commands. Each account must have and use its own Iroha object
iroha = Iroha(ADMIN_ACCOUNT_ID)
print(iroha)

# Here we created a key with the IrohaCrypto.private_key() method and we will assign it to user as a default value for testing
# We are not creating any user here, just creating the keys.
# To create a user, only the public key is needed, the private key will only be used to sign transactions.
# print(IrohaCrypto.private_key())
user_private_key = os.getenv(
    'user_private_key', '622e124e078333c58c644f5d107ac8a5c0002aeee222104411355ab10fc0faa8')
user_private_key2 = os.getenv(
    'user_private_key2', '116eac80e88983cabb0b47bcf2be1c0a25222e6aa30ec43bd5dcc3144eaf4c60')
money_administrator_private_key = os.getenv(
    'money_administrator_private_key', '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4')

# The derived public key of a private key is always the same.
user_public_key = IrohaCrypto.derive_public_key(user_private_key)
user_public_key2 = IrohaCrypto.derive_public_key(user_private_key2)
money_administrator_public_key = IrohaCrypto.derive_public_key(money_administrator_private_key)

# -------------------------------------------------------------------------------------------
# The following functions are used for tracking.

def trace(func):
    """
    A decorator for tracing methods' begin/end execution points
    """

    def tracer(*args, **kwargs):
        name = func.__name__
        print('\tEntering "{}"'.format(name))
        result = func(*args, **kwargs)
        print('\tLeaving "{}"'.format(name))
        return result

    return tracer


@trace
def send_transaction_and_print_status(transaction):
    """
    Sends the transaction and prints its status.
    """
    hex_hash = binascii.hexlify(IrohaCrypto.hash(transaction))
    print('Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id))
    net.send_tx(transaction)
    for status in net.tx_status_stream(transaction):
        print(status)


# -------------------------------------------------------------------------------------------
# The following functions are used to implement the functionality.

@trace
def create_domain_and_asset(domainName, defaultRole, assetName, assetPrecision, irohaObject, signingPrivateKey):
    """
    Creates a domain with its default role, and an asset for this domain with a specified precision.
    """
    commands = [
        irohaObject.command('CreateDomain', domain_id=domainName,
                      default_role=defaultRole),
        irohaObject.command('CreateAsset', asset_name=assetName,
                      domain_id=domainName, precision=assetPrecision)
    ]
    tx = IrohaCrypto.sign_transaction(
        irohaObject.transaction(commands), signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def create_domain(domainName, defaultRole, irohaObject, signingPrivateKey):
    """
    Creates a domain with its default role.
    """
    commands = [
        irohaObject.command('CreateDomain', domain_id=domainName,
                      default_role=defaultRole)
    ]
    tx = IrohaCrypto.sign_transaction(
        irohaObject.transaction(commands), signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def create_asset(domainName, assetName, assetPrecision, irohaObject, signingPrivateKey):
    """
    Creates an asset for a specified domain with a specified precision.
    """
    commands = [
        irohaObject.command('CreateAsset', asset_name=assetName,
                      domain_id=domainName, precision=assetPrecision)
    ]
    tx = IrohaCrypto.sign_transaction(
        irohaObject.transaction(commands), signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def add_asset(assetId, quantity, irohaObject, signingPrivateKey):
    """
    Adds a certain quantity of units of the asset to the signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('AddAssetQuantity',
                      asset_id=assetId, amount=quantity)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def create_account(name, domainName, publicKey, irohaObject, signingPrivateKey):
    """
    Create an account and its Iroha object
    """
    tx = irohaObject.transaction([
        irohaObject.command('CreateAccount', account_name=name, domain_id=domainName,
                      public_key=publicKey)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)

    tempIroha = name + '_iroha'
    tempAccountId = name + '@' + domainName
    globals()[tempIroha] = Iroha(tempAccountId)


@trace
def create_role(roleName, permissionList, irohaObject, signingPrivateKey):
    """
    Create a role
    """
    tx = irohaObject.transaction([
        irohaObject.command('CreateRole', role_name=roleName,
                      permissions=permissionList)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def transfer_asset_from_account_one_to_account_two(accountOneId, accountTwoId, assetId, transactionDescription, quantity, irohaObject, signingPrivateKey):
    """
    Transfer a specific quantity of assets from account number one to account number two.
    """
    tx = irohaObject.transaction([
        irohaObject.command('TransferAsset', src_account_id=accountOneId, dest_account_id=accountTwoId,
                      asset_id=assetId, description=transactionDescription, amount=quantity)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def userone_grants_to_admin_set_account_detail_permission(grantingAccountId, grantedAccountId, irohaObject, signingPrivateKey):
    """
    Make an account able to set details of the signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('GrantPermission', account_id=grantedAccountId,
                      permission=can_set_my_account_detail)
    ], creator_account=grantingAccountId)
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def set_detail_to_account(accountId, objectKey, objectValue, irohaObject, signingPrivateKey):
    """
    Set age to an account by signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('SetAccountDetail',
                      account_id=accountId, key=objectKey, value=objectValue)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def set_role(accountId, roleName, irohaObject, signingPrivateKey):
    """
    Set a role to an account by a signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('AppendRole',
                      account_id=accountId, role_name=roleName)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)


@trace
def get_asset_info(assetId, irohaObject, signingPrivateKey):
    """
    Get all the information about an asset
    """
    query = irohaObject.query('GetAssetInfo', asset_id=assetId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.asset_response.asset
    print('Asset id = {}, precision = {}'.format(data.asset_id, data.precision))


@trace
def get_account_assets(accountId, irohaObject, signingPrivateKey):
    """
    List all the assets of an account
    """
    query = irohaObject.query('GetAccountAssets', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.account_assets_response.account_assets
    for asset in data:
        print('Asset id = {}, balance = {}'.format(
            asset.asset_id, asset.balance))


@trace
def get_roles(irohaObject, signingPrivateKey):
    """
    List all the roles
    """
    query = irohaObject.query('GetRoles')
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.roles_response.roles
    for role in data:
        print(role)


@trace
def get_role_permissions(roleName, irohaObject, signingPrivateKey):
    """
    List all the permissions for a role
    """
    query = irohaObject.query('GetRolePermissions', role_id=roleName)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.role_permissions_response.permissions
    for permission in data:
        print(permission)


@trace
def get_account_transactions(accountId, irohaObject, signingPrivateKey):
    """
    List all the transactions of the account. 
    It's important to remember that a transaction can be comprised by one or more commands.
    """
    query = irohaObject.query('GetAccountTransactions',
                        account_id=accountId, page_size=1)
    IrohaCrypto.sign_query(query, signingPrivateKey)
    response = net.send_query(query)
    if response.transactions_page_response.all_transactions_size == 0:
        print('There are no transactions for this account')
    else:
        print('tx_hash: {}'. format(response.transactions_page_response.next_tx_hash))
        print(response)

        while response.transactions_page_response.next_tx_hash:
            print('tx_hash: {}'. format(
                response.transactions_page_response.next_tx_hash))
            query = irohaObject.query('GetAccountTransactions', account_id=accountId,
                                page_size=1, first_tx_hash=response.transactions_page_response.next_tx_hash)
            IrohaCrypto.sign_query(query, signingPrivateKey)
            response = net.send_query(query)
            print(response)


@trace
def get_account_asset_transactions(accountId, assetId, irohaObject, signingPrivateKey):
    """
    List all the transactions of a particular asset for an account. 
    It's important to remember that a transaction can be comprised by one or more commands.
    """
    query = irohaObject.query('GetAccountAssetTransactions',
                        account_id=accountId, asset_id=assetId, page_size=1)
    IrohaCrypto.sign_query(query, signingPrivateKey)
    response = net.send_query(query)
    if response.transactions_page_response.all_transactions_size == 0:
        print('There are no transactions of this particular asset for this account')
    else:
        print('tx_hash: {}'. format(response.transactions_page_response.next_tx_hash))
        print(response)

        while response.transactions_page_response.next_tx_hash:
            print('tx_hash: {}'. format(
                response.transactions_page_response.next_tx_hash))
            query = irohaObject.query('GetAccountAssetTransactions', account_id=accountId, asset_id=assetId,
                                page_size=1, first_tx_hash=response.transactions_page_response.next_tx_hash)
            IrohaCrypto.sign_query(query, signingPrivateKey)
            response = net.send_query(query)
            print(response)


@trace
def get_transaction_data(transactionHash, irohaObject, signingPrivateKey):
    """
    List all the information of a transaction
    """
    query = irohaObject.query('GetTransactions', tx_hashes=transactionHash)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.transactions_response.transactions
    for transaction in data:
        print(transaction)


@trace
def get_transactions_data(transactionHashes, irohaObject, signingPrivateKey):
    """
    List all the information of multiple transactions
    """
    for tempHash in transactionHashes:
        hash = [str(tempHash)]
        query = irohaObject.query('GetTransactions', tx_hashes=hash)
        IrohaCrypto.sign_query(query, signingPrivateKey)
        response = net.send_query(query)
        print(response)


@trace
def get_account_details(accountId, irohaObject, signingPrivateKey):
    """
    Get all the kv-storage entries for an account
    """
    query = irohaObject.query('GetAccountDetail', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.account_detail_response
    print('Account id = {}, details = {}'.format(accountId, data.detail))


@trace
def get_account(accountId, irohaObject, signingPrivateKey):
    """
    Get account information.
    """
    query = irohaObject.query('GetAccount', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    print(response)


@trace
def add_peer(accountID, addressAndPort, key, irohaObject, signingPrivateKey):
    """
    Add a peer to the network
    """
    peer1 = primitive_pb2.Peer()
    peer1.address = addressAndPort
    peer1.peer_key = key
    tx = irohaObject.transaction([
            irohaObject.command('AddPeer', peer=peer1)
    ], creator_account=accountID, quorum=1)
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    send_transaction_and_print_status(tx)
    

@trace
def get_peers(accountID, irohaObject, signingPrivateKey):
    query = irohaObject.query('GetPeers', creator_account=accountID)
    IrohaCrypto.sign_query(query, signingPrivateKey)
    response = net.send_query(query)
    print(response)


# Command for adding a new peer
#add_peer('admin@domain', '201.137.130.149:10001', 'bddd58404d1315e0eb27902c5d7c8eb0602c16238f005773df406bc191308928', iroha, ADMIN_PRIVATE_KEY)
#get_peers('admin@domain', iroha, ADMIN_PRIVATE_KEY)

# Commands for creating the environment
print("Environment testing")
#Comando utilizado para crear un nuevo dominio y una moneda para este.
#create_domain_and_asset('domain', 'user', 'coin', 2, iroha, ADMIN_PRIVATE_KEY)
create_account('money_administrator', 'domain', money_administrator_public_key, iroha, ADMIN_PRIVATE_KEY)
set_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)
add_asset('sentli#domain', '1000.00', money_administrator_iroha, money_administrator_private_key)
get_account_assets('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
create_account('userone', 'domain', user_public_key, iroha, ADMIN_PRIVATE_KEY)
create_account('usertwo', 'domain', user_public_key2, iroha, ADMIN_PRIVATE_KEY)

# Commands for testing the interactions between the users
print("Transactions testing")
transfer_asset_from_account_one_to_account_two('money_administrator@domain', 'userone@domain', 'sentli#domain', 'Funding of the account userone', '2.00', money_administrator_iroha, money_administrator_private_key)
transfer_asset_from_account_one_to_account_two('money_administrator@domain', 'usertwo@domain', 'sentli#domain', 'Funding of the account usertwo', '2.00', money_administrator_iroha, money_administrator_private_key)
get_account_assets('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_assets('userone@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_assets('usertwo@domain', iroha, ADMIN_PRIVATE_KEY)
# userone_iroha and usertwo_iroha are Iroha objects that are created when the user is created. This is why they show up as currently inexistent.
transfer_asset_from_account_one_to_account_two('userone@domain', 'usertwo@domain', 'sentli#domain', 'Transfer of 1.00 from user 1 to user 2', '1.00', userone_iroha, user_private_key)
get_account_assets('userone@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_assets('usertwo@domain', iroha, ADMIN_PRIVATE_KEY)
transfer_asset_from_account_one_to_account_two('usertwo@domain', 'userone@domain', 'sentli#domain', 'Transfer of 1.00 from user 2 to user 1', '1.00', usertwo_iroha, user_private_key2)
get_account_assets('userone@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_assets('usertwo@domain', iroha, ADMIN_PRIVATE_KEY)

# Commands for general testing
print("Other testing")
userone_grants_to_admin_set_account_detail_permission('userone@domain', 'admin@domain', userone_iroha, user_private_key)
set_detail_to_account('userone@domain', 'age', '18', iroha, ADMIN_PRIVATE_KEY)
get_asset_info('sentli#domain', iroha, ADMIN_PRIVATE_KEY)
get_account_details('userone@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_asset_transactions('money_administrator@domain', 'sentli#domain', iroha, ADMIN_PRIVATE_KEY)
get_roles(iroha, ADMIN_PRIVATE_KEY)
get_role_permissions('admin', iroha, ADMIN_PRIVATE_KEY)
get_account_transactions('admin@domain', iroha, ADMIN_PRIVATE_KEY)
permissionList=[5, 6, 7, 9, 14]
create_role('paquish', permissionList, iroha, ADMIN_PRIVATE_KEY)
get_role_permissions('paquish', iroha, ADMIN_PRIVATE_KEY)
set_role('userone@domain', 'paquish', iroha, ADMIN_PRIVATE_KEY)
get_account('userone@domain', iroha, ADMIN_PRIVATE_KEY)
get_account('admin@domain', iroha, ADMIN_PRIVATE_KEY)
transactionHash=['dea3a36916fdf0709f5c19f554dfcae0853819f0904ff330f13d827ba6265a0f']
get_transaction_data(transactionHash, iroha, ADMIN_PRIVATE_KEY)
transactionHashes=['dea3a36916fdf0709f5c19f554dfcae0853819f0904ff330f13d827ba6265a0f',
                   '7c07ec86dd08e42d42f5880b2eeabc525d4b5943beb6434c30a0e6ce2c678cd0']
get_transactions_data(transactionHashes, iroha, ADMIN_PRIVATE_KEY)
create_account('userthree', 'domain', user_public_key, iroha, ADMIN_PRIVATE_KEY)
get_account_transactions('userthree@domain', iroha, ADMIN_PRIVATE_KEY)
get_account_asset_transactions('userthree@domain', 'sentli#domain', iroha, ADMIN_PRIVATE_KEY)
print('done')

##tests with the new functionalities
#cmd.create_account('money_administrator', 'domain', money_administrator_public_key, iroha, ADMIN_PRIVATE_KEY)
#cmd.set_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)
#cmd.get_account('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
#money_administrator_iroha = cmd.irohaObject('money_administrator@domain')
#cmd.add_asset('sentli#domain', '1000.00', money_administrator_iroha, money_administrator_private_key)
#cmd.get_account_assets('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
#cmd.substract_assets('sentli#domain', '1000.00', money_administrator_iroha, money_administrator_private_key)
#cmd.get_account_assets('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
#cmd.add_signatory('money_administrator@domain', user_public_key, money_administrator_iroha, money_administrator_private_key)
#cmd.get_signatories('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)
#cmd.detach_role('money_administrator@domain', 'money_creator', iroha, ADMIN_PRIVATE_KEY)
#cmd.get_account('money_administrator@domain', iroha, ADMIN_PRIVATE_KEY)