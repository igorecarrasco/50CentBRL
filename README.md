# 50CentBRL bot

This bot will post the exchange rate between the US Dollar and Brazilian Real every half hour during trading hours in the Brazilian stock exchange. The rate posted will be divided by two and overlaid on top of a random picture of Curtis James Jackson III, the rapper 50 Cent.

## Architecture

This application will be deployed as an HTTP-triggered Cloud Function on Google Cloud Platform, and triggered by Cloud Scheduler. It's a `Python 3.7` app. Dependency management is handled by `pipenv`, code formatting by `black`, linting and type checking by `mypy`.

## License


