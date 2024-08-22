# AWS Cost Tag Analyzer

This project is a Python script that retrieves detailed cost information from AWS services, including tags associated with each resource. The data is then exported to an Excel spreadsheet for easy analysis and reporting.

## Features

- Retrieves cost information for each AWS resource.
- Includes tags and associated values for each resource.
- Exports data to an Excel spreadsheet with columns for resource name, service, tags, and total cost.

## Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate permissions.
- AWS `boto3` library
- `pandas` library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/fabianomonteiro/aws-cost-tag-analyzer.git
   cd aws-cost-tag-analyzer
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### AWS Authentication

This script uses AWS Access Key, Secret Key, and Session Token for authentication. Ensure you have these credentials available. You can set them directly in the script:

```python
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_session_token = 'YOUR_SESSION_TOKEN'
```

### Permissions

Ensure that the AWS user or role has the necessary permissions:

- `ce:GetCostAndUsage`
- `tag:GetResources`

You can configure your AWS CLI with the following command:

```bash
aws configure
```

## Usage

1. Run the script to generate the Excel report:

   ```bash
   python aws_cost_and_tags_to_excel.py
   ```

2. The script will create an Excel file named `aws_cost_per_resource.xlsx` in the project directory.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.