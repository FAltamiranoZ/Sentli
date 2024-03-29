# SPDX-License-Identifier: Apache-2.0
# Iroha python library consists of 3 parts: Iroha, IrohaCrypto and IrohaGrpc
import os
import binascii
from unittest import result
from iroha import IrohaCrypto
from iroha import Iroha, IrohaGrpc
from iroha.primitive_pb2 import can_set_my_account_detail
from iroha import primitive_pb2
import sys

if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '201.137.78.154')
#IROHA_HOST_ADDR = os.getenv('IROHA_HOST_ADDR', '127.0.0.1')
IROHA_PORT = os.getenv('IROHA_PORT', '50051')

net = IrohaGrpc('{}:{}'.format(IROHA_HOST_ADDR, IROHA_PORT))

# -------------------------------------------------------------------------------------------
# The following functions are used for tracking.


def irohaObject(idUsuario):
    """
    Returns the IrohaObject based on the user's id.
    """
    return Iroha(idUsuario)


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
    hashAndCreator = 'Transaction hash = {}, creator = {}'.format(
        hex_hash, transaction.payload.reduced_payload.creator_account_id)
    print(hashAndCreator)
    net.send_tx(transaction)
    statusVariable = ""
    for status in net.tx_status_stream(transaction):
        statusVariable = statusVariable + str(status) + "\n"
        print(status)
    return str(hashAndCreator) + "\n\n" + str(statusVariable)


# -------------------------------------------------------------------------------------------
# The following functions are used to implement the commands.

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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


@trace
def add_assets(assetId, quantity, irohaObject, signingPrivateKey):
    """
    Adds a certain quantity of units of the asset to the signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('AddAssetQuantity',
                      asset_id=assetId, amount=quantity)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    return send_transaction_and_print_status(tx)


@trace
def substract_assets(assetId, quantity, irohaObject, signingPrivateKey):
    """
    Substracts a certain quantity of units of the asset from the signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('SubtractAssetQuantity',
                      asset_id=assetId, amount=quantity)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    return send_transaction_and_print_status(tx)


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
    temp = send_transaction_and_print_status(tx)

    tempIroha = name + '_iroha'
    tempAccountId = name + '@' + domainName
    globals()[tempIroha] = Iroha(tempAccountId)
    return temp


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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


@trace
def detach_role(accountId, roleName, irohaObject, signingPrivateKey):
    """
    Detach a role from an account by a signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('DetachRole',
                      account_id=accountId, role_name=roleName)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    return send_transaction_and_print_status(tx)


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
    return send_transaction_and_print_status(tx)


@trace
def remove_peer(key, irohaObject, signingPrivateKey):
    """
    Removes a peer from the network
    """
    tx = irohaObject.transaction([
            irohaObject.command('RemovePeer', public_key=key)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    return send_transaction_and_print_status(tx)
    

@trace
def add_signatory(accountId, publicKey, irohaObject, signingPrivateKey):
    """
    Add a public key to an account by a signing account
    """
    tx = irohaObject.transaction([
        irohaObject.command('AddSignatory',
                      account_id=accountId, public_key=publicKey)
    ])
    IrohaCrypto.sign_transaction(tx, signingPrivateKey)
    return send_transaction_and_print_status(tx)


# -------------------------------------------------------------------------------------------
# The following functions are used to implement the queries.


@trace
def get_asset_info(assetId, irohaObject, signingPrivateKey):
    """
    Get all the information about an asset
    """
    query = irohaObject.query('GetAssetInfo', asset_id=assetId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.asset_response.asset
    result = 'Asset id = {}, precision = {}'.format(data.asset_id, data.precision)
    print(result)
    return result


@trace
def get_account_assets(accountId, irohaObject, signingPrivateKey):
    """
    List all the assets of an account
    """
    query = irohaObject.query('GetAccountAssets', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.account_assets_response.account_assets
    printableVariable = ""
    for asset in data:
        temp = 'Asset id = {}, balance = {}'.format(
            asset.asset_id, asset.balance)
        printableVariable = printableVariable + str(temp) + "\n"
    if(printableVariable == ""):
        printableVariable = "No hay activos disponibles para esta cuenta"
    print(printableVariable)
    return printableVariable


@trace
def get_roles(irohaObject, signingPrivateKey):
    """
    List all the roles
    """
    query = irohaObject.query('GetRoles')
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.roles_response.roles
    printableVariable = ""
    for role in data:
        printableVariable = printableVariable + str(role) + "\n"
        print(role)
    return printableVariable


@trace
def get_role_permissions(roleName, irohaObject, signingPrivateKey):
    """
    List all the permissions for a role
    """
    query = irohaObject.query('GetRolePermissions', role_id=roleName)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.role_permissions_response.permissions
    printableVariable = ""
    for permission in data:
        printableVariable = printableVariable + str(permission) + "\n"
        print(permission)
    return printableVariable


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
        print('Esta cuenta no ha realizado transacciones')
        return 'Esta cuenta no ha realizado transacciones'
    else:
        result = 'tx_hash: {}'. format(response.transactions_page_response.next_tx_hash)
        print(result)
        print(response)
        printableVariable = str(result) + "\n" + str(response) + "\n"
        while response.transactions_page_response.next_tx_hash:
            result2 = 'tx_hash: {}'. format(
                response.transactions_page_response.next_tx_hash)
            print(result2)
            printableVariable = printableVariable + str(result2) + "\n"
            query = irohaObject.query('GetAccountTransactions', account_id=accountId,
                                page_size=1, first_tx_hash=response.transactions_page_response.next_tx_hash)
            IrohaCrypto.sign_query(query, signingPrivateKey)
            response = net.send_query(query)
            print(response)
            printableVariable = printableVariable + str(response) + "\n"
        return printableVariable


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
        print('Esta cuenta no ha realizado transacciones con este activo')
        return 'Esta cuenta no ha realizado transacciones con este activo'
    else:
        result = 'tx_hash: {}'. format(response.transactions_page_response.next_tx_hash)
        print(result)
        print(response)
        printableVariable = str(result) + "\n" + str(response) + "\n"

        while response.transactions_page_response.next_tx_hash:
            result2 = 'tx_hash: {}'. format(
                response.transactions_page_response.next_tx_hash)
            print(result2)
            printableVariable = printableVariable + str(result2) + "\n"
            query = irohaObject.query('GetAccountAssetTransactions', account_id=accountId, asset_id=assetId,
                                page_size=1, first_tx_hash=response.transactions_page_response.next_tx_hash)
            IrohaCrypto.sign_query(query, signingPrivateKey)
            response = net.send_query(query)
            print(response)
            printableVariable = printableVariable + str(response) + "\n"
        return printableVariable


@trace
def get_transaction_data(transactionHash, irohaObject, signingPrivateKey):
    """
    List all the information of a transaction
    """
    query = irohaObject.query('GetTransactions', tx_hashes=transactionHash)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.transactions_response.transactions
    printableVariable = ""
    for transaction in data:
        print(transaction)
        printableVariable = printableVariable + str(transaction) + "\n"
    return printableVariable


@trace
def get_transactions_data(transactionHashes, irohaObject, signingPrivateKey):
    """
    List all the information of multiple transactions
    """
    printableVariable = ""
    for tempHash in transactionHashes:
        hash = [str(tempHash)]
        query = irohaObject.query('GetTransactions', tx_hashes=hash)
        IrohaCrypto.sign_query(query, signingPrivateKey)
        response = net.send_query(query)
        print(response)
        printableVariable = printableVariable + str(response) + "\n"
    return printableVariable


@trace
def get_account_details(accountId, irohaObject, signingPrivateKey):
    """
    Get all the kv-storage entries for an account
    """
    query = irohaObject.query('GetAccountDetail', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    data = response.account_detail_response
    result = 'Account id = {}, details = {}'.format(accountId, data.detail)
    print(result)
    return str(result)


@trace
def get_account(accountId, irohaObject, signingPrivateKey):
    """
    Get account information.
    """
    query = irohaObject.query('GetAccount', account_id=accountId)
    IrohaCrypto.sign_query(query, signingPrivateKey)

    response = net.send_query(query)
    print(response)
    return str(response)
    

@trace
def get_peers(accountID, irohaObject, signingPrivateKey):
    """
    List all the active nodes in the network.
    """
    query = irohaObject.query('GetPeers', creator_account=accountID)
    IrohaCrypto.sign_query(query, signingPrivateKey)
    response = net.send_query(query)
    print(response)
    return str(response)


@trace
def get_signatories(accountID, irohaObject, signingPrivateKey):
    """
    List all the signatories attached to an account.
    """
    query = irohaObject.query('GetSignatories', account_id=accountID)
    IrohaCrypto.sign_query(query, signingPrivateKey)
    response = net.send_query(query)
    print(response)
    return str(response)

