# ansible
This repository contains Ansible playbooks and other services that are in the works

## Playbooks
- Performs tasks

## Poller Service
- Calls tasks in an multithreaded envirinment to execute efficiently.

## Framework

Implementing a framework to add modularity to the code.
This is the standard filestructure that should be maintained, any changes in this structure will result in flawed functionality.

### Filestructure

```
framework/
├── roles/
│   ├── servicenow/
│   │   ├── tasks/
│   │   │   ├── fetch-tickets.yml
│   │   │   ├── update-or-close-tickets.yml
│   │   ├── vars/
│   │   │   └── main.yml
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── files/
│   │   ├── templates/
│   ├── helpers/
│   │   ├── tasks/
│   │   │   └── helper2.yml
│   │   ├── library/
│   │   │   └── helper1.py
│   ├── otherapis/
│   │   ├── tasks/
│   │   │   └── graphql-calls.yml
└── main_yaml/
    ├── main.yml
```