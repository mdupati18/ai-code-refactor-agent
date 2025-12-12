import json
from analyzer.analyzer import CodeAnalyzer
from refactor.refactor_agent import RefactorAgent
from utils.file_utils import write_file

CONFIG_PATH = "agent_config.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def run(file_path):
    config = load_config()

    analyzer = CodeAnalyzer(config)
    agent = RefactorAgent()

    print("🔍 Analyzing file...")
    analysis = analyzer.analyze(file_path)
    print(json.dumps(analysis, indent=2))

    print("\n🤖 Refactoring with AI agent...")
    improved_code = agent.refactor(file_path)

    output_path = file_path.replace(".py", "_refactored.py")
    write_file(output_path, improved_code)

    print(f"\n✅ Refactored file saved at: {output_path}")

if __name__ == "__main__":
    run("examples/sample_before.py")
