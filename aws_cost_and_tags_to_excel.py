import boto3
import pandas as pd
from datetime import datetime, timedelta

# Substitua pelos valores das suas credenciais temporárias
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_session_token = 'YOUR_SESSION_TOKEN'

# Inicializa o cliente do Cost Explorer com as credenciais temporárias
ce_client = boto3.client(
    'ce',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Inicializa o cliente do Resource Groups Tagging API com as credenciais temporárias
tagging_client = boto3.client(
    'resourcegroupstaggingapi',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# Define o período de tempo (últimos 30 dias)
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

# Obtém os custos por recurso
response = ce_client.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='MONTHLY',
    Metrics=['BlendedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'RESOURCE_ID'
        },
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        }
    ]
)

# Inicializa a lista para armazenar os dados
data = []

# Processa cada recurso
for result in response['ResultsByTime'][0]['Groups']:
    resource_id = result['Keys'][0]
    service_name = result['Keys'][1]
    cost = result['Metrics']['BlendedCost']['Amount']

    # Obtém as tags do recurso
    tags_response = tagging_client.get_resources(
        ResourceARNList=[resource_id]
    )

    tags = tags_response['ResourceTagMappingList'][0]['Tags'] if tags_response['ResourceTagMappingList'] else []

    # Formata as tags em um único string
    tags_str = ', '.join([f"{tag['Key']}={tag['Value']}" for tag in tags])

    # Adiciona os dados à lista
    data.append({
        'Resource ID': resource_id,
        'Service': service_name,
        'Tags': tags_str,
        'Cost ($)': cost
    })

# Cria um DataFrame a partir dos dados
df = pd.DataFrame(data)

# Salva o DataFrame em uma planilha Excel
output_file = 'aws_cost_per_resource.xlsx'
df.to_excel(output_file, index=False)

print(f"Planilha gerada: {output_file}")
