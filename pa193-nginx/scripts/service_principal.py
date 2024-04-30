from azure.identity import ClientSecretCredential, DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

credential = DefaultAzureCredential()

tenant_id="534a6433-58f7-45b2-aeb6-ad68da25732c"
client_id="FILL_ME"
client_secret="FILL_ME"

vault_url = "https://pa193-keyvault.vault.azure.net/"
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = SecretClient(vault_url=vault_url, credential=credential)


secrets = client.list_properties_of_secrets()
for secret in secrets:
    retrieved_secret = client.get_secret(secret.name)
    print(
        "Secret with name '{0}' and value {1} was found.".format(retrieved_secret.name, retrieved_secret.name)
    )
