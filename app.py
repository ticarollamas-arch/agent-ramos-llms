{
  "blueprint": {
    "metadata": {
      "version": "1.0.0",
      "classification": "MENU 02 — GENERATED PROJECT",
      "projectType": "CLI de Engenharia de Segurança em Docker / Agente Local",
      "language": "pt-BR",
      "ethicalFramework": "Defensivo, Educacional e Auditoria Ativa",
      "complianceStandard": "OWASP Top 10 LLM / Clean Architecture"
    },
    "projectName": "AegisAgent",
    "objective": "Orquestrador de IA local para Termux com RAG e ferramentas de automação.",
    "description": "AegisAgent é um framework de automação inteligente projetado para rodar em ambientes restritos como Termux. Ele utiliza Ollama para inferência local, um sistema de memória RAG persistente e um conjunto de ferramentas modulares para execução de tarefas de engenharia e segurança.",
    "bannerAscii": "    ___    __________  ____  _____    ___              __ \n   /   |  / ____/  _/  _/ / ___/   /   |  ____ ____/ /__  _____\n  / /| | / __/  / /  / /  \\__ \\   / /| | / __ `/ __  / _ \\/ ___/\n / ___ |/ /___ / / _/ /  ___/ /  / ___ |/ / / / /_/ /  __/ /    \n/_/  |_/_____/___/___/ /____/  /_/  |_/_/ /_/\\__,_/\\___/_/     \n",
    "technologies": {
      "primaryLanguages": ["Python 3.10+"],
      "databases": ["JSON (Local Memory)"],
      "libraries": {
        "standardLibrary": ["json", "os", "subprocess", "sys", "pathlib"],
        "thirdParty": [
          { "name": "requests", "version": "^2.31.0", "purpose": "Comunicação com API do Ollama e ferramentas web" },
          { "name": "rich", "version": "^13.7.0", "purpose": "Interface de terminal profissional" }
        ]
      }
    },
    "directoryTree": {
      "core": {
        "type": "directory",
        "children": {
          "orchestrator.py": { "type": "file", "description": "Loop principal e lógica de decisão" },
          "memory.py": { "type": "file", "description": "Gerenciamento de RAG local" }
        }
      },
      "tools": {
        "type": "directory",
        "children": {
          "files.py": { "type": "file", "description": "Manipulação de I/O" },
          "system.py": { "type": "file", "description": "Execução de comandos seguros" }
        }
      },
      "Dockerfile": { "type": "file", "description": "Container para ambiente isolado" },
      "main.py": { "type": "file", "description": "Ponto de entrada" }
    },
    "database": {
      "type": "JSON",
      "engine": "File-based",
      "filePath": "data/memory.json",
      "tables": {
        "memory": {
          "description": "Armazenamento de contexto",
          "columns": [
            { "name": "user_interests", "type": "LIST", "description": "Interesses do usuário" },
            { "name": "history", "type": "LIST", "description": "Histórico de interações" }
          ]
        }
      }
    },
    "security": {
      "classification": "DEFENSIVO",
      "approach": "Sandboxing e Validação de Input",
      "controlledVulnerabilities": ["Command Injection", "Arbitrary File Read"],
      "mitigations": [
        { "threat": "Command Injection", "mitigation": "Uso de shlex.quote e whitelist de comandos permitidos" }
      ]
    },
    "cli": {
      "toolName": "python main.py",
      "commandUsage": "python main.py --interactive",
      "description": "Interface de linha de comando para o agente",
      "args": [
        { "name": "--model", "shortcut": "-m", "type": "string", "default": "llama3", "description": "Modelo Ollama" }
      ]
    },
    "filesContent": {
      "main.py": "import sys\nfrom core.orchestrator import Agent\n\ndef main():\n    agent = Agent()\n    agent.run()\n\nif __name__ == '__main__':\n    main()",
      "core/orchestrator.py": "import json\nfrom tools.files import read_file\n\nclass Agent:\n    def __init__(self):\n        self.memory = 'data/memory.json'\n    \n    def run(self):\n        print('[+] AegisAgent Iniciado')\n        while True:\n            cmd = input('>>> ')\n            if cmd == 'exit': break\n            # Lógica de processamento aqui"
    }
  }
}
}