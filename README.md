# shotalyzer

AWS snapshot analyzer

## About

This demo project uses boto3 library

## Configuring

Create AWS configuration profile e.g.

```
aws configure --profile shotty
```

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes or snapshots
*subcommand* depends on command
*project* is optional
