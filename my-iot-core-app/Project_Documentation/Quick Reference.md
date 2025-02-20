# My IoT Core App

This project simulates traffic intensity monitoring using AWS services, including AWS Lambda and AWS IoT Core. The application consists of a Lambda function that sends notifications based on traffic intensity and a device simulator that interacts with AWS IoT.

## Project Structure

```
my-iot-core-app
├── lambda
│   └── lambda-fuctiion.py       # AWS Lambda function for traffic monitoring
├── device
│   └── device_simulator.py       # Simulates IoT devices
├── iot
│   └── iot_policy.json           # AWS IoT policy for device permissions
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd my-iot-core-app
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**:
   Make sure your AWS credentials are configured. You can do this by running:
   ```
   aws configure
   ```

4. **Deploy the Lambda Function**:
   Use the AWS Management Console or AWS CLI to deploy the Lambda function defined in `lambda/lambda-fuctiion.py`.

5. **Set Up AWS IoT Core**:
   - Create an IoT thing for your device.
   - Attach the policy defined in `iot/iot_policy.json` to your IoT thing.
   - Use the `device/device_simulator.py` to simulate device behavior.

## Usage Guidelines

- The Lambda function will automatically send notifications to an SNS topic when the simulated traffic intensity exceeds 50.
- The device simulator can be modified to publish messages to specific topics or subscribe to receive messages.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.