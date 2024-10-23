# Market Data API Integration and Monitoring System User Manual

This document provides a detailed guide on how to use the **Market Data API Integration and Monitoring System**.

## Overview

The **Market Data API Integration and Monitoring System** is designed to:

- Fetch and store financial market data from the Alpha Vantage API.
- Monitor the health of the API and send alerts via email if issues are detected.
- Perform network diagnostics and verify configuration settings.

## Table of Contents

1. [Running the Main Script](#1-running-the-main-script)
2. [API Authentication Check](#2-api-authentication-check)
3. [Verify Configuration](#3-verify-configuration)
4. [Network Diagnostics](#4-network-diagnostics)
5. [Troubleshooting](#5-troubleshooting)
6. [Email Alerts](#6-email-alerts)

---

## 1. Running the Main Script

To fetch market data from the Alpha Vantage API and store it in the PostgreSQL database, run the main script:

```bash
python api_integration/main.py
```

This will:
- Fetch market data for the specified stock symbol (e.g., TSLA) every minute.
- Store the data in the `market_data` PostgreSQL table.

The script will run for 5 minutes by default. Modify the runtime as needed in the script.

---

## 2. API Authentication Check

To verify if your Alpha Vantage API key is valid, use the `check_auth.py` script:

```bash
python monitoring/check_auth.py
```

- If the API key is valid, the message "API Authentication Successful!" will appear.
- If the authentication fails, an email alert will be sent.

---

## 3. Verify Configuration

Ensure that all required environment variables are properly set by running the `config_verifier.py` script:

```bash
python monitoring/config_verifier.py
```

This will check for missing variables and print out any that are not set.

---

## 4. Network Diagnostics

If you are experiencing network issues, you can run the `network_diagnostics.py` script to check if the Alpha Vantage API server is reachable:

```bash
python monitoring/network_diagnostics.py
```

This script performs a `ping` and `traceroute` to diagnose connectivity issues.

---

## 5. Troubleshooting

- **Database Connection Issues**: Ensure that PostgreSQL is running and that your credentials in the `.env` file are correct.
- **API Rate Limits**: The Alpha Vantage API has a limit of 5 API requests per minute and 500 requests per day. Be mindful of this limit when fetching data.
- **Missing Environment Variables**: If any environment variables are missing, use the `config_verifier.py` script to identify them.

---

## 6. Email Alerts

The system sends email alerts for the following events:

1. **API Authentication Failure**: If the Alpha Vantage API key is invalid.
2. **Network Connectivity Issues**: If the Alpha Vantage server is unreachable.
3. **Monitoring Errors**: Any issues with the API or system monitoring.

Ensure that your email settings in the `.env` file are correctly configured.

To manually test email alerts, run:

```bash
python monitoring/alert.py
```

---

## Conclusion

This system provides a robust solution for monitoring financial market data APIs and ensuring the health of the system through alerts, diagnostics, and configuration verification. 

For any issues or further questions, please refer to the troubleshooting section or contact support.